*The title is a reference to the mostly forgotten nickname of the excellent [Python Package
Index](https://pypi.org/) —* *Cheese Shop — which refers to the Monty Python [Cheese Shop
sketch](https://www.youtube.com/watch?v=Hz1JWzyvv8A).*

I often find myself staring at the piwheels monitor, and occasionally a strange package name or an
unusually longer version number pops up:

<figure class="aligncenter size-large">
<img src="images/Screenshot-from-2021-07-28-21-36-08-904x1024.png" />
</figure>

I've been doing a lot of auditing piwheels vs PyPI lately, making sure we have the right set of
packages and versions, pruning stuff that should have been deleted and adding in any that somehow
got missed. And I came across lots of interesting oddities, so I thought I'd do some analysis and
exploration and share the results here.

The following analysis is of a set of packages and version obtained from PyPI a few days ago, and at
the time there were:

- **311,063 packages**
- **2,766,603 versions**

## Longest package names

The most common length of package name is **8** characters (like
[**gpiozero**](https://pypi.org/project/gpiozero/)):

<figure class="aligncenter size-full">
<img src="images/package_name_len_bar.png" />
</figure>

The least common package name lengths are **72**, **73**, **74**, **75**, **80**, **82**, **83**,
**90**, **92** — all of which occur once.

The longest package names are:

- [**testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest**](https://pypi.org/project/testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest/)
    (92)
- [**wix-protos-com-wix-ecom-shipments-localdelivery-wix-ecommerce-shipments-local-delivery-web**](https://pypi.org/project/wix-protos-com.wix.ecom.shipments.localdelivery-wix-ecommerce-shipments-local-delivery-web/)
    (90)
- [**wix-protos-multilingual-localizationimporterexporter-localization-importer-exporter**](https://pypi.org/project/wix-protos-multilingual-localizationimporterexporter-localization-importer-exporter/)
    (83)
- [**wix-protos-ecom-shipments-localdelivery-wix-ecommerce-shipments-local-delivery-web**](https://pypi.org/project/wix-protos-ecom-shipments-localdelivery-wix-ecommerce-shipments-local-delivery-web/)
    (82)

<figure class="aligncenter size-full">
<img src="images/package_name_len_pie.png" />
</figure>

<figure class="aligncenter size-large">
<img src="images/test.png" />
</figure>

## Starting characters

The most common starting character for a package name is **p** (14%), due to lots of packages being
named "py"-something or "python"-something. Second is **d** (9%) due to "django-" packages.
The distribution for the rest of the character set is:

<figure class="aligncenter size-full">
<img src="images/pkg_first_letter_pie.png" />
</figure>

The least common starting character is **9**. Only five packages start with a 9:

- **[91act-platform](https://pypi.org/project/91act-platform)**
- **[99d4aa80-d846-424f-873b-a02c7215fc54](https://pypi.org/project/99d4aa80-d846-424f-873b-a02c7215fc54)**
- **[908dist](https://pypi.org/project/908dist)**
- **[91downloader](https://pypi.org/project/91downloader)**
- **[9](https://pypi.org/project/9)**

Looking at the first two characters, the most common are **py**, **dj**, **od**, **co** and **re**:

<figure class="aligncenter size-full">
<img src="images/pkg_first_two_letters_bar-1.png" />
</figure>

Looking at the first three characters, **dja** takes over **py**:

<figure class="aligncenter size-full">
<img src="images/pkg_first_three_letters_bar.png" />
</figure>

## Benford's Law

[Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law) states that in many naturally
occurring collections of numbers, the leading digit is likely to be small, and hence the
distribution of each subsequent digit is less likely. I wondered if this could be seen within
package version numbers. Taking the numeric versions, and looking at the first non-zero digit, the
distribution is reasonably compliant with Benford's Law:

<figure class="aligncenter size-full">
<img src="images/bar_with_benford_fd.png" />
</figure>

However, looking at the distribution of all digits (not just the first), this follows the pattern
laid out by Benford's Law much more closely:

<figure class="aligncenter size-full">
<img src="images/bar_with_benford.png" />
</figure>

In both cases, 1 is more common that expected, 2 seems to be perfectly aligned, but 9 is slightly
more common than expected, more so in the first digit example.

## Number of versions per package

I excluded packages which had no versions (because they don't have JSON endpoints on PyPI). As for
the rest of them, over a quarter only have a single version. The frequency drops steadily as the
number of versions rises:

<figure class="aligncenter size-full">
<img src="images/vers_per_package.png" />
</figure>

The package with the most versions is **[pulumi](https://pypi.org/project/pulumi/)** with **2,566**
versions!

## Version length

A PyPI package version doesn't have to be strictly numeric — they're usually in the form 1.2.3 or
similar, sometimes with characters appended to indicate alpha, beta, dev or release candidate, but
they can be *any* string.

- The most common version length is **5**, which matches the "**1.2.3**" format.
- The single most common version is "**0.1.0**" which occurs **57,258** times
- There are **233,734** distinct versions
- The longest version is a version of package
    [**lyricsprocessor**](https://pypi.org/project/lyricsprocessor), with the version number
    [**0.1.40404040404040404040404040404040404040404040404040404040404040404040404040404040**](https://pypi.org/project/lyricsprocessor/0.1.40404040404040404040404040404040404040404040404040404040404040404040404040404040/)
    (84 chars)
- The next longest are all from package
    [**softwarefabrica-django-utils**](https://pypi.org/project/softwarefabrica.django.utils/) which
    exclusively has versions of 70 characters e.g.
    [**1.0dev-BZR-r115-panta-elasticworld.org-20100520155735-sf3yrsr0pvyvlm8m**](https://pypi.org/project/softwarefabrica.django.utils/1.0dev-BZR-r115-panta-elasticworld.org-20100520155735-sf3yrsr0pvyvlm8m/)

<figure class="aligncenter size-full">
<img src="images/ver_lens.png" />
</figure>

<figure class="aligncenter size-large">
<img src="images/Screenshot-from-2021-08-01-15-54-23-1024x275.png" />
</figure>

At one point in PyPI's history, someone accidentally submitted the description of their package as
the version name, so there was a version of package
**[sysv-ipc](https://pypi.org/project/sysv-ipc/)** called:

```
Sysv_ipc gives Python programs access to System V semaphores, shared memory and message queues. Most (all?) Unixes (including OS X) support System V IPC. Windows+Cygwin 1.7 might also work. 

Sample code is included.

This extension is released under the GPL. 

You might also be interested in the similar POSIX IPC module at: http://semanchuk.com/philip/posix_ipc/
```

Yes, that entire block of text. The version has now been deleted.

<figure class="aligncenter size-large">
<img src="images/photo6021784590307407545-1-1024x486.jpg" />
<figcaption>The truncated version number appearing on piwheels, prior to its deletion</figcaption>
</figure>

Other times this kind of thing has happened by accident include the first version of
**[omnijson](https://pypi.org/project/omnijson/)** which was called "**[Kenneth
Reitz](https://pypi.org/project/omnijson/Kenneth%20Reitz/)**" and is still live:

<figure class="aligncenter size-full">
<img src="images/photo6048744782924200107.jpg" />
</figure>

## Whitespace significance?

I recently noticed a version which seemed to have whitespace at the end of it, and had a look to see
if there were others. There are 16 versions on PyPI which end in a newline character. Of these 16,
12 have registered the stripped equivalent too:

- **bugzilla** '1.0\\n'
- **bugzilla** '1.0.0\\n'
- **django-filtered-form** '1.0.1\\n'
- **django-mongokit** '0.2.3\\n'
- **docbook** '1.0.11\\n'
- **git-plus** '0.2.1.beta\\n'
- **lcinvestor** '2.2.1\\n'
- **lendingclub** '0.1.7\\n'
- **pythonwpy** '0.3.0\\n'
- **pythonwpy** '0.3.3\\n'
- **rabbit-qurator** 'v1.0.0\\n'
- **rtmidi2** '0.5.2\\n'

Visually, on PyPI, these look identical:

<figure class="aligncenter size-full">
<img src="images/Screenshot-from-2021-08-01-16-49-49.png" />
<figcaption><a href="https://pypi.org/project/bugzilla/#history">Bugzilla</a> v1 – but which
one??</figcaption>
</figure>

## Non-numeric version names

Since version numbers tend to be numeric, surely the most interesting ones are those without any
numbers in them.

- There are **166** packages which have non-numeric versions
- There are a total of **171** non-numeric versions
- The longest non-numeric version is [**jw-util**](https://pypi.org/project/jw.util/) version
    "**[-class.-jw.util.version.Version-](https://pypi.org/project/jw.util/-class.-jw.util.version.Version-/)**"

This version number of **jw-util** seems to have been another accident:

<figure class="aligncenter size-full">
<img src="images/Screenshot-from-2021-08-01-16-04-29.png" />
</figure>

Since the version included a tarball in its
[release](https://pypi.org/project/jw.util/-class.-jw.util.version.Version-/#files), you can inspect
how this accident occurred. Lots of complicated code for calculating what the version number should
be ... gone wrong. The version string is actually the
[repr](https://docs.python.org/3/library/functions.html#repr) of the Version class, not the string
representation of the instance, as intended. Normally it would appear as
`<__class__.jw.util.version.Version>` but it's been canonicalised, replacing the angle brackets and
double underscores with single hyphens.

Interestingly (if you've made it this far, I think you're the kind of person who'll find this
interesting), of the 166 packages with non-numeric versions, all but five of them have only a single
non-numeric version, and those five only have two such versions each. Those are:

- [**confine-controller**](https://pypi.org/project/confine-controller) 'dev' and 'beta'
- [**pycli**](https://pypi.org/project/pycli) 'devel' and 'dev'
- [**pyircserver**](https://pypi.org/project/pyircserver) 'PreAlpha' and 'Alpha'
- **[amoi](https://pypi.org/project/amoi)** 'lol' and '.lol.'
- **[dstufft-testpkg](https://pypi.org/project/dstufft-testpkg)** 'dog' and 'watwatwat'

## Queen's English

Using the system dictionaries, I wondered how many package names were dictionary words:

- **11,131** packages are a single word found in the US English dictionary
- **11,031** packages are are a single word found in the British English dictionary
- Only **39** of the British English dictionary packages do not appear in the US dictionary, so
    for fun, let's see what those are:
    - **[acclimatise](https://pypi.org/project/acclimatise)**
    - **[aluminium](https://pypi.org/project/aluminium)**
    - **[analyse](https://pypi.org/project/analyse)**
    - **[armoury](https://pypi.org/project/armoury)**
    - **[behaviour](https://pypi.org/project/behaviour)**
    - **[caesium](https://pypi.org/project/caesium)**
    - **[colour](https://pypi.org/project/colour)**
    - **[colouration](https://pypi.org/project/colouration)**
    - **[coloured](https://pypi.org/project/coloured)**
    - **[colourful](https://pypi.org/project/colourful)**
    - **[colourless](https://pypi.org/project/colourless)**
    - **[colours](https://pypi.org/project/colours)**
    - **[connexion](https://pypi.org/project/connexion)**
    - **[decentralise](https://pypi.org/project/decentralise)**
    - **[draughts](https://pypi.org/project/draughts)**
    - **[draughtsman](https://pypi.org/project/draughtsman)**
    - **[fibre](https://pypi.org/project/fibre)**
    - **[gramme](https://pypi.org/project/gramme)**
    - **[harbour](https://pypi.org/project/harbour)**
    - **[inflexion](https://pypi.org/project/inflexion)**
    - **[labours](https://pypi.org/project/labours)**
    - **[liquorice](https://pypi.org/project/liquorice)**
    - **[memorised](https://pypi.org/project/memorised)**
    - **[mitre](https://pypi.org/project/mitre)**
    - **[motorise](https://pypi.org/project/motorise)**
    - **[mould](https://pypi.org/project/mould)**
    - **[moult](https://pypi.org/project/moult)**
    - **[mums](https://pypi.org/project/mums)**
    - **[normalise](https://pypi.org/project/normalise)**
    - **[optimisation](https://pypi.org/project/optimisation)**
    - **[optimise](https://pypi.org/project/optimise)**
    - **[optimiser](https://pypi.org/project/optimiser)**
    - **[organise](https://pypi.org/project/organise)**
    - **[pyjamas](https://pypi.org/project/pyjamas)**
    - **[sceptre](https://pypi.org/project/sceptre)**
    - **[spectre](https://pypi.org/project/spectre)**
    - **[spectres](https://pypi.org/project/spectres)**
    - **[summarise](https://pypi.org/project/summarise)**
    - **[tricolour](https://pypi.org/project/tricolour)**

You can view the notebook to see the workings around this analysis on
[**GitHub**](https://github.com/piwheels/stats/blob/master/pypi.ipynb), including how I obtained the
data from PyPI using the XMLRPC and JSON APIs.
