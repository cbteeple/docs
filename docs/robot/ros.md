---
layout: default
title: ROS
permalink: /robot/ros
parent: Robot Systems
nav_order: 1
font_awesome: "fas fa-terminal"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }


1. TOC
{:toc}

---


## Installing ROS on Linux

[Instructions on the ROS Wiki](http://wiki.ros.org/Installation/Ubuntu){: .btn .btn-primary}

For ROS Noetic on Ubuntu 20.04, follow [this tutorial](https://varhowto.com/install-ros-noetic-ubuntu-20-04/)

Important
{: .label .label-red }

Be sure to add the ROS path to your `~/.bashrc` file: `source /opt/ros/melodic/setup.bash`



## Installing ROS on Windows
There are times when you might want to use Windows 10 and still run ROS. Luckily, thanks to the Linux subsystem for Windows, Now that's easier than ever!

_Note: You need 3+ GB to spare on your computer._

[Follow this guide](https://janbernloehr.de/2017/06/10/ros-windows)
- Install the Linux subsystem for Windows
- Install ROS on that system
    - Instead of the "curl" step in the first guide, use the "curl" step for the new keyserver in [section 1.3 of the ROS installation guide](http://wiki.ros.org/Installation/Ubuntu)
- Install a windows program to display linux graphics


## Setting up ROS on Linux

1. Make a new [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
2. Source your workspace's "devel" folder
```bash
source /home/armando/Documents/armando_ws/devel/setup.bash
```
3. If you want, you can always make more catkin workspaces and use the `--extend` option to connect them to the original workspace
```bash
source /home/armando/Documents/apriltag_ws/devel/setup.bash --extend
```



## Using ROS
Use the terminal.

