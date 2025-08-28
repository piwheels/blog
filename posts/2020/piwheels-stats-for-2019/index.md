In 2019, a total of **9,218,822** packages were downloaded, taking the total to **14,745,528**. This
saved **128 years 5 months** during 2019, taking us to over **172 years** saved overall. **37TB** of
files were downloaded, taking the total to **51TB**.

- Average daily downloads:
    - 2018: **14,519**
    - 2019: **25,257**
- Average monthly downloads:
    - 2018: **429,519**
    - 2019: **768,235**
- Most downloads in one day:
    - 2018: **25,389** on 30 November
    - 2019: **39,153** on 4 December
- Most downloads in one month:
    - 2018: **662,621** in December (**21,445** daily average)
    - 2019: **1,017,563** in December (**32,824** daily average) / **1,014,577** in November
        (**33,819** daily average)
- Bandwidth used from downloads:
    - 2018: **12TB**
    - 2019: **37TB**

Each month had over **500,000** downloads, reaching over **1 million** in November and December:

<figure class="aligncenter size-large">
<img src="images/downloads-2019.png" />
</figure>

Each month saved over 7 years, topping out at 17 years:

<figure class="aligncenter size-large">
<img src="images/time-saved-2019.png" />
</figure>

- 4 December 2019 was the biggest day on record, with **39,153** downloads.
- The month of December recorded the most downloads at **1,017,563** (November had more on average
    due to Christmas days being lower, but December is a 31 day month).
- December also saw the most time saved with **17 years 9 months 24 days** (again, November had
    more on average).

## Top 30 packages

1.  **[pycparser](https://www.piwheels.org/project/pycparser)** (629,037)
2.  **[numpy](https://www.piwheels.org/project/numpy)** (230,086)
3.  **[PyYAML](https://www.piwheels.org/project/PyYAML)** (208,477)
4.  **[cffi](https://www.piwheels.org/project/cffi)** (190,941)
5.  **[MarkupSafe](https://www.piwheels.org/project/MarkupSafe)** (172,981)
6.  **[tensorflow](https://www.piwheels.org/project/tensorflow)** (170,210)
7.  **[cryptography](https://www.piwheels.org/project/cryptography)** (164,812)
8.  **[future](https://www.piwheels.org/project/future)** (162,354)
9.  **[paho-mqtt](https://www.piwheels.org/project/paho-mqtt)** (144,635)
10. **[aiohttp](https://www.piwheels.org/project/aiohttp)** (136,185)
11. **[opencv-python](https://www.piwheels.org/project/opencv-python)** (129,328)
12. **[multidict](https://www.piwheels.org/project/multidict)** (116,325)
13. **[yarl](https://www.piwheels.org/project/yarl)** (115,071)
14. **[RPi.GPIO](https://www.piwheels.org/project/RPi.GPIO)** (114,513)
15. **[voluptuous-serialize](https://www.piwheels.org/project/voluptuous-serialize)** (109,972)
16. **[SQLAlchemy](https://www.piwheels.org/project/SQLAlchemy)** (109,169)
17. **[docopt](https://www.piwheels.org/project/docopt)** (104,735)
18. **[home-assistant-frontend](https://www.piwheels.org/project/home-assistant-frontend)**
    (102,820)
19. **[ruamel.yaml](https://www.piwheels.org/project/ruamel.yaml)** (100,600)
20. **[ifaddr](https://www.piwheels.org/project/ifaddr)** (100,573)
21. **[Adafruit-PureIO](https://www.piwheels.org/project/Adafruit-PureIO)** (100,051)
22. **[python-slugify](https://www.piwheels.org/project/python-slugify)** (99,183)
23. **[scipy](https://www.piwheels.org/project/scipy)** (96,895)
24. **[gTTS-token](https://www.piwheels.org/project/gTTS-token)** (85,083)
25. **[PyNaCl](https://www.piwheels.org/project/PyNaCl)** (84,663)
26. **[mutagen](https://www.piwheels.org/project/mutagen)** (82,714)
27. **[pycryptodome](https://www.piwheels.org/project/pycryptodome)** (81,741)
28. **[spidev](https://www.piwheels.org/project/spidev)** (81,037)
29. **[PyQRCode](https://www.piwheels.org/project/PyQRCode)** (78,603)
30. **[sysv_ipc](https://www.piwheels.org/project/sysv_ipc)** (77,846)

## Python version usage

At the start of the year, most downloads were for Python 3.5 which is in Raspbian Stretch, but as
soon as Buster was released, Python 3.7 began to take over:

<figure class="wp-block-image size-large">
<img src="images/pyvers2019.png" />
</figure>

There's a steady trickle of Python 2.7 downloads, but note that this does not fairly represent
usage as we do not provide wheels for Python 2, so any downloads are for pure Python packages.
There's also a small number of people using out-of-distribution Python versions 3.6 and 3.8 (the
red section). We are barely seeing any Python 3.4 downloads, perhaps due to the fact Raspbian Jessie
was never configured to use piwheels, and the pip in Jessie needs upgrading to be able to use it.

## Architectures

The Pi 2, 3 and 4 all identify as armv7l, whereas Pi 1 and Zero are armv6l. armv7l usage has always
accounted a huge majority of downloads (88% in 2018), and it's pretty much stayed around that mark
through 2019:

<figure class="wp-block-image size-large">
<img src="images/arch2019.png" />
</figure>

## Operating systems

The vast majority of downloads are from Raspbian (over 90%). As observed with Python versions, much
of the usage switched from Stretch to Buster after its release in July:

<figure class="wp-block-image size-large">
<img src="images/distro_versions.png" />
</figure>

There was a noticeable bump of users reporting Raspbian (testing) before Buster was officially
launched.

## Downloads through the day

Our busiest hour is between 7pm-8pm. All afternoon/evening UTC we are at our busiest:

<figure class="wp-block-image size-large">
<img src="images/downloads-day-2019.png" />
</figure>

## 2020 vision

There's no Raspbian release scheduled this year, so we won't be introducing any new Python
versions until Raspbian Bullseye arrives mid-2021.

We have been working on a few new features, including a JSON API which dynamically populates our
project pages, and which you'll be able to use to programmatically find out info about what
packages we provide. We have also made it possible to calculate apt dependencies for a wheel based
on packages providing required shared object files, as described in a [previous
post](https://blog.piwheels.org/how-to-work-out-the-missing-dependencies-for-a-python-package/),
although it's not yet been calculated for older projects. Hopefully we'll get this sorted, and it
being included in the project pages JSON API will make it even easier. We're working on deploying
these changes very shortly!

If you're interested in following piwheels project updates, we tweet daily and monthly stats at
[@piwheels](https://twitter.com/piwheels). You can also follow me
[@ben_nuttall](https://twitter.com/ben_nuttall) and Dave
[@waveform80](https://twitter.com/waveform80).

*The piwheels project wouldn't be possible without considerable support from* [*Mythic
Beasts*](https://www.mythic-beasts.com/)*, who provide storage and cloud Pis. The Pi platform is so
straightforward, it's been a pleasure to use, allowing us to scale up builder Pis with ease. We
highly recommend using this (very affordable) service for real* [*Pi
testing*](https://www.mythic-beasts.com/order/rpi) *for your projects.*
