Raspberry Pi have just
[released](https://www.raspberrypi.com/news/trixie-the-new-version-of-raspberry-pi-os/) their
operating system images based on [Debian Trixie](https://www.debian.org/releases/trixie/).

Over the last few weeks, we've been working hard behind the scenes to prepare for this, building
armv7 and armv6 wheels for the cp313 ABI, and we're pleased to announce we've completed the backlog
and fully support Trixie at the time of launch.

<figure class="block-image">
<img src="images/trixie.png" />
</figure>

When we started the piwheels project, there were around 106,000 packages. Now there are over
684,000. It takes a lot of effort to churn through all these, so it's taken several weeks to catch
up. Now we're up-to-date and building new packages as they're released.

Note we still only build for the 32-bit operating system images, not aarch64.

Next summer will see Debian Bullseye go end-of-life, so we'll stop building for it then.