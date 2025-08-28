Until now, piwheels has served its simple index, [project
pages](https://blog.piwheels.org/requires-python-support-new-project-page-layout-and-a-new-json-api/),
wheel files and even [build log entries](https://blog.piwheels.org/view-piwheels-build-output/) from
a single server — a Raspberry Pi, of course. As our index has grown over the years, the amount of
disk space we've needed to host all those files has grown — we currently have a 5TB SSD storage
allocation attached to the Pi running the piwheels master service — provided at no cost by our
wonderful hosts [Mythic Beasts](https://www.mythic-beasts.com/). The growth of our disk space
requirements is unsustainable, and so it makes sense at this point to move *some* of our storage to
cheaper HDD storage, freeing up SSD storage for Mythic's other [Pi
cloud](https://www.mythic-beasts.com/order/rpi) customers.

Our file structure follows the [Simple repository API
specification](https://packaging.python.org/en/latest/specifications/simple-repository-api/) in the
most straightforward way. We have directories for each package, containing an index.html file
containing a list of links to files for that package. That's all that's required for pip to work.
In our case, the files are stored within that same directory, e.g. `/simple/gpiozero/index.html` and
`/simple/gpiozero/gpiozero-2.0.1-py3-none-any.whl`.

I think PyPI probably used to be laid out this way, but at some point they moved their files to a
CDN. All this requires is changing the URL of the file as its listed in the simple HTML index to an
absolute URL to the new location of the file. That's what we're doing to a subset of the files on
piwheels — we're moving them to a separate server backed by HDD storage, and updating the links
accordingly.

Since piwheels aims to build 100% of all package versions for the sake of completion, we end up
hosting files that won't be downloaded regularly, or ever at all. For example: obsolete packages,
packages intended for Windows users only, old versions of packages, and so on. Since we keep track
of the number of downloads each file has had, we're able to use this logic to partition the files
according to popularity. Any files which haven't been downloaded recently can be moved to the
archive server.

Take the package **[gpiozero](https://www.piwheels.org/project/gpiozero/)**, for example: only five
of the files we host for this package have been downloaded recently, so we moved the rest to the
archive server. The file for gpiozero 2.0 still lives on the main server and so has the URL
`https://www.piwheels.org/simple/gpiozero/gpiozero-2.0.1-py3-none-any.whl` whereas the less popular
first release `0.1.0` was moved to our archive server so it's now at
`https://archive1.piwheels.org/simple/gpiozero/gpiozero-0.1.0-py2.py3-none-any.whl`.

Users using **pip** to install packages will not need to change anything, even if installing files
we've moved to the archive server. The only users requiring a change in behaviour are those who are
manually downloading or installing files using a specific URL. It would be best to use pip to
resolve the URL for your files, or download the package's simple index HTML file (e.g.
<https://www.piwheels.org/simple/gpiozero/>) and extract the URL from there.
