---
layout: default
title: April Tags
permalink: /robot/april-tags
parent: Robot Systems
nav_order: 2
font_awesome: "fas fa-qrcode"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }


1. TOC
{:toc}

---

## Make a printable grid of april tags in pdf form
I wrote a bash script to generate pdfs of april tages with a specified real-world size.

[<i class="fas fa-file-alt"></i> resize-tags.sh]( {{ "assets/files/resize_tags.sh" | absolute_url }} ){: .btn .btn-primary}


1. Download the pre-made apriltag images from [thier repo](https://github.com/AprilRobotics/apriltag-imgs). _These images are all tiny (each square in the tag is one pixel)_
2. Fix ImageMagick's pdf write permissions per [these instructions](https://cromwell-intl.com/open-source/pdf-not-authorized.html)
	- `sudo gedit /etc/ImageMagick-6/policy.xml`
	- Change PDF rights to `rights="read|write"`
3. Download my "**_resize-tags.sh_**" file, and move it into the root folder of the apriltag-imgs repo.
4. Open "**_resize-tags.sh_**" in a text editor and set the parameters at the top.
```bash
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
```
5. Run the script from a terminal.
	- `bash resize-tags.sh`
	- A new folder (named by the tag dimension) will be generated inside the folder of whichever tag type you set to resize.
	- Larger images of all individual tags are stored in the new folder.
	- Printable grids are also generated according to your settings.
6. Print grids. _**When printing the grid pdfs, be sure to turn off "auto-scaling" and "document scaling" everywhere in the print dialog to ensure all the tags come out the correct real-world size.**_

### PDFs for the standard "tag36h11" tags
Since I use the "tag36h11" often, I have already generated sets of printable tags in PDF form at various standard dimensions.

[<i class="fas fa-file-archive"></i> 30 mm Side Length]( {{ "assets/files/tag36h11_30mm.zip" | absolute_url }} ){: .btn .btn-primary}

[<i class="fas fa-file-archive"></i> 60 mm Side Length]( {{ "assets/files/tag36h11_60mm.zip" | absolute_url }} ){: .btn .btn-primary}

[<i class="fas fa-file-archive"></i> 90 mm Side Length]( {{ "assets/files/tag36h11_90mm.zip" | absolute_url }} ){: .btn .btn-primary}

<img alt="The first 24 april tags with side lengths of 30mm in a nice printable grid"
     src="{{ "assets/img/apriltags_30mm.png" | absolute_url }}"/>


## Setting up a test workspace

### Building the catkin workspace
1. Build the workspace: `catkin_make_isolated`

2. Add the source to the `~/.bashrc` file: `source devel_isolated/setup.sh`

### Run the apriltag detection algorithm
`roslaunch usb_cam usb_cam-test.launch`
`roslaunch apriltag_ros continuous_detection.launch`

3. Calibrate the camera (luckily NVidia has the [characteristics for the Logitech C920 webcam](https://github.com/NVlabs/Deep_Object_Pose/blob/master/doc/camera_tutorial.md))

## Combining april tags with the rest of robot control
You need to use a separate workspace for apriltags due to some conflicts in the way the apriltags ros package needs to be built.

You can see how to do that in the [ROS]({{ site.baseurl }}{% link docs/robot/ros.md %}) page

