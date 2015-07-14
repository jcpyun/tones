from a4tuning  import *
from snd110 import *

ND = notesDict()
TD = timesDict()

def readNote(note):
  split = note.split(",")
  freq = ND[split[0]]
  dur = TD[split[1]]
  return (freq,dur)

def readSongFile(file):
  global ND
  global TD
  song = open(file)
  notes = []
  for note in song.readlines():
    notes.append(readNote(note))
  return notes

def makeMusic(notes):
  newSound = []
  for note in notes:
    freq = note[0]
    duration = note[1]*60.0/tempo
    new = sine_tone(freq, duration, 1.0)
    newSound += new
  return newSound

def createSong(songFile, writeFile):
  notes = readSongFile(songFile)
  song = makeMusic(notes)
  if (writeFile[-4:] != ".wav"):
    writeFile += ".wav"
  write_wave(writeFile, song)

import sys
createSong(sys.argv[1], sys.argv[2])



