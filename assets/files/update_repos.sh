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
		echo Updating Remote:  "$val"

		# Go into the repo's main folder, commit, then go back out
		cd $val
		git add .
		git commit -m 'Update Documentation'
		git push
		cd ..
	else
		echo "Directory doesn't exist"
	fi  
done