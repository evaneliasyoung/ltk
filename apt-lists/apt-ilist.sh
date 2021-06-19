#!/bin/bash
###
# @file      apt-ilist.sh
# @brief     Installs a list of apt packages.
#
# @author    Evan Elias Young
# @date      2021-06-18
# @date      2021-06-18
# @copyright Copyright 2021 Evan Elias Young. All rights reserved.
###

die() {
    echo "$1";
    exit 1;
}

which apt-get &> /dev/null
if [ ! $? -eq 0 ]; then die "failed to locate apt installation"; fi

if [ -z "$1" ]; then die "usage: install_list.sh <list>"; fi
if [ ! -f "$1" ]; then die "failed to find the package listing file"; fi

xargs sudo apt-get install -y < "$1"
