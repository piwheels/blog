
<p>When piwheels first launched in 2017, we used the default domain provided by Mythic Beasts' Pi cloud: <code>piwheels.hostedpi.com</code>, however, we quickly acquired the domain <code>piwheels.org</code> and this became the canonical URL.</p>
<p>As of 2020-05-05 the <code>piwheels.hostedpi.com</code> domain is no longer in service. Please update your configuration to point at <code>piwheels.org</code>, specifically:</p>
<pre class="wp-block-preformatted">[global]
extra-index-url=https://www.piwheels.org/simple</pre>
<p><a href="https://github.com/piwheels/packages/issues/112">https://github.com/piwheels/packages/issues/112</a></p>
