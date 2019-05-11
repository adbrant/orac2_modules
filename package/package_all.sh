#!/bin/bash

cd ../usermodules/
for category in $(find  -mindepth 1 -maxdepth 1 -type d ); do
  cd $category
  for f in $(find  -mindepth 1 -maxdepth 1 -type d ); do
    echo $f
    zip -v -r "$f" "$f"
  done
  mv -f *.zip ../../package
  cd ..
done




