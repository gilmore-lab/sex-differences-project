import psychtoolbox as ptb
from psychopy import sound, core

mySound = sound.Sound('E', secs=0.5, octave=5)
mySound.play(loops = 0)
core.wait(1)

print("Done with 1")

highA = sound.Sound('A', octave=3, sampleRate=44100, secs=1.5, stereo=True)
highA.play(loops=-1)
print("Really done")
