Today, Raspberry Pi
[announced](https://www.raspberrypi.org/blog/8gb-raspberry-pi-4-on-sale-now-at-75/) the launch of a
new 64-bit version of their operating system, which is now named "Raspberry Pi OS" rather than
"Raspbian".

Currently, piwheels does not support the 64-bit image, as we do not currently build or host aarch64
wheels. However, pip will still work without users needing to change their pip config. It will
simply be a degraded service from the 32-bit image, as package installations will be slower, and
you'll need to install the appropriate dev libraries to be able to install them. Unfortunately, it
seems that forcing installations of armv7 wheels will not work.

Adding support for aarch64 will require a significant amount of work for the piwheels team, which we
intend to undertake in due course, but we cannot provide a timeline for this as we are so busy at
present. Watch this space for updates.

It will be interesting to see what the take-up of the 64-bit image will be, and how popular the
32-bit image, which works across all Pi models, will remain.
