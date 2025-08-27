from datetime import datetime

import requests
from pydantic import BaseModel, model_validator
from structlog import get_logger


URL = "https://blog.piwheels.org/wp-json/wp/v2/posts?per_page=100"

logger = get_logger()


class WithRendered(BaseModel):
    rendered: str


class Post(BaseModel):
    date: datetime
    slug: str
    title: WithRendered
    tags_list: list[str] = []
    class_list: list[str] = []

    @model_validator(mode="after")
    def validate_tags(self):
        for value in self.class_list:
            parts = value.split("-")
            if parts[0] == "tag":
                self.tags_list.append("-".join(parts[1:]))
        return self


def fetch_posts() -> list[Post]:
    logger.info("Fetching posts", url=URL)
    response = requests.get(URL)
    response.raise_for_status()
    posts_data = response.json()
    logger.info("Fetched posts", count=len(posts_data))
    return [Post.model_validate(post) for post in posts_data]


def get_new_url(post: Post) -> str:
    return f"/{post.date.year}/{post.date.strftime('%m')}/{post.slug}/"


def make_post_rewrite_rule(post: Post) -> str:
    old_url = post.slug
    new_url = get_new_url(post)
    return f"RewriteRule ^{old_url}/?$ {new_url} [R=301,L]"


def make_tag_rewrite_rule(tag: str) -> str:
    if "debian-" in tag:
        new_tag = tag.replace("debian-", "")
    elif "raspbian-" in tag:
        new_tag = tag.replace("raspbian-", "")
    else:
        new_tag = tag
    return f"RewriteRule ^tag/{tag}/?$ /tags/{new_tag}/ [R=301,L]"


if __name__ == "__main__":
    posts = fetch_posts()

    for post in posts:
        rule = make_post_rewrite_rule(post)
        print(rule)

    tags = set()
    for post in posts:
        tags |= set(post.tags_list)

    for tag in tags:
        rule = make_tag_rewrite_rule(tag)
        print(rule)
