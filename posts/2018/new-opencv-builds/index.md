The opencv maintainers don't release source distribution for the packages, so
[Dave](https://www.github.com/waveform80) has been building Raspberry Pi wheels manually from
source on [GitHub](https://github.com/skvark/opencv-python). They have also chosen to split releases
into four separate pacakges:

- [opencv-python](https://pypi.org/project/opencv-python)
- [opencv-python-headless](https://pypi.org/project/opencv-python-headless)
- [opencv-contrib-python](https://pypi.org/project/opencv-contrib-python)
- [opencv-contrib-python-headless](https://pypi.org/project/opencv-contrib-python-headless)

`opencv-contrib` includes all of opencv, plus additional modules (listed in the [opencv
docs](https://docs.opencv.org/master/)). The `-headless` releases exclude any GUI functionality,
which mean they require fewer dependencies, and are ideal if you're using Raspbian Lite or simply
not using any GUI features.

We now have Raspberry Pi wheels for versions** 3.4.2.16,** **3.4.2.17** and **3.4.3.18** of all four
package variations on piwheels.org.

## Dependencies

When you pip install an opencv package, you'll need various apt packages installed to provide make
it work. We're planning to document this on piwheels.org for each package in future but for now,
here are the full installation instructions for opencv:

### opencv-python

```
sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-python
```

### opencv-python-headless

```
sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0
sudo pip3 install opencv-python-headless
```

### opencv-contrib-python

```
sudo apt install libatlas3-base libsz2 libharfbuzz0b libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-contrib-python libwebp6
```

### opencv-contrib-python-headless

```
sudo apt install libatlas3-base libhdf5-100 libharfbuzz0b libwebp6 libtiff5 libjasper1 libilmbase12 libopenexr22 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0
sudo pip3 install opencv-contrib-python-headless
```
