# Testat: Tablet

## Overview

This folder contains examples on how to deal with the Tablet on the Softbank Pepper.

### Manipulating the tablet using Choreographe

Using the tablet using Choreographe is pretty simple.
All you have to do is create a html folder and put everything you want on your website in it.
Then add a "Multimedia/Tablet/Show App" action which runs your website.

### Manipulating the tablet using python

The tablet can be controlled with Python with the ALTabletService.
The problem however is that you need to upload your behavior containing your website first.
To do that you can either create a Behavior in Choreographe and load/run the behavior and then
load the latest loaded behavior in the ALTabletService. Or you can copy your website directly onto
the robot using scp. All apps are stored in `/opt/aldebaran/www/apps`. Simply copy your behavior containing
your website with this command:

`scp -r local_folder nao@192.168.1.103:/opt/aldebaran/www/apps/app_name`

The password can be obtained from the lecture notes on ILIAS.
