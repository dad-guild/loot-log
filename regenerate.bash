#!/usr/bin/env bash

# Canonicalizes the `discord` directory by sorting each file, then regenerates
# the entire state of the `csv` directory using the `convert.py` utility.

pushd discord > /dev/null
ls -1 . | xargs -P32 -n1 -I{} sh -c 'sort {} -o {}.bak && mv {}.bak {} && ../convert.py {}'
popd > /dev/null
mv discord/*.csv csv/
