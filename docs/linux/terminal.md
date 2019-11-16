---
layout: default
title: Terminal Colors
permalink: /linux/terminal
parent: Linux
nav_order: 1
font_awesome: "fas fa-terminal"
---


# <i class="{{ page.font_awesome }}"></i> Bash Color Customization + Git Integration

1. Open your `~.bashrc` file in a text editor: `subl ~.bashrc`
2. Add one of the following options at the end of the file


- The original from [StackExchange](https://gist.github.com/justintv/168835#gistcomment-1717504) adds the git branch name in red and starts prompt at a new line
	- `PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\]\u@\h: \[\033[36;1m\]\w\[\033[0;32m\]$(__git_ps1)\n\[\033[0;32m\]└─\[\033[0m\033[0;32m\] \$\[\033[0m\033[0;32m\] ▶\[\033[0m\] '`

- In my cleaner modification, the actual prompt at the newline is slimmer.
	- `PS1='\[\033[0;32m\]\[\033[0m\033[1;32m\]\u@\h: \[\e[34;1m\]\w\[\033[1;31m\]$(__git_ps1)\n\[\033[0m\033[1;0m\]\$\[\033[0m\] '`



![Nice-colored terminal]({{ "/assets/img/terminal-colors.png" | absolute_url }})