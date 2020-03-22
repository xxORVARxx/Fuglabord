#!/bin/bash


# http://mywiki.wooledge.org/ProcessManagement
# Relaunch an executable if it dies
# Respawn dead processes


my_script="/home/pi/Project/Fuglabord/Fuglabord_Launcher.sh"  # <- This file name.
logger_file="_logger_$(date +'%m_%y').txt"  # <------------------- Logger file name.
python_file="/home/pi/Project/Fuglabord/Fuglabord_main.py" # <---- Python file name.


echo "$(date +'%M:%H-%d.%m.%Y') | $my_script:  All Good!  Starting program" >> $logger_file
while :; do
    python3 $python_file "/home/pi/Project/Fuglabord/" >> $logger_file 2>&1
    sleep 20
    echo "$(date +'%M:%H-%d.%m.%Y') | $my_script:  Something Went Wrong!  Restarting program..." >> $logger_file
done
echo "$(date +'%M:%H-%d.%m.%Y') | $my_script:  Something Went Wrong!  Exiting program" >> $logger_file
