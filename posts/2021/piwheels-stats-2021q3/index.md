In the period of July — September 2021, **7,047,854** packages were downloaded from piwheels,
bringing the total to **55,657,694**. This has saved **33 years** in the period, and **558 years**
in total! There were **48,256,952** pip searches, **875,834** project page hits, **397,834** web
page hits and **1,094,432** project JSON downloads in the period.

<figure class="aligncenter size-full">
<img src="images/downloads-by-month.png" />
</figure>

There were 7 days surpassing **100k** downloads, a peak of **over 120k**, and averaged at **76k**
per day:

<figure class="aligncenter size-full">
<img src="images/downloads-by-day-1.png" />
</figure>

<figure class="aligncenter size-full">
<img src="images/searches-by-day-1.png" />
</figure>

Downloads saved around between **10** and **11** years per month. It seems this is falling,
presumably due to more downloads coming from faster platforms (Pi 3/4 vs 1/Zero).

<figure class="aligncenter size-full">
<img src="images/time-saved-by-month-1.png" />
</figure>

The top 10 downloads were:

1.  **[requests](https://www.piwheels.org/project/requests)** (116,496)
2.  **[six](https://www.piwheels.org/project/six)** (102,660)
3.  **[numpy](https://www.piwheels.org/project/numpy)** (100,423)
4.  **[pip](https://www.piwheels.org/project/pip)** (98,708)
5.  **[idna](https://www.piwheels.org/project/idna)** (94,551)
6.  **[importlib-metadata](https://www.piwheels.org/project/importlib-metadata)** (93,747)
7.  **[urllib3](https://www.piwheels.org/project/urllib3)** (91,259)
8.  **[certifi](https://www.piwheels.org/project/certifi)** (87,703)
9.  **[typing-extensions](https://www.piwheels.org/project/typing-extensions)** (85,543)
10. **[pillow](https://www.piwheels.org/project/pillow)** (83,796)

The top 10 pip searches were:

1.  **[pip](https://www.piwheels.org/project/pip)** (7,423,597)
2.  **[wheel](https://www.piwheels.org/project/wheel)** (4,427,701)
3.  **[setuptools](https://www.piwheels.org/project/setuptools)** (3,375,412)
4.  **[pyrogram](https://www.piwheels.org/project/pyrogram)** (1,762,252)
5.  **[future](https://www.piwheels.org/project/future)** (742,655)
6.  **[youtube-dl](https://www.piwheels.org/project/youtube-dl)** (664,821)
7.  **[pyngrok](https://www.piwheels.org/project/pyngrok)** (645,709)
8.  **[speedtest-cli](https://www.piwheels.org/project/speedtest-cli)** (399,889)
9.  **[six](https://www.piwheels.org/project/six)** (379,356)
10. **[requests](https://www.piwheels.org/project/requests)** (377,486)

The top 10 project page hits were:

1.  **[lilurl](https://www.piwheels.org/project/lilurl)** (2,401)
2.  **[numpy](https://www.piwheels.org/project/numpy)** (1,354)
3.  **[opencv-python](https://www.piwheels.org/project/opencv-python)** (1,102)
4.  **[opencv-contrib-python](https://www.piwheels.org/project/opencv-contrib-python)** (1,044)
5.  **[scipy](https://www.piwheels.org/project/scipy)** (1,006)
6.  **[scikit-image](https://www.piwheels.org/project/scikit-image)** (653)
7.  **[tensorflow](https://www.piwheels.org/project/tensorflow)** (559)
8.  **[imagecodecs](https://www.piwheels.org/project/imagecodecs)** (523)
9.  **[cryptography](https://www.piwheels.org/project/cryptography)** (474)
10. **[pandas](https://www.piwheels.org/project/pandas)** (437)

The top 10 project JSON downloads were:

1.  **[awscrt](https://www.piwheels.org/project/awscrt)** (20,679)
2.  **[numpy](https://www.piwheels.org/project/numpy)** (458)
3.  **[opencv-contrib-python](https://www.piwheels.org/project/opencv-contrib-python)** (107)
4.  **[v2ray-runtime-windows](https://www.piwheels.org/project/v2ray-runtime-windows)** (104)
5.  **[requests-toolkit](https://www.piwheels.org/project/requests-toolkit)** (103)
6.  **[github-http-api](https://www.piwheels.org/project/github-http-api)** (96)
7.  **[bevy-events](https://www.piwheels.org/project/bevy-events)** (95)
8.  **[newrelic-plugins-agent](https://www.piwheels.org/project/newrelic-plugins-agent)** (95)
9.  **[v2ray-runtime](https://www.piwheels.org/project/v2ray-runtime)** (92)
10. **[protobuf](https://www.piwheels.org/project/protobuf)** (91)

See the [JSON API](https://www.piwheels.org/json.html) page for more information on using this API.

## Platforms

Linux makes up over 99.9% of all searches so I've discounted the rest. Raspberry Pi OS and Debian
are now combined (due to Raspberry Pi OS identifying itself as Debian). This group obviously
dominates with over 99%. Ubuntu remains in third place with only 0.6%, although we don't officially
support it.

<figure class="aligncenter size-full">
<img src="images/distro-usage-2.png" />
</figure>

Buster accounts for 93% of PiOS/Debian usage and Stretch accounts for just 7%:

<figure class="aligncenter size-full">
<img src="images/debian-usage-2.png" />
</figure>

armv7l (Pi 2/3/4 platform) is still a majority architecture with 93% of searches from Arm devices
(76% of which is from armv7l). We now get more hits from aarch64 users than x86_64 and armv6l
combined. It seems usage of the 64-bit OS image is on the rise (now 20% of Arm usage), although we
do not as yet provide aarch64 wheels.

<figure class="aligncenter size-full">
<img src="images/arch-1.png" />
</figure>

Python 3 has a supermajority of usage, and 3.7 (the version provided by the current stable distro)
has the highest share with 69%. Python 2.7 comes second with 15%, followed by 3.8 and 3.9. Generally
most users are using the Python provided by the current Debian stable — which was due to change
this summer, so we'll start to see a rise in Python 3.9 usage as soon as Raspberry Pi OS Bullseye
is released for which could become the leader by the end of the year.

<figure class="aligncenter size-full">
<img src="images/py-vers-1.png" />
</figure>

We're also logging pip and setuptools versions:

<figure class="aligncenter size-full">
<img src="images/pip-vers-1.png" />
</figure>

Note that 18.1 is pre-installed in Buster, and 9.0.1 is pre-installed in Stretch. 20.1.1 is a
recently released version, so likely the most common for people who update their pip.

<figure class="aligncenter size-full">
<img src="images/setuptools-vers-1.png" />
</figure>

Similarly, setuptools 40.8.0 is what's pre-installed in Buster, but the version of pip in Stretch
doesn't send the setuptools version (33.1.1) in the user agent like it does in newer versions.

We see about **4TB** of bandwidth each month, peaking at **4.2TB** in April. The breakdown of
bandwidth in the period is 76% pip downloads, 3% pip searches, a tiny amount (0.13%) of website
traffic (project pages, JSON, etc) and the rest (surprisingly high, 20%) comprising mostly of wheel
downloads from browsers (not pip):

<figure class="wp-block-image size-full">
<img src="images/bandwidth-1.png" />
</figure>

And broken down by month:

<figure class="wp-block-image size-full">
<img src="images/bandwidth-by-month-2.png" />
</figure>

Check out the source of this post in a Jupyter notebook:
[github.com/piwheels/stats/blob/master/2021q3.ipynb](https://github.com/piwheels/stats/blob/master/2021q3.ipynb)
