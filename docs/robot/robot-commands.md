---
layout: default
title: Robot Commands
permalink: /robot/robot-commands
parent: Robot Systems
nav_order: 1
font_awesome: "fas fa-terminal"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }


1. TOC
{:toc}

---


## Robot

[Hand+Arm Package Documentation](https://cbteeple.github.io/hand_arm_cbt_docs/){: .btn .btn-cbt-blue}
[Pressure Controller Documentation](https://cbteeple.github.io/pressure_controller_docs/){: .btn .btn-cbt-orange}

### Hardware Bringup
```bash
bash bringup-hw.sh anthro8
bash bringup-planning.sh
roslaunch hand_arm pick-place-plan-multi.launch traj:=ihm_demos/cap
roslaunch hand_arm pick-place-run-multi.launch traj:=ihm_demos/cap reps:=1 speed_factor:=1.0

```


### Real Robot
#### Bring up the robot
`roslaunch ur_modern_driver ur5e_bringup.launch limited:=true robot_ip:=192.168.1.2`


#### Move to zero and home positions:
- `rosrun hand_arm move_home.py 0`
- `rosrun hand_arm move_home.py 1`


#### Freemove/teach the robot
- Just freemove: `rosrun hand_arm teach.py`

- Teach points: `rosrun hand_arm teach_points.py [FILENAME]`, then use spacebar to set each point

- Teach continuuous (more for debug purposes): `rosrun hand_arm teach.py [FILENAME]`

- Replay: `rosrun hand_arm replay.py [FILENAME] [SPEED FACTOR]`



#### Pick and Place Action
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


### Simulated Robot
#### Gazebo
`roslaunch ur_e_gazebo ur5e.launch`

If Gazebo nodes never get started, [sometimes gazebo needs to be killed](https://answers.gazebosim.org//question/4153/gazebo-crashes-immediately-using-roslaunch-after-installing-gazebo-ros-packages/).

#### Look at RViz pose
`rostopic echo rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/feedback`

#### MoveIt!
```
roslaunch ur5_e_moveit_config ur5_e_moveit_planning_execution.launch sim:=true
roslaunch ur5_e_moveit_config moveit_rviz.launch config:=true
```


### Planning
`roslaunch hand_arm pick-place-plan.launch traj:=pick_place/pick_place_2finger`



## Hand
### Bring up the hand controller
- `roslaunch hand_arm hand_bringup.launch profile:=planar2seg`
- `roslaunch hand_arm hand_bringup.launch profile:=anthro7`



## MoveIt!

### Setting up custom end effectors
[Useful setup tutorial](https://gramaziokohler.github.io/compas_fab/latest/examples/03_backends_ros/07_ros_create_urdf_ur5_with_measurement_tool.html)

### Start up the MoveIt! Server and RViz (real robot)
```
roslaunch ur5_e_moveit_config ur5_e_moveit_planning_execution.launch limited:=false
roslaunch ur5_e_moveit_config moveit_rviz.launch config:=true
```


### Testing in a simulated robot:
`roslaunch ur5_e_moveit_config demo.launch`


### Custom Tutorial:
`rosrun moveit_tutorials move_group_python_interface_tutorial_cbt.py`


### Edit the joint limits given to the MoveIt! planner:
from the catkin workspace:
	`subl src/universal_robot/ur5_e_moveit_config/config/joint_limits.yaml`







## Useful Misc

### Kinematics Calculations:
[kinematics calculations from UR](https://www.universal-robots.com/how-tos-and-faqs/faq/ur-faq/parameters-for-calculations-of-kinematics-and-dynamics-45257)


### April Tags

See Other page


### Record Rosbags
#### Start the service
My fork of the [rosbag_recorder](https://github.com/cbteeple/rosbag-recorder) package
- Start the service using launch file
	- `roslaunch rosbag_recorder rosbag_recorder.launch`
- Pickle each bag after it's saved
	- `roslaunch rosbag_recorder rosbag_recorder.launch pickle:=true`
	- _(Note, this could take a long time if you're saving super large amounts of data)_


#### Start/Stop recording
Use a ROS service call to start and stop recording.
```python
import rosbag_recorder.srv as rbr

def start_saving(out_filename):
    rospy.wait_for_service('rosbag_recorder/record_topics')

    # Generate the topic list (robot and pressure controller topics)
    topic_list = []
    topic_list.extend(['/joint_states','/wrench','/tool_velocity'])
    topic_list.extend(['/pressure_control/echo','/pressure_control/pressure_data'])

    # Start saving data
    try:
        service = rospy.ServiceProxy('rosbag_recorder/record_topics', rbr.RecordTopics)
        response = service(out_filename, topic_list)
        return response.success
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def stop_saving(out_filename):
    # Stop saving data
    try:
        service = rospy.ServiceProxy('rosbag_recorder/stop_recording', rbr.StopRecording)
        response = service(out_filename)
        return response.success
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

```

#### Graphing later
If you pickled your data after saving, you can use another set of scripts I made to plot them

[rosbag-pickle-graph](https://github.com/cbteeple/rosbag-pickle-graph)

`python graph_robot.py ft/up200_11162019_210947`


### Generating URDFs from xacros

For example, in the [unviersal_robots](https://github.com/ros-industrial/universal_robot) package, inside "ur_e_description", ther are several urdf xacros. To generate a plain URDF from these, just use:  

`rosrun xacro xacro --inorder -o ur5e_robot.urdf ur5e_robot.urdf.xacro`


