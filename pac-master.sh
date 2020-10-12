#!/bin/sh
###
# @file      pac-master.sh
# @brief     My master pacman command.
#
# @author    Evan Elias Young
# @date      2020-10-12
# @date      2020-10-12
# @copyright Copyright 2020 Evan Elias Young. All rights reserved.
###

which pacman &> /dev/null
if [ ! $? -eq 0 ]; then echo "failed to locate pacman installation"; exit 1; fi

sudo pacman -Syy --noconfirm
sudo pacman -Su --noconfirm

echo $(date +%s) > .lpac
