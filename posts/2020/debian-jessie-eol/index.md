**Update 2020-07-01: The EOL date has now been reached, and Jessie support has ended.**

Debian Jessie was released on [25 April 2015](https://www.debian.org/News/2015/20150426), and it's
been supported by the Debian team for over five years. On 30 June 2020 it reaches its [long term
support end of life](https://wiki.debian.org/DebianReleases). Therefore on this date we will stop
building new package releases on Jessie, for the cp34m ABI. We will not delete existing cp34m
wheels, just not build any new ones.

<figure class="aligncenter size-large">
<img src="images/Jessie_Toy_Story.png" />
<figcaption>Thank you for your service, Jessie</figcaption>
</figure>

The piwheels repository was launched a few months before the release of Debian Stretch, so we
started building for Jessie and later added support for multiple ABIs, and rebuilt everything for
Stretch. Two years on, Buster was released and we started building for a third distro version and
ABI.

Now that the sun is setting on Jessie, we'll return to building for just two ABIs, until next
summer when Debian Bullseye will be released, and we'll go back up to three.

Unrelated to this, we'll have to introduce the concept of not only distinguishing ABIs, but
multiple architectures as we plan to introduce [support for
aarch64](https://blog.piwheels.org/raspberry-pi-os-64-bit-aarch64/).

The main piwheels.org server itself is actually still running on Jessie, because we've left it
running since launch. But now's the time to upgrade so we're moving to a new Pi running Buster,
which should see us through to 2024.

Even though piwheels has always built wheels for Jessie, it ships with such an old version of pip,
it wasn't possible to pre-configure Raspbian images with the necessary piwheels config. It's
possible to use piwheels if you upgrade pip, or explicitly set the extra index with `-i` every time.
And I guess most Jessie users aren't aware, so we see *incredibly low* numbers of downloads from
Jessie users. In all time, we've seen 12 million downloads for Stretch, 8 million for Buster, and
... 24,000 for Jessie. So far this year: 5 million for Buster, 1 million for Stretch, 1,000 for
Jessie.

If you're still using Raspbian Jessie, you can still use piwheels to get any packages released
before the end of this month. But if your Pi is connected to the internet and you're installing new
stuff on it, you should probably upgrade!
