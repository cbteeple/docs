---
layout: default
title: Login Theme
permalink: /linux/login
parent: Linux
nav_order: 3
font_awesome: "fas fa-sign-in-alt"
---

# <i class="{{ page.font_awesome }}"></i> {{ page.title }}

## A nicer startup theme that fills some gaps
It turns out you can edit the css file that determines what the login page looks like.

**This is tested in Ubuntu 18.04**

1. Download my custom theme
2. To edit the real style sheet, open the original `ubuntu.css` file
	- `sudo subl /usr/share/gnome-shell/theme/ubuntu.css`
3. Copy the text form my custom theme into the real stylesheet
4. Restart to apply changes.


## Download the theme
[ubuntu.css]({{ "assets/files/ubuntu.css" | absolute_url }}){: .btn .btn-primary}