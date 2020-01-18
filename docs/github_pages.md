---
layout: default
title: GitHub Pages
permalink: github_pages
nav_order: 6
font_awesome: "fab fa-github"
---


# <i class="{{ page.font_awesome }}"></i> Useful tidbits for using github pages
{: .no_toc }


1. TOC
{:toc}


## Updating all repos at once

It's nice to automate this update step. 

[<i class="fas fa-file-alt"></i> update_repos.sh]({{ "assets/files/update_repos.sh" | absolute_url }}){: .btn .btn-primary}

```bash
# If you send an argument, use it. Otherwise, use the default list of repos
if [ "$1" != "" ] && [ "$1" != "-a" ]; then
    declare -a StringArray=("$1")
else
    declare -a StringArray=("docs" "pressure_controller_docs" "hand_arm_cbt_docs")
fi

# Ask user for a commit message unless you use the -u input
if [ "$2" != "-u" ]; then
    read -p "Commit Message: " desc
else
    desc="Update Documentation"
fi


# Iterate over the repo list
for val in ${StringArray[@]}; do
	# Check if the current directory exists
	if [[ -d $val ]]
	then
		echo 
		echo UPDATING REMOTE:
		echo repo:    "$val"
		echo msg : "$desc"
		echo 

		# Go into the repo's main folder, commit, then go back out
		cd $val
		git add .
		git commit -m "$desc"
		git push
		cd ..
	else
		echo "Directory doesn't exist"
	fi  
done
```




## Rebuilding all repos at once without updating
Sometimes I make updates to my main fork of the "Just The Docs" theme. These changes will only propagate to all of my documentation sites if they get recompiled. This only happens when new commits are pushed, so I wrote a simple bash script to send empty commits.

[<i class="fas fa-file-alt"></i> rebuild_repos.sh]({{ "assets/files/rebuild_repos.sh" | absolute_url }}){: .btn .btn-primary}

```bash
# If you send an argument, use it. Otherwise, use the default list of repos
if [ "$1" != "" ]; then
    declare -a StringArray=("$1")
else
    declare -a StringArray=("docs" "pressure_controller_docs" "hand_arm_cbt_docs")
fi

# Iterate over the repo list
for val in ${StringArray[@]}; do
	# Check if the current directory exists
	if [[ -d $val ]]
	then
		echo 
		echo Re-building "$val"

		# Go into the repo's main folder, commit, then go back out
		cd $val
		git commit -m 'rebuild pages' --allow-empty
		git push
		cd ..
	else
		echo "Directory doesn't exist"
	fi  
done
```


