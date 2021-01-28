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

- Teach: `rosrun hand_arm teach_points.py pick_place_test`

- Replay: `rosrun hand_arm replay.py pick_place_test`



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

#### Building the catkin workspace
1. Build the workspace: `catkin_make_isolated`

2. Add the source to the `~/.bashrc` file: `source devel_isolated/setup.sh`

#### Run the apriltag detection algorithm
`roslaunch usb_cam usb_cam-test.launch`
`roslaunch apriltag_ros continuous_detection.launch`

3. Calibrate the camera (luckily NVidia has the [characteristics for the Logitech C920 webcam](https://github.com/NVlabs/Deep_Object_Pose/blob/master/doc/camera_tutorial.md))

#### Make a printable grid of april tags in pdf form
I wrote a bash script to generate pdfs of april tages with a specified real-world size. When printing the resulting pdfs, be sure to turn off "auto-scaling" and "document scaling" everywhere in the print dialog to ensure all the tags come out the correct real-world size.

```bash
#!/bin/bash

# ==============================================
# User inputs (change these settings!)
# ==============================================

# Set the folder to use
FILES=tag36h11/*.png  # Set the folder to convert from

# Set the desired width of your tags
width=30.0         # [mm]  Set the desired width in real units
dpi=300            # [ppi] Set the dpi (to control the print quality)
extra_margin=1     # [px]  Add an extra margin around your tags
default_width=10.0 # [px]  The pixel width of the original images

# Set the grid size your want to make
grid_h=4           # [num] Number of rows
grid_w=6           # [num] Number of columns
grid_filetype=pdf  # [png, jpg, pdf] Set the filetype for the grids



# ==============================================
# Do some magick! (ImageMagick)
# ==============================================

# Get the total number of files
total_files=0

for f in $FILES
do
    total_files=$((total_files+1))
done

total_files_check=$((total_files-1))


# Calculate the scale factors
scale1=$(awk "BEGIN {printf \"%.2f\",${width}*(1+(2/${default_width})) * ${dpi} / 24.5 * 100 / ${default_width}"})
scale=$(awk "BEGIN {printf \"%d\", ${scale1}"})

pixels1=$(awk "BEGIN {printf \"%.2f\",${width}*(1+(2/${default_width})) * ${dpi} / 24.5"})
pixels=$(awk "BEGIN {printf \"%d\", ${pixels1}"})

margin=$(awk "BEGIN {printf \"%d\", ${pixels1}* ${extra_margin}/${default_width}"})

grid_check=$((grid_h * grid_w))

echo "$scale1"
echo "$scale"
echo "$margin"


# Make the output filepath 
base="$(dirname -- $FILES[0])"
OUTFOLDER="${base}/${width}mm"
mkdir -p $OUTFOLDER


# Set up some variables
allnames=""
i=0
last_i=0
montage_num=0

# Loop over all pictures
for f in $FILES
do
    # Skip the mosaic picture
    if [[ "$f" == *"mosaic"* ]]; then
        total_files_check=$((total_files_check-1))
        continue
    fi

    # Generate the output filename for the current image
    ext="${f#*.}"
    filename="$(basename -- $f)"
    name=$(echo "$filename" | cut -f 1 -d '.')
    outname="${OUTFOLDER}/${name}.${ext}"
    #echo "$outname"

    # Rescale the current image
    convert $f -scale $scale% $outname

    # Add the image to the list of images to add to the current grid
    allnames="${allnames} ${outname}"

    # Every time we need to generate a grid, do it 
    v=$(((i+1)%grid_check))
    if [[ ( "$v" -eq 0  &&  "$i" != 0 ) || "$i" == "$total_files_check" ]]; then

        # Generate the output filename for the grid
        outmontage="${OUTFOLDER}/grid${last_i}_${i}.${grid_filetype}"

        # Generate the grid and save it as a pdf
        montage $allnames -geometry ${pixels}x${pixels}+${margin}+${margin} -tile ${grid_w}x -density ${dpi} $outmontage
        echo "$outmontage"

        # Update grid counters
        last_i=$((i+1))
        montage_num=$((montage_num+1))
        allnames=""
    fi

    # Update single image counter
    i=$((i+1))
done
```


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


