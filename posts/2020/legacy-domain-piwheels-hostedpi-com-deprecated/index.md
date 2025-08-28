When piwheels first launched in 2017, we used the default domain provided by Mythic Beasts' Pi
cloud: `piwheels.hostedpi.com`, however, we quickly acquired the domain `piwheels.org` and this
became the canonical URL.

As of 2020-05-05 the `piwheels.hostedpi.com` domain is no longer in service. Please update your
configuration to point at `piwheels.org`, specifically:

```
[global]
extra-index-url=https://www.piwheels.org/simple
```

<a href="https://github.com/piwheels/packages/issues/112">https://github.com/piwheels/packages/issues/112</a>
