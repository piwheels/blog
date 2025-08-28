Big news today: the [Raspberry Pi 4 is
out](https://www.raspberrypi.org/blog/raspberry-pi-4-on-sale-now-from-35) — and slightly ahead of
the [official release of Debian Buster](https://twitter.com/debian/status/1138715072841146370),
[Raspbian Buster is released](https://www.raspberrypi.org/downloads/raspbian/) too.

So what does this mean for piwheels?

## Raspberry Pi 4

The Raspberry Pi 4 is a huge step forward in performance. It's a much faster computer. However,
it's not a new architecture. Like the Pi3/3+ it contains an Armv8 CPU which generally runs a 32-bit
(Armv7) operating system in Pi-1 compatible userland (Armv6). This means Armv7-optimised (NEON) code
will work on it, but so will Armv6 code, just like the Pi 2 and 3.

<figure class="block-image">
<img src="images/raspberry-pi-4-1024x732.jpg" />
</figure>

## Raspbian Buster

Whether you're on a Pi 1, 2, 3, 4 or Zero, you can and should use Raspbian Buster. It's now the
recommended and supported operating system for all Raspberry Pi models.

<figure class="block-image">
<img src="images/buster-1024x576.jpg" />
</figure>

Raspbian Buster ships **Python 3.7** — which means a whole new set of wheels is required for pip
installs to be fast.

We had hoped to have them all ready by now, but we've been busy dealing with a series of issues
related to a piwheels system upgrade. It's a long story, which involves Dave following a [rabbit
hole](https://github.com/agronholm/cbor2/pull/51). We've still been operational the whole time,
serving hundreds of thousands of downloads, but not building any new package releases for a while,
and have not been able to start building Python 3.7 wheels yet.

As a temporary measure, I've manually built all the most popular packages for Jessie, Stretch and
Buster, and imported them into piwheels.

There's still a bit of work to do to get piwheels building again, but we're nearly there. Watch
this space!

**Update 27 June: we are now building again. It will probably take a couple of weeks to catch up.**
