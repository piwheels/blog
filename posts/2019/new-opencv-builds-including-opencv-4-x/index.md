I think this post will please a lot of people. We've just imported all the missing opencv files,
including the latest 4.x releases up to **v4.1.1.26** for all opencv/contrib/headless variations:

- [opencv-python](https://www.piwheels.org/project/opencv-python)
- [opencv-python-headless](https://www.piwheels.org/project/opencv-python-headless)
- [opencv-contrib-python](https://www.piwheels.org/project/opencv-contrib-python)
- [opencv-contrib-python-headless](https://www.piwheels.org/project/opencv-contrib-python-headless)

When you pip install an opencv package, you'll need various apt packages installed to provide make
it work. These are now provided on the project pages linked above. Soon you'll be able to see the
dependencies for each distro (Jessie, Stretch and Buster) but for now here are the Buster ones:

*(for older distros, follow* [*this
guide*](https://blog.piwheels.org/how-to-work-out-the-missing-dependencies-for-a-python-package/)*)*

### opencv-python

```
sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-python
```

### opencv-python-headless

```
sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 
sudo pip3 install opencv-python-headless
```

### opencv-contrib-python

```
sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 libqtgui4 libqt4-test libqtcore4
sudo pip3 install opencv-contrib-python
```

### opencv-contrib-python-headless

```
sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0
sudo pip3 install opencv-contrib-python-headless
```

Huge thanks to [Dave](https://github.com/waveform80) for working through all these builds.

*Note: due to a missing link flag, for now you'll need to run Python with*
`LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3` *in order to successfully*
`import cv2`*. We'll address this in due course. Follow* [*issue
#59*](https://github.com/piwheels/packages/issues/59)*.*
