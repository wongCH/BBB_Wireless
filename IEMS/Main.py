 
"""
import ptvsd

ptvsd.enable_attach(('192.168.7.2',5678))
ptvsd.wait_for_attach()
ptvsd.break_into_debugger()
"""
 

import threading
 
import time
import datetime
import logging

from Sensors.IMUSensor import *
from Sensors.EnvironmentalSensor import *
from Sensors.LightSensors import *

#from Connection.Beebotte import *   
from Connection.MqttConn import *

liSnr = LightSensors()
imuSnr   = IMUSensor()
envSnr  = EnvironmentalSensor()


#sendToSrv = Beebotte()
sendToSrv = MqttConn()
while 1:
 unixTime =  int(time.time() * 1000)
 liData = liSnr.getSensors()
 imuData = imuSnr.getSensors()
 envData=envSnr.getSensors()
 
 sendToSrv.publish(unixTime,liData,envData['temp'],envData['humi'],envData['pres'],imuData['gyro_x'], imuData['gyro_y'],imuData['gyro_z'],imuData['acc_x'],imuData['acc_y'],imuData['acc_z'])
 time.sleep(2)
 

 