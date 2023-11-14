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
for f in `find . -type f -name "*.csv"`; do
  cat "$f" >> "../csv/$f"
  rm "$f"
done
popd > /dev/null

pushd csv > /dev/null
ls -1 . | xargs -P32 -n1 -I{} sh -c 'sort {} -o {}.bak && mv {}.bak {}'
popd > /dev/null

sed -i '' '1s;^;character,itemName,itemID,offspec,date\r\n;' csv/*.csv
