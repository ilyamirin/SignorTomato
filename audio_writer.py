#!python3
import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime

fs = 48000  # Sample rate
seconds = 3  # Duration of recording

while True:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    ts = datetime.utcnow().timestamp()
    write("%s.wav" % ts, fs, myrecording)  # Save as WAV file 

