#!/bin/bash


# It will list all the PIDs related to my_script.sh and
# verify if they are the same of the process we are
# currently running. If not, then exits the script.


for pid in $(pidof -x Fuglabord_pilot.sh); do
    if [ $pid != $$ ]; then
	touch ./Log/pilot.log
	echo "$(date +'%M:%H-%d.%m.%Y') | Allt gott! Forrit er í ganagi." >> ./Log/pilot.log
        exit 1
    fi 
done
touch ./Log/pilot.log
echo "$(date +'%M:%H-%d.%m.%Y') | Allt gott! Forrit sett í ganag." >> ./Log/pilot.log
python3 ./Fuglabord_main.py >> ./Log/pilot.log 2>&1
