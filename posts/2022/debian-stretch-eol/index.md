Debian Stretch was released on [17 June 2017](https://www.debian.org/News/2015/20150426), and it's
been supported by the Debian team for over five years. On 30 June 2022 it reached its [long term
support end of life](https://wiki.debian.org/DebianReleases). Therefore we have stopped building new
package releases on Stretch, for the cp35m ABI. We will not delete existing cp35m wheels, just not
build any new ones.

<figure class="aligncenter size-large">
<img src="images/Stretch-1024x576.jpg" />
<figcaption>Thank you for your service, Stretch</figcaption>
</figure>

Now that the sun has set on Stretch, we'll return to building for just two ABIs, until next summer
when Debian Bookworm will be released, and we'll go back up to three.

Unrelated to this, we'll have to introduce the concept of not only distinguishing ABIs, but
multiple architectures as we plan to introduce [support for
aarch64](https://blog.piwheels.org/raspberry-pi-os-64-bit-aarch64/).
