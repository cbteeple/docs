
## Gazebo
`roslaunch ur_e_gazebo ur5e.launch`

## MoveIt!
`roslaunch ur5_e_moveit_config ur5_e_moveit_planning_execution.launch sim:=true`

`roslaunch ur5_e_moveit_config moveit_rviz.launch config:=true`

## Planning
`roslaunch hand_arm pick-place-plan.launch traj:=pick_place/pick_place_2finger`


## April Tags

### Building the catkin workspace
1. Build the workspace: `catkin_make_isolated`

Add the source to the ~.bashrc file: `source devel_isolated/setup.sh`

### Run the apriltag detection algorithm
`roslaunch usb_cam usb_cam-test.launch`
`roslaunch apriltag_ros continuous_detection.launch`
