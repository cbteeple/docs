---
layout: default
title: SSH
permalink: /linux/ssh
parent: Linux
nav_order: 4
font_awesome: "fas fa-network-wired"
---


# <i class="{{ page.font_awesome }}"></i> SSH Wizdardry

## Copy files
From Linux to Windows (must use command line):
```bash
PSCP.exe -r REMOTE_USER@IP_ADDRESS:/path/to/folder C:\Users\WINDOWS_USERNAME\Documents
```
