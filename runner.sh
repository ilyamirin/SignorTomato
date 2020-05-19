#!/bin/bash
#export IAM_TOKEN="$(yc iam create-token)"
echo "Press [CTRL+C] to stop.."
while true
do
	python3 audio_writer.py 
    oggenc -q 3 -o output.ogg output.wav >> ogg.log
    python3 speech_to_text.py >> speech.log
done
 
