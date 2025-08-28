In 2020, a total of **36,724,799** packages were downloaded, taking the total to **67,695,042**.
This saved **159 years** during 2020, taking us to over **600 years** saved overall. **50TB** of
files were downloaded, taking the total to **153TB**.

- Average daily downloads:
    - 2020: **44,220**
    - 2021: **100,615**
- Average monthly downloads:
    - 2020: **1,326,600**
    - 2021: **3,060,399**
- Most downloads in one day:
    - 2020: **105,826** on 15 December
    - 2021: **314,030**
- Most downloads in one month:
    - 2020: **1,850,781** in October (**59,702** daily average)
    - 2021: **4,263,286** in October (**137,525** daily average)
- Bandwidth used from downloads:
    - 2020: **52TB**
    - 2021: **50TB**

Apart from January, each month had over **2 million downloads**. The last three months all passed
**3.5 million**.

<figure class="aligncenter size-full">
<img src="images/year-downloads-by-month.png" />
</figure>

12 October 2021 was the biggest day on record, with ****314,030**** downloads.

The month of October recorded the most downloads at **4,263,286**.

## Top 30 packages

1.  **[requests](https://www.piwheels.org/project/requests)** (684,141)
2.  **[numpy](https://www.piwheels.org/project/numpy)** (546,668)
3.  **[setuptools](https://www.piwheels.org/project/setuptools)** (524,595)
4.  **[pip](https://www.piwheels.org/project/pip)** (460,168)
5.  **[idna](https://www.piwheels.org/project/idna)** (443,288)
6.  **[urllib3](https://www.piwheels.org/project/urllib3)** (425,864)
7.  **[chardet](https://www.piwheels.org/project/chardet)** (420,834)
8.  **[certifi](https://www.piwheels.org/project/certifi)** (407,524)
9.  **[websocket-client](https://www.piwheels.org/project/websocket-client)** (404,080)
10. **[six](https://www.piwheels.org/project/six)** (403,825)
11. **[importlib-metadata](https://www.piwheels.org/project/importlib-metadata)** (392,717)
12. **[pillow](https://www.piwheels.org/project/pillow)** (388,883)
13. **[typing-extensions](https://www.piwheels.org/project/typing-extensions)** (387,626)
14. **[pyyaml](https://www.piwheels.org/project/pyyaml)** (368,142)
15. **[attrs](https://www.piwheels.org/project/attrs)** (348,164)
16. **[cffi](https://www.piwheels.org/project/cffi)** (337,885)
17. **[click](https://www.piwheels.org/project/click)** (337,042)
18. **[wheel](https://www.piwheels.org/project/wheel)** (329,901)
19. **[jinja2](https://www.piwheels.org/project/jinja2)** (316,285)
20. **[h11](https://www.piwheels.org/project/h11)** (315,878)
21. **[octoprint-pisupport](https://www.piwheels.org/project/octoprint-pisupport)** (309,915)
22. **[octoprint-firmwarecheck](https://www.piwheels.org/project/octoprint-firmwarecheck)**
    (307,221)
23. **[markupsafe](https://www.piwheels.org/project/markupsafe)** (277,070)
24. **[zipp](https://www.piwheels.org/project/zipp)** (276,298)
25. **[python-dateutil](https://www.piwheels.org/project/python-dateutil)** (264,416)
26. **[charset-normalizer](https://www.piwheels.org/project/charset-normalizer)** (256,203)
27. **[tornado](https://www.piwheels.org/project/tornado)** (243,797)
28. **[pycparser](https://www.piwheels.org/project/pycparser)** (239,223)
29. **[async-timeout](https://www.piwheels.org/project/async-timeout)** (238,955)
30. **[immutabledict](https://www.piwheels.org/project/immutabledict)** (231,729)

## Python version usage

Most searches are from Python 3.7, the default in Debian Buster (67%). Second is Python 2.7 with
15%, followed by 3.9 (the default in Bullseye, which was only released in the summer) with 9%:

<figure class="wp-block-image size-full">
<img src="images/year-py-vers.png" />
</figure>

## Architectures

armv7l (Pi 2/3/4 and Zero 2 platform) is still a majority architecture with 85% of searches from Arm
devices, with aarch64 rising beyond 10% and armv6l (Pi 1/Zero) dropping below 4%:

<figure class="wp-block-image size-full">
<img src="images/year-debian-arch.png" />
</figure>

## Operating systems

The vast majority of downloads are from Raspberry Pi OS (over 98%). Of these, 86% are Buster, 7.5%
are Bullseye (released in the summer), 6.6% are Stretch.

<figure class="wp-block-image size-full">
<img src="images/year-debian-usage.png" />
</figure>

## Downloads through the day

Our busiest hour is still between 3pm-4pm. All afternoon/evening UTC we are at our busiest:

<figure class="wp-block-image size-full">
<img src="images/year-downloads-by-hour.png" />
</figure>

## Year-on-year

We have been nearly doubling every year, but this year we more than doubled downloads:

<figure class="wp-block-image size-full">
<img src="images/year-downloads-by-year.png" />
</figure>

Check out the source of this post in a Jupyter notebook:
<a href="https://github.com/piwheels/stats/blob/master/2021.ipynb">https://github.com/piwheels/stats/blob/master/2021.ipynb</a>

If you're interested in following piwheels project updates, we tweet daily and monthly stats at
[@piwheels](https://twitter.com/piwheels). You can also follow me
[@ben_nuttall](https://twitter.com/ben_nuttall) and Dave
[@waveform80](https://github.com/waveform80).

*The piwheels project wouldn't be possible without considerable support from* [*Mythic
Beasts*](https://www.mythic-beasts.com/)*, who provide storage, bandwidth and cloud Pis. The Pi
platform is so straightforward, it's been a pleasure to use, allowing us to scale up builder Pis
with ease. We highly recommend using this (very affordable) service for real* [*Pi
testing*](https://www.mythic-beasts.com/order/rpi) *for your projects.*
