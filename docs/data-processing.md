---
layout: default
title: Data Processing
permalink: /data-processing
nav_order: 4
font_awesome: "fas fa-chart-bar"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}


Some useful tools for data processing in python

## Convert rosbag files to a Pandas Dataframe
[rosbag_pandas](https://github.com/aktaylor08/RosbagPandas) library from aktaylor08

## Plot pickled rosbag data

[rosbag-pickle-graph](https://github.com/cbteeple/rosbag-pickle-graph){: .btn .btn-primary}

`python graph_robot.py ft/up200_11162019_210947`

## Nice-looking plots

### Making plots for IEEE conferences
Thanks to this [blog post by Bastian Bloessl](https://www.bastibl.net/publication-quality-plots/).

### Color palettes
The [seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) package in python lets me set nice color palettes. My color palette of choice right now is `GnBu_d`
```python
import seaborn as sns

sns.set_palette(sns.color_palette("GnBu_d", 8))
sns.set_style("ticks")
sns.despine()
```

