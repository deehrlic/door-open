import snowboydecoder
import os

def detected_callback():
	print "hotword caught opening door"
	os.system('python motorSnow.py')


detector = snowboydecoder.HotwordDetector("Bloomie.pmdl", sensitivity = 0.5, audio_gain = 1)

detector.start(detected_callback)
