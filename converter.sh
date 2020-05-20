#!/bin/bash
echo "Press [CTRL+C] to stop.."
while true
do
	for filename in ./*.wav; do
        oggenc -o "$filename.ogg.tmp" $filename
        mv "$filename.ogg.tmp" "$filename.ogg"
        rm $filename
    done
    sleep 1
done
 
