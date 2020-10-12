#!/bin/sh
###
# @file      pipup.sh
# @brief     Updates all the outdated Python packages.
#
# @author    Evan Elias Young
# @date      2016-03-27
# @date      2020-10-12
# @copyright Copyright 2020 Evan Elias Young. All rights reserved.
###

which python3 &> /dev/null
if [ ! $? -eq 0 ]; then echo "failed to detect a python3 installation"; exit 1; fi

python3 -m pip &> /dev/null
if [ ! $? -eq 0 ]; then echo "failed to detect a pip3 installation"; exit 1; fi

dated=$(python3 -m pip list -o --format=freeze | sed 's|==.*||g')

while IFS= read -r line; do
    python3 -m pip install -U "$line"
done <<< "$dated"
