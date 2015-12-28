import xbmcaddon
import xbmcgui
import RPi.GPIO as GPIO
import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


#Set pin numbering to board numbering
GPIO.setmode(GPIO.BCM)

# set pin 18 to be in output mode
GPIO.setup(18, GPIO.OUT)

PIN = 18
run = True
state = GPIO.input(PIN)

while(run):
  try:
    if (state is True):
         GPIO.output(PIN, GPIO.LOW)
    else:
          GPIO.output(PIN, GPIO.HIGH)
    
   

  except KeyboardInterrupt:
    run = False
    GPIO.cleanup()
    print



 
