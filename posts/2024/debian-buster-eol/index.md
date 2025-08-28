Debian Buster was released on [6 July 2019](https://www.debian.org/News/2019/20190706), and it's
been supported by the Debian team for over five years. On 30 June 2024 it reached its [long term
support end of life](https://wiki.debian.org/DebianReleases). Therefore we have stopped building new
package releases on Buster, for the `cp37m` ABI. We will not delete existing `cp37m` wheels, just
not build any new ones.

<figure class="block-image">
<img src="images/buster.jpg" />
<figcaption>Thank you for your service, Buster. You were a good boy.</figcaption>
</figure>

Now that the sun has set on Buster, we'll return to building for just two ABIs, until next summer
when Debian Trixie will be released, and we'll go back up to three.
