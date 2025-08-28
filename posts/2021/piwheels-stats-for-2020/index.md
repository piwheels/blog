In 2020, a total of **16,184,523** packages were downloaded, taking the total to **30,815,907**.
This saved **269 years 3 months** during 2020, taking us to over **441 years** saved overall.
**52TB** of files were downloaded, taking the total to **103TB**.

- Average daily downloads:
    - 2019: **25,257**
    - 2020: **44,220**
- Average monthly downloads:
    - 2019: **768,235**
    - 2020: **1,326,600**
- Most downloads in one day:
    - 2019: **39,153** on 4 December
    - 2020: **105,826** on 15 December
- Most downloads in one month:
    - 2019: **1,017,563** in December (**32,824** daily average) / **1,014,577** in November
        (**33,819** daily average)
    - 2020: **1,850,781** in October (**59,702** daily average)
- Bandwidth used from downloads:
    - 2019: **37TB**
    - 2020: **52TB**

Apart from February (short month, slightly under), each month had over **1 million downloads**. Four
of the last five months had over **1.5 million**.

<figure class="aligncenter size-large">
<img src="images/downloads-by-month-1.png" />
</figure>

15 December 2020 was the biggest day on record, with **105,826** downloads.

The month of October recorded the most downloads at **1,850,781**.

## Top 30 packages

Incredibly, numpy was downloaded over a million times this year!

1.  **[numpy](https://www.piwheels.org/project/numpy)** (1,004,056)
2.  **[dogpile-cache](https://www.piwheels.org/project/dogpile-cache)** (389,999)
3.  **[webrtcvad-wheels](https://www.piwheels.org/project/webrtcvad-wheels)** (356,793)
4.  **[pyyaml](https://www.piwheels.org/project/pyyaml)** (351,503)
5.  **[sentry-sdk](https://www.piwheels.org/project/sentry-sdk)** (350,834)
6.  **[semantic-version](https://www.piwheels.org/project/semantic-version)** (314,402)
7.  **[cffi](https://www.piwheels.org/project/cffi)** (301,478)
8.  **[markdown](https://www.piwheels.org/project/markdown)** (284,277)
9.  **[flask-login](https://www.piwheels.org/project/flask-login)** (266,479)
10. **[pycparser](https://www.piwheels.org/project/pycparser)** (259,366)
11. **[requests](https://www.piwheels.org/project/requests)** (210,274)
12. **[markupsafe](https://www.piwheels.org/project/markupsafe)** (206,343)
13. **[cryptography](https://www.piwheels.org/project/cryptography)** (198,981)
14. **[paho-mqtt](https://www.piwheels.org/project/paho-mqtt)** (198,747)
15. **[octoprint-firmwarecheck](https://www.piwheels.org/project/octoprint-firmwarecheck)**
    (184,992)
16. **[filetype](https://www.piwheels.org/project/filetype)** (181,539)
17. **[opencv-python](https://www.piwheels.org/project/opencv-python)** (179,079)
18. **[pyusb](https://www.piwheels.org/project/pyusb)** (170,359)
19. **[zope-component](https://www.piwheels.org/project/zope-component)** (165,536)
20. **[adafruit-pureio](https://www.piwheels.org/project/adafruit-pureio)** (162,949)
21. **[docopt](https://www.piwheels.org/project/docopt)** (161,961)
22. **[pillow](https://www.piwheels.org/project/pillow)** (160,590)
23. **[rpi-gpio](https://www.piwheels.org/project/rpi-gpio)** (150,513)
24. **[pynacl](https://www.piwheels.org/project/pynacl)** (148,723)
25. **[future](https://www.piwheels.org/project/future)** (145,075)
26. **[adafruit-platformdetect](https://www.piwheels.org/project/adafruit-platformdetect)**
    (143,978)
27. **[tornado](https://www.piwheels.org/project/tornado)** (141,605)
28. **[adafruit-blinka](https://www.piwheels.org/project/adafruit-blinka)** (140,604)
29. **[bcrypt](https://www.piwheels.org/project/bcrypt)** (138,836)
30. **[sysv-ipc](https://www.piwheels.org/project/sysv-ipc)** (136,934)

## Python version usage

Most searches are from Python 3.7, the default in Debian Buster (55%). Second is Python 2.7 with
31%, followed by 3.5 (the default in Stretch) with 7.5%:

<figure class="wp-block-image size-large">
<img src="images/py-vers-1.png" />
</figure>

## Architectures

armv7l (Pi 2/3/4 platform) is still a majority architecture with 91% of searches from Arm devices,
with armv6l (Pi 1/Zero) taking under 5%:

<figure class="wp-block-image size-large">
<img src="images/debian-arch-1.png" />
</figure>

Raspberry Pi released a beta of a 64-bit version of the official OS earlier in the year, and that's
starting to grow in usage. It's currently up to 4.2%, and those users are currently not served by
piwheels as we don't build aarch64 platform wheels.

## Operating systems

The vast majority of downloads are from Raspbian / Pi OS (over 98%). Of these, 76% are Buster, 24%
are Stretch and practically none are Jessie:

<figure class="wp-block-image size-large">
<img src="images/debian-usage-1.png" />
</figure>

## Downloads through the day

Our busiest hour has moved earlier in the day, now between 3pm-4pm. All afternoon/evening UTC we are
at our busiest:

<figure class="wp-block-image size-large">
<img src="images/downloads-by-hour-1.png" />
</figure>

## 2020 features

We have been working on a lot of new features throughout the year, including [deletion and
yanking](https://blog.piwheels.org/new-features-deletion-yanking-and-more/), [canonicalising package
names](https://blog.piwheels.org/canonicalise-all-the-things/), [Requires-Python support, new
project page layout and a new JSON
API](https://blog.piwheels.org/requires-python-support-new-project-page-layout-and-a-new-json-api/).
I've also produced quarterly stats: [2020Q1](https://blog.piwheels.org/piwheels-stats-2020q1/),
[2020Q2](https://blog.piwheels.org/piwheels-stats-2020q2/),
[2020Q3](https://blog.piwheels.org/piwheels-stats-2020q3/) and
[2020Q4](https://blog.piwheels.org/piwheels-stats-2020q4/).

## 2021 vision

There's a new Debian release scheduled this summer, so we will be introducing a new Python version
when Debian Bullseye arrives in the summer. We'll also aim to start work on aarch64 support.

If you're interested in following piwheels project updates, we tweet daily and monthly stats at
[@piwheels](https://twitter.com/piwheels). You can also follow me
[@ben_nuttall](https://twitter.com/ben_nuttall) and Dave
[@waveform80](https://twitter.com/waveform80).

*The piwheels project wouldn't be possible without considerable support from* [*Mythic
Beasts*](https://www.mythic-beasts.com/)*, who provide storage, bandwidth and cloud Pis. The Pi
platform is so straightforward, it's been a pleasure to use, allowing us to scale up builder Pis
with ease. We highly recommend using this (very affordable) service for real* [*Pi
testing*](https://www.mythic-beasts.com/order/rpi) *for your projects.*

I've also been working on a Python library and command line interface to the Mythic Beasts Pi Cloud
service, called **hostedpi**, which is out in beta now and will be fully released soon. You can find
it on [GitHub](https://github.com/piwheels/hostedpi),
[readthedocs](https://hostedpi.readthedocs.io/en/latest/),
[PyPI](https://pypi.org/project/hostedpi/) and (of course)
[piwheels](https://www.piwheels.org/project/hostedpi/).
