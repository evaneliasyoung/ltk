#!/bin/sh
###
# @file      apt-master.sh
# @brief     My master apt command.
#
# @author    Evan Elias Young
# @date      2013-10-07
# @date      2020-10-12
# @copyright Copyright 2020 Evan Elias Young. All rights reserved.
###

which apt-get &> /dev/null
if [ ! $? -eq 0 ]; then echo "failed to locate apt installation"; exit 1; fi

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y autoremove
sudo apt-get -y autoclean

echo $(date +%s) > .lapt
