# Face-Recognition-for-Mobile-Robot

Complete code to connect with ROS an Asus Xtion Pro Live (Infrared 3D sensor camera), and use it's camera feed to identify people in real time. Includes the database generator (gdasus.py) ready to work into a Nvidia Tegra TK1.

## How to use

You have to init ROS and get the camera ready:

`roscore`

`roslaunch openni2_launch openni2.launch`

To start generating the database, run:

`python gdasus.py`

When it´s ready, just run:

`python face_detect_v5.py`

