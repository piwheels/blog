from datetime import datetime
from pathlib import Path

import pypandoc
import requests
import yaml
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field, model_validator
from structlog import get_logger


POSTS_DIR = Path(__file__).parent.parent / "posts"
POSTS_DIR.mkdir(exist_ok=True)

logger = get_logger()


class WithRendered(BaseModel):
    rendered: str


class Post(BaseModel):
    published: datetime = Field(alias="date")
    modified: datetime
    slug: str
    title: WithRendered
    content: WithRendered
    tags_list: list[str] = []
    class_list: list[str] = []

    @model_validator(mode="after")
    def validate_tags(self):
        for value in self.class_list:
            parts = value.split("-")
            if parts[0] == "tag":
                tag = "-".join(parts[1:])
                if "debian-" in tag:
                    tag = tag.replace("debian-", "")
                elif "raspbian-" in tag:
                    tag = tag.replace("raspbian-", "")
                self.tags_list.append(tag)
        return self


def fetch_posts_json(url: str) -> list[Post]:
    logger.info("Fetching posts", url=url)
    response = requests.get(url)
    response.raise_for_status()
    posts_data = response.json()
    logger.info("Fetched posts", count=len(posts_data))
    return [Post.model_validate(post) for post in posts_data]


def save_posts(url: str):
    posts = fetch_posts_json(url)
    for post in posts:
        save_post(post)


def save_post(post: Post):
    post_dir = POSTS_DIR / str(post.published.year) / post.slug
    post_dir.mkdir(exist_ok=True, parents=True)
    logger.info("Saving post", slug=post.slug, path=str(post_dir))
    metadata = {
        "title": post.title.rendered,
        "slug": post.slug,
        "published": post.published.isoformat(timespec="seconds"),
        "modified": post.modified.isoformat(timespec="seconds"),
        "tags": post.tags_list,
        "author": "Ben Nuttall"
    }
    metadata_file = post_dir / "meta.yml"
    metadata_file.write_text(yaml.dump(metadata))
    post_file = post_dir / "index.md"
    bs = BeautifulSoup(post.content.rendered, "html.parser")
    for img_tag in bs.find_all("img"):
        source = img_tag["src"]
        if source.startswith("http"):
            r = requests.get(source)
            img_path = post_dir / "images" / Path(source).name
            img_path.parent.mkdir(exist_ok=True)
            if not img_path.exists():
                logger.info("Downloading image", src=source)
                img_path.write_bytes(r.content)
            img_tag["src"] = f"images/{Path(source).name}"
            for attr in ("srcset", "aria-describedby"):
                if attr in img_tag.attrs:
                    del img_tag[attr]
        else:
            logger.warn("Skipping non-http image", src=source)
        for attr in ("alt", "class", "decoding", "height", "loading", "width", "sizes"):
            if attr in img_tag.attrs:
                del img_tag[attr]

    for a_tag in bs.find_all("a", href=True):
        for attr in ("data-id", "data-type"):
            if attr in a_tag.attrs:
                del a_tag[attr]
        if a_tag["href"].startswith("https://blog.piwheels.org/"):
            img_tag = a_tag.find("img")
            if img_tag:
                a_tag.unwrap()

    html = str(bs)
    replacements = {
        "“": '"',
        "”": '"',
        "„": '"',
        "‟": '"',
        "‘": "'",
        "’": "'",
        "‚": "'",
        "‛": "'",
    }
    for a, b in replacements.items():
        html = html.replace(a, b)

    markdown = pypandoc.convert_text(
        html,
        "markdown+fenced_code_blocks",
        format="html",
        extra_args=["--wrap=auto", "--columns=100"]
    ).replace("\\'", "'")
    post_file.write_text(markdown)


if __name__ == "__main__":
    urls = [
        "https://blog.piwheels.org/wp-json/wp/v2/posts?per_page=100",
    ]
    for url in urls:
        save_posts(url)
