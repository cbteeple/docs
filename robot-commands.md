
## Gazebo
roslaunch ur_e_gazebo ur5e.launch

## MoveIt!
roslaunch ur5_e_moveit_config ur5_e_moveit_planning_execution.launch sim:=true

roslaunch ur5_e_moveit_config moveit_rviz.launch config:=true

## Planning
roslaunch hand_arm pick-place-plan.launch traj:=pick_place/pick_place_2finger