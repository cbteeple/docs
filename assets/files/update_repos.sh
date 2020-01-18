#!/bin/bash
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