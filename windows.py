import winsound

file = "sound.wav"  # Make sure the file is in the same folder
winsound.PlaySound(file, winsound.SND_FILENAME)