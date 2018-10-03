"""
import ptvsd

ptvsd.enable_attach(('192.168.7.2',5678))
ptvsd.wait_for_attach()
ptvsd.break_into_debugger()
"""
  

import threading
import time
import logging

from Sensors.IMUSensor import *
from Sensors.EnvironmentalSensor import *
from Sensors.LightSensors import *
from Test.BMM150 import *

#lightSensor = LightSensors()
#imuSensor   = IMUSensor()
#envinSensor  = EnvironmentalSensor()

testBMM = BMM150();
while 1:
 #lightSensor.getSensors()
 #imuSensor.getSensors()
 #envinSensor.getSensors()
 
 time.sleep(2)

 