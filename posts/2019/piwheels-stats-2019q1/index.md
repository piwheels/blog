piwheels had a great start to 2019, with our biggest month in terms of downloads in January, and
biggest month in terms of time saved in February! Headline stats for the quarter:

- Downloads: **2,176,652**
- Build time saved: **25 years 7 months 23 days**

This brings our totals so far to:

- Downloads: **7,703,358**
- Build time saved: **67 years 2 months 3 days**

The number of downloads in this period is *more than double* the same period in 2018.

<figure class="wp-block-image">
<img src="images/Downloads.png" />
</figure>

There was a record breaking number of downloads in the month of January:

- January: **793,294**
- February: **700,246**
- March: **683,112**

<figure class="wp-block-image">
<img src="images/Downloads-by-month.png" />
</figure>

However, February saved users the most time:

- January: **8 years 6 months**
- February: **9 years 1 month**
- March: **8 years**

<figure class="wp-block-image">
<img src="images/Time-saved-in-years-by-month.png" />
</figure>

## Project pages

We also recently deployed new project pages so users have a nicer interface when browsing
information about which packages and versions we have:

<figure class="wp-block-image">
<a href="https://www.piwheels.org/project/pycparser/"><img src="images/piwheels-project-page.png" /></a>
</figure>

## Popular packages

The top 30 most downloaded packages of the quarter:

