---
layout: default
title: Plotting Data
permalink: /robot/plotting-data
parent: Robot Systems
nav_order: 4
font_awesome: "fas fa-chart-bar"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }


1. TOC
{:toc}

---


## Use the plotting functions
[Download the plotting package](https://github.com/cbteeple/soft-finger-characterization){: .btn .btn-primary}


## Get the object angle from video

### Track a video using Tracker
I use [Tracker](https://physlets.org/tracker/), an open source video tracking software. It's pretty bad, but it gets the job done for free!

Makes sure to save the raw data from two tracking points, using  `_A.dat` and `_B.dat` at the end of the files.

### Plot the object angle from the raw image tracking data

Use "**plot_video_data.py**"

```python
python plot_video_data.py planned_23_00/2020_01_20 diam23_angles0_30_base80_tip92_0006
```

Inputs:

- **data_folder** - the folder where your data is stored
- **filename** - the name of the tracked file family (_do not include the `_A.dat` part_) 
- _pickle_ (optional) - pickle the data once calculated (varients: -p, -s, pickle, save)

Outputs:

- **Plot of the angle vs. time**
- **pickled data** if you told it to save that

_Note: all output files are saved in the same folder as the data files._

### Usage Examples:

- folder: *planned_23_00* >> *2020_01_20*
- file: *diam23_angles0_30_base80_tip92_0006*
- pickle: yes

```python
python plot_video_data.py planned_23_00/2020_01_20 diam23_angles0_30_base80_tip92_0006 -p
```