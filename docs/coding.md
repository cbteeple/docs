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

### Settings
- Tools >> Preferences >> **Syntax Coloring >> Monokai**
- Tools >> Preferences >> iPython Console >> **Graphics >> Backend >> Automatic**

### QDarkStyle
[QDarkStyle](https://github.com/ColinDuquesnoy/QDarkStyleSheet) dark mode for spyder. Here are the [instructions from someone on StackOverflow](https://github.com/spyder-ide/spyder/issues/2350#issuecomment-436320189)

I tried it by placing the correct line here: `C:\ProgramData\Anaconda2\Lib\site-packages\spyder\app`, but it sort of looks like garbage. For now I'm sticking to the white window with dark Monokai syntax highlighting.