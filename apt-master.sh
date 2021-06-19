#!/bin/bash
###
# @file      apt-master.sh
# @brief     My master apt command.
#
# @author    Evan Elias Young
# @date      2013-10-07
# @date      2021-06-18
# @copyright Copyright 2020-2021 Evan Elias Young. All rights reserved.
###

which apt-get &> /dev/null
if [ ! $? -eq 0 ]; then echo "failed to locate apt installation"; exit 1; fi

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y autoremove
sudo apt-get -y autoclean
