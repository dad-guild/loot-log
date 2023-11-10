#!/usr/bin/env bash

# Canonicalizes the `discord` directory by sorting each file, then regenerates
# the entire state of the `csv` directory using the `convert.py` utility.

rm csv/*.csv

pushd gargul > /dev/null
ls -1 . | xargs -P32 -n1 -I{} sh -c 'sort {} -o {}.bak && mv {}.bak {} && ../convert-gargul.py {}'
popd > /dev/null
mv gargul/*.csv csv/

pushd rclc > /dev/null
ls -1 . | xargs -P32 -n1 -I{} sh -c 'sort {} -o {}.bak && mv {}.bak {} && ../convert-rclc.py {}'
popd > /dev/null
mv rclc/*.csv csv/

sed -i '' '1s;^;character,itemName,itemID,offspec,date\r\n;' csv/*.csv
