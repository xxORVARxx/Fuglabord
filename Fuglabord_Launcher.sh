#!/bin/bash
#
# http://mywiki.wooledge.org/ProcessManagement
# Relaunch an executable if it dies:
#

python_file="Fuglabord_main.py" # <------------- Python file name. 
logger_file="_logger_$(date +'%m_%y').txt" # <-- Logger file name. 

script=`basename $0`
directory="$1"
echo "$(date +'%d.%m.%Y-%H:%M') | $script:  Allt Gott!  Kveiki á Python forriti." >> ${directory}${logger_file}
while :; do
    sleep 5
    sudo python3 "${directory}${python_file}" "$directory" >> "${directory}${logger_file}" 2>&1
    sleep 15
    echo "$(date +'%d.%m.%Y-%H:%M') | $script:  Eitthvað fór úrskeiðis!  Endurræsi Python forrit..." >> ${directory}${logger_file}
done
echo "$(date +'%d.%m.%Y-%H:%M') | $script:  Eitthvað fór úrskeiðis!  slökkt á Python forriti" >> ${directory}${logger_file}
