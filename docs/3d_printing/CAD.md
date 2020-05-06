---
layout: default
title: CAD
permalink: /3d_printing/cad_workflow
parent: 3D Printing
nav_order: 1
font_awesome: "fas fa-terminal"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}
{: .no_toc }


### My Workflow and Customizations
{: .no_toc }

1. TOC
{:toc}

---

## Fusion 360 Tweaks

1. Use Solidworks pan/rotate commands
	- Go to "User Name" >> "Preferences"
	- Set **Pan, Zoom, Orbit shortcuts** to "**Solidworks**"
2. Set Z axis as up
	- Go to "User Name" >> "Preferences"
	- Set **Default Modeling Orientation** to "**Z up**"
	- _Note: Literally every 3D printing and CNC system sets Z-axis to be up. I don't know why CAD softwares always default to y-axis up._


## Convert Objects to OBJ Files in Fusion 360
Exporting an STL is easy in Fusion, but for some reason exporting an OBJ is not. This process is based on [a tutorial on YouTube](https://www.youtube.com/watch?v=K9WmsWWYnUI)

1. **Create** >> **Create Base Feature** to separate the obj creation process from the modeling process
2. **Modify** >> **Mesh** >> **BRep to Mesh**
3. Change all your settings similar to when you expert an STL, and click "done".
4. Right click the new mesh body >> **Save As OBJ**
 