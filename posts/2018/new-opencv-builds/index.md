<p>The opencv maintainers don't release source distribution for the packages, so <a href="https://www.twitter.com/waveform80">Dave</a> has been building Raspberry Pi wheels manually from source on <a href="https://github.com/skvark/opencv-python">GitHub</a>. They have also chosen to split releases into four separate pacakges:</p>
<ul>
<li><a href="https://pypi.org/project/opencv-python">opencv-python</a></li>
<li><a href="https://pypi.org/project/opencv-python-headless">opencv-python-headless</a></li>
<li><a href="https://pypi.org/project/opencv-contrib-python">opencv-contrib-python</a></li>
<li><a href="https://pypi.org/project/opencv-contrib-python-headless">opencv-contrib-python-headless</a></li>
</ul>
<p><code>opencv-contrib</code> includes all of opencv, plus additional modules (listed in the <a href="https://docs.opencv.org/master/">opencv docs</a>). The <code>-headless</code> releases exclude any GUI functionality, which mean they require fewer dependencies, and are ideal if you're using Raspbian Lite or simply not using any GUI features.</p>
<p>We now have Raspberry Pi wheels for versions<strong> 3.4.2.16,</strong> <strong>3.4.2.17</strong> and <strong>3.4.3.18</strong> of all four package variations on piwheels.org.</p>
<h2>Dependencies</h2>
<p>When you pip install an opencv package, you'll need various apt packages installed to provide make it work. We're planning to document this on piwheels.org for each package in future but for now, here are the full installation instructions for opencv:</p>
<h3>opencv-python</h3>
<pre>sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-python</pre>
<h3>opencv-python-headless</h3>
<pre>sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0
sudo pip3 install opencv-python-headless</pre>
<h3>opencv-contrib-python</h3>
<pre>sudo apt install libatlas3-base libsz2 libharfbuzz0b libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-contrib-python libwebp6</pre>
<h3>opencv-contrib-python-headless</h3>
<pre>sudo apt install libatlas3-base libhdf5-100 libharfbuzz0b libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0
sudo pip3 install opencv-contrib-python-headless</pre>
<p> </p>
