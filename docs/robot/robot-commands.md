---
layout: default
title: Robot Commands
permalink: /robot/robot-commands
parent: Robot Systems
nav_order: 1
font_awesome: "fas fa-terminal"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}



# Robot:

[Hand+Arm Package Documentation](https://cbteeple.github.io/hand_arm_cbt_docs/){: .btn .btn-primary}
[Pressure Controller Documentation](https://cbteeple.github.io/pressure_controller_docs/){: .btn}

## Real Robot
### Bring up the robot
`roslaunch ur_modern_driver ur5e_bringup.launch limited:=true robot_ip:=192.168.1.2`


### Move to zero and home positions:
- `rosrun hand_arm move_home.py 0`
- `rosrun hand_arm move_home.py 1`


### Freemove/teach the robot
- Just freemove: `rosrun hand_arm teach.py`

- Teach: `rosrun hand_arm teach_points.py pick_place_test`

- Replay: `rosrun hand_arm replay.py pick_place_test`



### Pick and Place Action
- Joint Space
	- `roslaunch hand_arm pick-place-run.launch traj_profile:=pick_front speed_factor:=2.0 num_reps:=20`

- Cartesian
	- `roslaunch hand_arm pick-place-run.launch traj_profile:=pick_front_xyz num_reps:=20`
	- `roslaunch hand_arm pick-place-run.launch traj_profile:=pick_place/pick_place_2finger num_reps:=20`
	- `roslaunch hand_arm pick-place-run.launch traj_profile:=pick_place/pick_place_4finger reps:=10`


- Build Pick and Place
	- `roslaunch hand_arm pick-place-build.launch traj_profile:=pick_place/pick_place_2finger`

- Plan Pick and Place
	- `roslaunch hand_arm pick-place-plan.launch traj:=pick_place/pick_place_2finger`

- Multiple Trajectories
	- `roslaunch hand_arm pick-place-build-multi.launch traj:=pick_place/pick_place_4finger_grid`
	- `roslaunch hand_arm pick-place-plan-multi.launch traj:=pick_place/pick_place_4finger_grid`
	- `roslaunch hand_arm pick-place-run-multi.launch traj:=pick_place/pick_place_4finger_grid reps:=4`


## Simulated Robot
### Gazebo
`roslaunch ur_e_gazebo ur5e.launch`

### Look at RViz pose
`rostopic echo rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/feedback`

### MoveIt!
```
roslaunch ur5_e_moveit_config ur5_e_moveit_planning_execution.launch sim:=true
roslaunch ur5_e_moveit_config moveit_rviz.launch config:=true
```


## Planning
`roslaunch hand_arm pick-place-plan.launch traj:=pick_place/pick_place_2finger`



# Hand:
## Bring up the hand controller
- `roslaunch hand_arm hand_bringup.launch profile:=planar2seg`
- `roslaunch hand_arm hand_bringup.launch profile:=anthro7`



# MoveIt!
## Start up the MoveIt! Server and RViz (real robot)
```
roslaunch ur5_e_moveit_config ur5_e_moveit_planning_execution.launch limited:=false
roslaunch ur5_e_moveit_config moveit_rviz.launch config:=true
```


## Testing in a simulated robot:
`roslaunch ur5_e_moveit_config demo.launch`


## Custom Tutorial:
`rosrun moveit_tutorials move_group_python_interface_tutorial_cbt.py`


## Edit the joint limits given to the MoveIt! planner:
from the catkin workspace:
	`subl src/universal_robot/ur5_e_moveit_config/config/joint_limits.yaml`







# Useful Misc

## Kinematics Calculations:
[kinematics calculations from UR](https://www.universal-robots.com/how-tos-and-faqs/faq/ur-faq/parameters-for-calculations-of-kinematics-and-dynamics-45257)


## April Tags

### Building the catkin workspace
1. Build the workspace: `catkin_make_isolated`

2. Add the source to the `~/.bashrc` file: `source devel_isolated/setup.sh`

### Run the apriltag detection algorithm
`roslaunch usb_cam usb_cam-test.launch`
`roslaunch apriltag_ros continuous_detection.launch`

## Regord Rosbags
[rosbag_recorder](https://github.com/chili-epfl/rosbag-recorder) package