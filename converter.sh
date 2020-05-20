#!/bin/bash
echo "Press [CTRL+C] to stop.."
while true
do
	for filename in ./*.wav; do
        oggenc -o "$filename.ogg" $filename
        rm $filename
    done
done
 
