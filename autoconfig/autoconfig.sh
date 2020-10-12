#!/bin/sh
###
# @file      autoconfig.sh
# @brief     Automatically configures certain things.
#
# @author    Evan Elias Young
# @date      2020-10-12
# @date      2020-10-12
# @copyright Copyright 2020 Evan Elias Young. All rights reserved.
###

die() {
    echo "$1";
    exit 1;
}

if [ -z "$1" ]; then die "usage: autoconfig.sh <config>"; fi
if [ ! -f "$1" ]; then die "failed to find the config file"; fi

lines=$(wc -l < "$1")
if [ $lines -lt 3 ]; then die "config file too short"; fi

eval dest=$(head -n1 "$1")
if [ -d "$dest" ]; then die "config file identified a directory as the destination"; fi
if [ -w "$dest" ]; then die "you have insufficient permissions"; fi

contents=$(tail -n+3 "$1")
echo "$contents" > "$dest"
echo "success! copied configuration from $1 to $dest!"