1.  **[pycparser](https://www.piwheels.org/project/pycparser)** (73,736)
2.  **[cffi](https://www.piwheels.org/project/cffi)** (54,483)
3.  **[cryptography](https://www.piwheels.org/project/cryptography)** (52,436)
4.  **[PyYAML](https://www.piwheels.org/project/PyYAML)** (50,047)
5.  **[numpy](https://www.piwheels.org/project/numpy)** (49,988)
6.  **[MarkupSafe](https://www.piwheels.org/project/MarkupSafe)** (47,950)
7.  **[aiohttp](https://www.piwheels.org/project/aiohttp)** (47,875)
8.  **[ruamel.yaml](https://www.piwheels.org/project/ruamel.yaml)** (45,296)
9.  **[bcrypt](https://www.piwheels.org/project/bcrypt)** (45,248)
10. **[SQLAlchemy](https://www.piwheels.org/project/SQLAlchemy)** (42,998)
11. **[future](https://www.piwheels.org/project/future)** (41,061)
12. **[multidict](https://www.piwheels.org/project/multidict)** (34,581)
13. **[yarl](https://www.piwheels.org/project/yarl)** (34,163)
14. **[home-assistant-frontend](https://www.piwheels.org/project/home-assistant-frontend)** (34,057)
15. **[voluptuous-serialize](https://www.piwheels.org/project/voluptuous-serialize)** (33,573)
16. **[idna_ssl](https://www.piwheels.org/project/idna_ssl)** (33,110)
17. **[python-slugify](https://www.piwheels.org/project/python-slugify)** (33,047)
18. **[paho-mqtt](https://www.piwheels.org/project/paho-mqtt)** (31,360)
19. **[mutagen](https://www.piwheels.org/project/mutagen)** (29,544)
20. **[ifaddr](https://www.piwheels.org/project/ifaddr)** (28,433)
21. **[gTTS-token](https://www.piwheels.org/project/gTTS-token)** (26,500)
22. **[pycryptodome](https://www.piwheels.org/project/pycryptodome)** (24,949)
23. **[RPi.GPIO](https://www.piwheels.org/project/RPi.GPIO)** (24,513)
24. **[opencv-python](https://www.piwheels.org/project/opencv-python)** (24,032)
25. **[PyQRCode](https://www.piwheels.org/project/PyQRCode)** (23,259)
26. **[Pillow](https://www.piwheels.org/project/Pillow)** (21,652)
27. **[user-agents](https://www.piwheels.org/project/user-agents)** (21,486)
28. **[Adafruit-PureIO](https://www.piwheels.org/project/Adafruit-PureIO)** (20,759)
29. **[docopt](https://www.piwheels.org/project/docopt)** (20,385)
30. **[kiwisolver](https://www.piwheels.org/project/kiwisolver)** (18,443)

## Environmental stats

Armv7 is still by far our most used architecture, getting almost 88% versus less than 9% for Armv6.
Remember, Armv7 means Pi 2, 3, and 3+; and Armv6 means Pi 1 and Pi Zero. There's still a small (3%)
record of x86_64 downloads, and a trace of a few others. But since we only provide Arm platform
wheels (not x86 ones), the only x86 (& etc) downloads recorded are pure Python wheels only.

<figure class="wp-block-image">
<img src="images/Downloads-by-architecture.png" />
</figure>

Raspbian users make up over 95% of our downloads, followed by a 3.7% Debian base, and a tiny slither
of Ubuntu users and so on. It's notable that until recently, Ubuntu MATE only had 16.04 images. Now
they're shipping 18.04 images, but neither of these ship with piwheels pre-configured. Also
Canonical have started work on officially supporting Ubuntu Desktop and Server for the Pi, so I'm
sure we'll see a rise in usage in 2019.

<figure class="wp-block-image">
<img src="images/Downloads-by-OS.png" />
</figure>

Similarly, Raspbian Stretch has a 95% share of downloads, followed by Debian Stretch (3.5%) and
Ubuntu 18.04 (<1%). Unsurprising as Raspbian is so popular and the only OS pre-configured to use
piwheels. Jessie had very few downloads, and Buster (testing) had almost as many. We do actually
have Python 3.4 wheels, but Jessie is not configured to use piwheels. We don't get have Python 3.7
wheels for Buster, but we will by the time it's released.

<figure class="wp-block-image">
<img src="images/Downloads-by-distro-version.png" />
</figure>

Again, unexpectedly, the Python 3 version found in Raspbian Stretch (3.5) sticks out with over 90%
of the share. There's a small but significant presence of Python 2, and this is only the pure
Python pakcages that explicitly state in their setup that they are universal (compatible with 2 and
3), but don't release wheels on PyPI. It's a small proportion of packages, but includes the most
popular package of all, [pycparser](https://www.piwheels.org/project/pycparser/).

I see a lot of Stack Exchange and forum questions from people installing out-of-distribution
versions of Python on their Pis (particularly when following guides that say they require Python 3.6
or 3.7). I don't see a lot of success in this, and generally advise people to stick with the
distribution, or try upgrading to Buster. But it seems we have a 1.4% hit for Python 3.6 despite not
providing wheels for it. These could be Ubuntu 18.04 users, or Raspbian users who have built Python
3.6 themselves.

<figure class="wp-block-image">
<img src="images/Downloads-by-Python-version.png" />
</figure>

## What next?

Since deploying the new project pages and some other updates, we had some issues with communication
across Pis, and we've halted building for the time being. Dave's working on a new C-based
implementation of [CBOR](https://cbor.io/) (called [cboar](https://github.com/waveform80/cboar))
which we think will resolve these issues, and we expect to be building again very soon. This means
we'll catch up with any recent releases, and we'll be able to start building Python 3.7 wheels in
time for Buster's release. We have also deployed dependency calculation to solve the [missing
shared object
problem](https://blog.piwheels.org/how-to-work-out-the-missing-dependencies-for-a-python-package/),
so now when wheels are built, their apt dependencies will be calculated. We'll need to do this for
all existing wheels too.

Debian and Raspbian Buster are expected around June, possibly, so we'll be in a position where both
stable (Buster) and oldstable (Stretch) provide configuration for piwheels, and I have a strong
suspicion that a more stable Ubuntu 18.04 or later might also pre-configure for piwheels too. This
will show a much more varied and informative view of which distributions and Python versions are
being used. I imagine Q2 will be similar to Q1 but Q3 and Q4 will be more interesting.

For regular updates, follow [@piwheels](https://twitter.com/piwheels) on Twitter!
