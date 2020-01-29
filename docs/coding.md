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

## Spyder
Python IDE

### Settings
- Tools >> Preferences >> **Syntax Coloring >> Monokai**
- Tools >> Preferences >> iPython Console >> **Graphics >> Backend >> Automatic**

### QDarkStyle

Failed
{: .label .label-red }

[QDarkStyle](https://github.com/ColinDuquesnoy/QDarkStyleSheet) dark mode for spyder. Here are the [instructions from someone on StackOverflow](https://github.com/spyder-ide/spyder/issues/2350#issuecomment-436320189)

I tried it by placing the correct line here: `C:\ProgramData\Anaconda2\Lib\site-packages\spyder\app`, but it sort of looks like garbage. For now I'm sticking to the white window with dark Monokai syntax highlighting.

### Dark Fusion

Failed
{: .label .label-red }

Based on the instructions from [this Github Issue](https://github.com/spyder-ide/spyder/issues/2350#issuecomment-440693015)
1. Put the following code into a file named `darkflat.py`, and place it in `C:\ProgramData\Anaconda2\Lib\site-packages\spyder\`

{% raw %}
```python
#! /usr/bin/env python

from qtpy.QtGui import QPalette, QColor
from qtpy import QtCore


WHITE =     QColor(255, 255, 255)
BLACK =     QColor(0, 0, 0)
RED =       QColor(255, 0, 0)
PRIMARY =   QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY =  QColor(42, 130, 218)


def css_rgb(color, a=False):
    """Get a CSS `rgb` or `rgba` string from a `QtGui.QColor`."""
    return ("rgba({}, {}, {}, {})" if a else "rgb({}, {}, {})").format(*color.getRgb())


class QDarkPalette():
    """Dark palette for a Qt application meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        # Set all the colors based on the constants in globals       
        palette=QPalette()     
        palette.setColor(QPalette.Window,          PRIMARY)
        palette.setColor(QPalette.WindowText,      WHITE)
        palette.setColor(QPalette.Base,            SECONDARY)
        palette.setColor(QPalette.AlternateBase,   PRIMARY)
        palette.setColor(QPalette.ToolTipBase,     WHITE)
        palette.setColor(QPalette.ToolTipText,     WHITE)
        palette.setColor(QPalette.Text,            WHITE)
        palette.setColor(QPalette.Button,          PRIMARY)
        palette.setColor(QPalette.ButtonText,      WHITE)
        palette.setColor(QPalette.BrightText,      RED)
        palette.setColor(QPalette.Link,            TERTIARY)
        palette.setColor(QPalette.Highlight,       TERTIARY)
        palette.setColor(QPalette.HighlightedText, BLACK)


        palette.setColor(QPalette.Disabled, QPalette.Text, QtCore.Qt.darkGray)
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QtCore.Qt.darkGray)
        
        self.palette=palette
        
    @staticmethod
    def set_stylesheet(app):
        """Static method to set the tooltip stylesheet to a `QtWidgets.QApplication`."""
        app.setStyleSheet("QToolTip {{"
                          "color: {white};"
                          "background-color: {tertiary};"
                          "border: 1px solid {white};"
                          "}}".format(white=css_rgb(WHITE), tertiary=css_rgb(TERTIARY)))

    def set_app(self, app):
        """Set the Fusion theme and this palette to a `QtWidgets.QApplication`."""
        app.setStyle("Fusion")
        app.setPalette(self.palette)
        self.set_stylesheet(app)
```
{% endraw %}

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