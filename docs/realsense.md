---
layout: default
title: Intel RealSense
permalink: /realsense
nav_order: 3
font_awesome: "fas fa-video"
---

# <i class="{{ page.font_awesome }}"></i> Using an Intel RealSense


## Install all the drivers
[librealsense](https://github.com/IntelRealSense/librealsense/){: .btn}

- [Install on Linux](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)

[RealSense ROS Drivers](https://github.com/IntelRealSense/realsense-ros){: .btn}


## View realsense camera + take basic snapshots

`realsense-viewer`


## Interface with everything in ROS

These commands are from the [RealSense ROS Documentation](https://github.com/IntelRealSense/realsense-ros)

- Just launch the camera
	- `roslaunch realsense2_camera rs_camera.launch`
- View a cool point cloud
	- `roslaunch realsense2_camera rs_camera.launch filters:=pointcloud`
- Visualize in Rviz
	- `rviz`
	- View the RGB camera `Add > By topic > /camera/color/image_raw > Image`
	- View the point cloud `Add > By topic > /camera/depth/image_rect_raw > DepthCloud`


## Deep Object Pose Estimation

Download the base drivers for deep object pose estimation (trained on RGB cameras)

[DOPE Base Drivers](https://github.com/NVlabs/Deep_Object_Pose){: .btn}

Someone has tried this to include the depth data too: [DOPE RealSense Drivers](https://github.com/yehengchen/DOPE-ROS-D435)

Also: There are several dependencies I had to manually install since I'm using ROS Melodic (both of these packages are built for Kinetic)

### Actually using the dope package

`roslaunch dope dope.launch`