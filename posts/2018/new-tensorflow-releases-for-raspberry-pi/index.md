<p>Last month, the Tensorflow team at Google <a href="https://medium.com/tensorflow/tensorflow-1-9-officially-supports-the-raspberry-pi-b91669b0aa0">announced official support</a> for Raspberry Pi, by releasing pre-build binaries of v1.9.0 to piwheels.org. Since then, two new releases (<strong>v1.10.1</strong> and <strong>v1.11.0</strong>) have been made and they are now available on piwheels.org.</p>
<p>To install the latest Tensorflow on Raspbian Stretch, first install libatlas, which is a depencency for the optimised version of numpy on piwheels, the  simply use pip to install tensorflow:</p>
<pre>sudo apt install libatlas3-base
sudo pip3 install tensorflow</pre>
<p>If you're using Tensorflow in your Pi project, be sure to let us know by tweeting at <a href="https://twitter.com/piwheels">@piwheels</a>.</p>
