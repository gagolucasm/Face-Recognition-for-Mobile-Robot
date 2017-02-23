# Face Recognition for Mobile Robot

Complete code to connect with ROS an Asus Xtion Pro Live (Infrared 3D sensor camera), and use it's camera feed to identify people in real time. Includes the database generator (gdasus.py) ready to work into a Nvidia Tegra TK1.

## Installation

Clone the repository in your computer:

`git clone https://github.com/gagolucasm/Face-Recognition-for-Mobile-Robot.git`

## Dependencies

You will need:

* [Python 3.5](https://www.python.org/)
* [Opencv](http://opencv.org/)
* [Numpy](http://www.numpy.org/)
* [Rospy](http://wiki.ros.org/rospy)
* [Picamera](https://picamera.readthedocs.io/en/release-1.12/) (if you want to run it on a Raspberry Pi)

## How to use

You have to init ROS and get the camera ready:

`roscore`

`roslaunch openni2_launch openni2.launch`

To start generating the database, run:

`python gdasus.py`

When it´s ready, just run:

`python face_detect_v5.py`

## Licence

This proyect is Copyright © 2015-2017 Lucas Gago. It is free software, and may be redistributed under the terms specified in the [MIT Licence](https://opensource.org/licenses/MIT).
