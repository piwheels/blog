Debian Buster was released on [14 August 2021](https://www.debian.org/releases/bullseye/), and it's
been supported by the Debian team for over five years. Yesterday, 31 August 2026 it reached its
[long term support end of life](https://www.debian.org/releases/). Therefore we have stopped
building new package releases on Buster, for the `cp39` ABI.

<figure class="block-image">
<img src="images/bullseye.webp" />
<figcaption>Thank you for your service, Bullseye. The end is neigh.</figcaption>
</figure>

Now that the sun has set on Bullseye, we'll return to building for just two ABIs, until next summer
when Debian Forkie will be released, and we'll go back up to three.

This also draws a conclusion to the [ABI ordering
bug](https://github.com/piwheels/piwheels/issues/288) we have suffered with on piwheels. Since ABIs
were traditionally sorted effectively alphabetically, once Python versions hit double digits, that
ordering broke. This was mostly fine except in some cases affected by builds being built on cp311
and cp313 before cp39, or if a pure Python wheel required 3.10+, the project page would wrongly
indicate that the wheel was supported on cp39. Now that we've retired the last single-digit ABI, we
can consider that bug to be closed.