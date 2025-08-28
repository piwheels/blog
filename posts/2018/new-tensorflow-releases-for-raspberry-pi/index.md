Last month, the Tensorflow team at Google [announced official
support](https://medium.com/tensorflow/tensorflow-1-9-officially-supports-the-raspberry-pi-b91669b0aa0)
for Raspberry Pi, by releasing pre-build binaries of v1.9.0 to piwheels.org. Since then, two new
releases (**v1.10.1** and **v1.11.0**) have been made and they are now available on piwheels.org.

To install the latest Tensorflow on Raspbian Stretch, first install libatlas, which is a depencency
for the optimised version of numpy on piwheels, the  simply use pip to install tensorflow:

```
sudo apt install libatlas3-base
sudo pip3 install tensorflow
```

If you're using Tensorflow in your Pi project, be sure to let us know by tweeting at
[@piwheels](https://twitter.com/piwheels).
