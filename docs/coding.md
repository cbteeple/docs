---
layout: default
title: Coding
has_children: false
permalink: coding
nav_order: 3
font_awesome: "fas fa-terminal"
---


# <i class="{{ page.font_awesome }}"></i> Coding - Programs and Tweaks
{: .no_toc }

1. TOC
{:toc}

---

## Sublime Text
A nice text editor with good themeing and visual apeal

A good basic setup: 
- Theme: Preferences >> Theme >> **Adaptive**
- Colors: Preferences >> Color Scheme >> **Monokai**

### Extensions
- [Package Control](https://packagecontrol.io/installation) - A nice way to add and remove packages to sublime. You need this for all other visual tweaks
- [Material Theme](https://github.com/equinusocio/material-theme) - Beautiful theming using material design. Be sure to set the colors back to Monokai afterward
	- Theme settings:
```json
"material_theme_accent_cyan": true,
"material_theme_big_fileicons": true,
"material_theme_bright_scrollbars": true,
"material_theme_compact_sidebar": true,
"material_theme_contrast_mode": true,
"material_theme_small_tab": true,
"material_theme_titlebar": true,
"theme": "Material-Theme-Darker.sublime-theme"
```
- [Sync Settings](https://packagecontrol.io/packages/Sync%20Settings) - A nice tool to sync sublime settings using github gists.


### Windows right-click menu items

[<i class="fas fa-file-alt"></i> subl.reg]({{ "assets/files/subl.reg" | absolute_path }}){: .btn .btn-primary }

This registy file adds several right-click options:
1. Open any file with Sublime
2. Open any folder with Sublime
	- by right-clicking on the folder
	- by right clicking on any white space inside the folder

Enjoy!


## Spyder
Python IDE

### Settings
- Tools >> Preferences >> **Syntax Coloring >> Monokai**
- Tools >> Preferences >> iPython Console >> **Graphics >> Backend >> Automatic**

### QDarkStyle

Doesn't Work
{: .label .label-red }

[QDarkStyle](https://github.com/ColinDuquesnoy/QDarkStyleSheet) dark mode for spyder. Here are the [instructions from someone on StackOverflow](https://github.com/spyder-ide/spyder/issues/2350#issuecomment-436320189)

I tried it by placing the correct line here: `C:\ProgramData\Anaconda2\Lib\site-packages\spyder\app`, but it sort of looks like garbage. For now I'm sticking to the white window with dark Monokai syntax highlighting.

### Dark Fusion

Doesn't Work
{: .label .label-red }

Based on the instructions from [this Github Issue](https://github.com/spyder-ide/spyder/issues/2350#issuecomment-440693015)

[<i class="fas fa-file-code"></i> darkflat.py]({{ "assets/files/darkflat.py" | absolute_path }}){: .btn .btn-primary}

1. Put `darkflat.py` into `C:\ProgramData\Anaconda2\Lib\site-packages\spyder\`
	- This is a modified version of the original code.
	- Modifications: Refactored the class definition to not rely on `super`
	- Additions: 
```python
from qtpy.QtGui import QPalette, QColor
from qtpy import QtCore
```
	- Subtractions:
```python
#! /usr/bin/env python3
```


2. Add the following three lines right before the `return` statement in the `initialize` function in `app/mainwindow.py`
```python
from spyder import darkflat
palette = darkflat.QDarkPalette()
palette.set_app(app)
```

3. Follow [Repligon's instructions](https://github.com/spyder-ide/spyder/issues/2350#issuecomment-440693015) to make all uncolored icons white.

Note: I tried this as well, but this styling didn't affect the title bar or the tabs in spyder's editor. I ultipmatiely abandoned my attempts to add a nice dark mode to Spyder 3.


## Jupyter Notebooks

Install Monokai theme using [jupyter-themes](https://github.com/dunovank/jupyter-themes):
```shell
pip install jupyterthemes # install jupyterthemes
jt -t monokai -T   # Use monokai theme and enable the toobar (-T)
```

As seen on [this post on StackOverflow](https://stackoverflow.com/a/49444359)


## Python Best Practices

### Packages
When making python packages, I follow Scott Torborg's guide for how to package python code

[Python Packaging Guidelines](https://python-packaging.readthedocs.io/en/latest/index.html){: .btn .btn-primary }

Tweaks I make to his style guide:
1. I place the `tests` folder in the main folder (not in the package directory)
2. I don't use the `unittest.TestCase` class

### Virtual Environments
1. Install [venv](https://docs.python.org/3/library/venv.html): `sudo apt install python3-venv`
2. Create a folder to store virtual environments (mine is in _~Documents/virtual_envs_)
3. Create a new vertual environment: `python3 -m venv ~Documents/virtual_envs/[ENV NAME]`
4. Activate a virtual environment in a terminal: `source Documents/virtual_envs/[ENV NAME]/bin/activate`