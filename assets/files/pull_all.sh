#!/bin/bash
# If you send an argument, use it. Otherwise, use the default list of repos
if [ "$1" != "" ] && [ "$1" != "-a" ]; then
    declare -a StringArray=("$1")
else
    declare -a StringArray=("docs" "pressure_controller_docs" "hand_arm_cbt_docs" "template")
fi



# Iterate over the repo list
for val in ${StringArray[@]}; do
	# Check if the current directory exists
	if [[ -d $val ]]
	then
		echo 
		echo PULLING FROM REMOTE:
		echo repo:    "$val"
		echo 

		# Go into the repo's main folder, commit, then go back out
		cd $val
		git pull
		cd ..
	else
		echo "Directory doesn't exist"
	fi  
done