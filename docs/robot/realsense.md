---
layout: default
title: Intel RealSense
permalink: /robot/realsense
parent: Robot Systems
nav_order: 2
font_awesome: "fas fa-video"
---

# <i class="{{ page.font_awesome }}"></i> Using an Intel RealSense


## Install all the drivers
[librealsense](https://github.com/IntelRealSense/librealsense/){: .btn .btn-primary}
[Install on Linux](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md){: .btn}

[RealSense ROS Drivers](https://github.com/IntelRealSense/realsense-ros){: .btn .btn-primary}


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

[DOPE Base Drivers](https://github.com/NVlabs/Deep_Object_Pose){: .btn .btn-primary}
[Based on this paper](https://arxiv.org/abs/1809.10790){: .btn}

Someone has tried this to include the depth data too: [DOPE RealSense Drivers](https://github.com/yehengchen/DOPE-ROS-D435)

Also: There are several dependencies I had to manually install since I'm using ROS Melodic (both of these packages are built for Kinetic)

### Actually using the dope package
1. Edit the `dope/config/config_pose.yaml`

```yaml	
topic_camera: "/camera/color/image_raw"
topic_camera_info: "/camera/color/camera_info"
```

2. `roslaunch dope dope.launch`