
<p>Following a substantial record breaking spike in downloads, we recently passed the <strong>100,000,000</strong> mark. That's the total number of wheel files served from piwheels to date.</p>
<figure class="wp-block-embed is-type-rich is-provider-twitter wp-block-embed-twitter"><div class="wp-block-embed__wrapper">
<blockquote class="twitter-tweet" data-dnt="true" data-width="500"><p dir="ltr" lang="en">Now passed 100,000,000 downloads</p>— piwheels.org (@piwheels) <a href="https://twitter.com/piwheels/status/1571839180380020738?ref_src=twsrc%5Etfw">September 19, 2022</a></blockquote><script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>
</div></figure>
<p>When we reached 10 million in 3 years, reaching 100 million seemed impossible, but downloads significantly increased year-on-year, so here we are:</p>
<div class="wp-block-image">
<figure class="aligncenter size-full"><img sizes="auto, (max-width: 640px) 100vw, 640px" src="images/downloads-per-year.png"/></figure></div>
<h2 class="wp-block-heading">The daily record</h2>
<p>Also, the daily record keeps getting beaten. Last month, the previous record of 314,030 was smashed when we passed 500,000 for the first time. Since then, that record has been doubled — we've now passed 1,000,000.</p>
<figure class="wp-block-embed is-type-rich is-provider-twitter wp-block-embed-twitter"><div class="wp-block-embed__wrapper">
<blockquote class="twitter-tweet" data-dnt="true" data-width="500"><p dir="ltr" lang="en">Yesterday, 1,060,767 packages were downloaded from <a href="https://t.co/cXm1GPsEZt">https://t.co/cXm1GPsEZt</a> (a new daily record), saving users over 344 days of build time <a href="https://t.co/7SszRFiM3b">pic.twitter.com/7SszRFiM3b</a></p>— piwheels.org (@piwheels) <a href="https://twitter.com/piwheels/status/1577224587934195712?ref_src=twsrc%5Etfw">October 4, 2022</a></blockquote><script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>
</div></figure>
<div class="wp-block-image">
<figure class="aligncenter size-full"><img sizes="auto, (max-width: 640px) 100vw, 640px" src="images/top-daily-downloads-per-year.png"/></figure></div>
<h2 class="wp-block-heading">Raspberry Pi web hosting: does it scale?</h2>
<p>The <a href="https://piwheels.org/">piwheels website</a> is hosted on a single Raspberry Pi 4 with 4GB RAM. It's in the <a href="https://www.mythic-beasts.com/order/rpi">Mythic Beasts Pi Cloud</a>, where the Pis are netbooted from a hard disk drive, so the filesystem is over NFS.</p>
<p>It runs the piwheels master software, which controls what the other Pis build, manages file transfers and more. I'd describe that as quite a complex system (feel free to inspect it yourself on <a href="https://github.com/piwheels/piwheels/tree/master/piwheels">GitHub</a>), but the "website" part of it is as simple as possible — which is why it scales to demand so well.</p>
<p>Rather than running a web application to serve dynamic content for each request, we have the piwheels system write out the HTML indexes according to <a href="https://peps.python.org/pep-0503/">PEP 503 – Simple Repository API</a>.</p>
<p>As long as the Pi has power, network connectivity and can handle the load, the piwheels repository remains accessible. If the piwheels master software falls over for whatever reason, the website carries on serving files as before.</p>
<p>It'll be interesting to see how long the current trend pans out, and we'll see if we can figure out what's driving it. If the annual growth keeps on, maybe we'll hit the one billion mark some day…</p>
