
<p>I think this post will please a lot of people. We've just imported all the missing opencv files, including the latest 4.x releases up to <strong>v4.1.1.26</strong> for all opencv/contrib/headless variations:</p>
<ul class="wp-block-list"><li><a href="https://www.piwheels.org/project/opencv-python">opencv-python</a></li><li><a href="https://www.piwheels.org/project/opencv-python-headless">opencv-python-headless</a></li><li><a href="https://www.piwheels.org/project/opencv-contrib-python">opencv-contrib-python</a></li><li><a href="https://www.piwheels.org/project/opencv-contrib-python-headless">opencv-contrib-python-headless</a></li></ul>
<p>When you pip install an opencv package, you'll need various apt packages installed to provide make it work. These are now provided on the project pages linked above. Soon you'll be able to see the dependencies for each distro (Jessie, Stretch and Buster) but for now here are the Buster ones:</p>
<p><em>(for older distros, follow </em><a href="https://blog.piwheels.org/how-to-work-out-the-missing-dependencies-for-a-python-package/"><em>this guide</em></a><em>)</em></p>
<h3 class="wp-block-heading">opencv-python</h3>
<pre class="wp-block-preformatted">sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-python</pre>
<h3 class="wp-block-heading">opencv-python-headless</h3>
<pre class="wp-block-preformatted">sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 
sudo pip3 install opencv-python-headless</pre>
<h3 class="wp-block-heading">opencv-contrib-python</h3>
<pre class="wp-block-preformatted">sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-contrib-python</pre>
<h3 class="wp-block-heading">opencv-contrib-python-headless</h3>
<pre class="wp-block-preformatted">sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0
sudo pip3 install opencv-contrib-python-headless</pre>
<p>Huge thanks to <a href="https://twitter.com/waveform80">Dave</a> for working through all these builds.</p>
<p><em>Note: due to a missing link flag, for now you'll need to run Python with </em><code>LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3</code><em> in order to successfully </em><code>import cv2</code><em>. We'll address this in due course. Follow </em><a href="https://github.com/piwheels/packages/issues/59"><em>issue #59</em></a><em>.</em></p>
