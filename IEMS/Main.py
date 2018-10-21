 #!/usr/bin/python3
"""
import ptvsd

ptvsd.enable_attach(('192.168.7.2',5678))
ptvsd.wait_for_attach()
ptvsd.break_into_debugger()
"""
 
import time
import datetime
import logging
import threading

from Helpers.Constant import *
from Sensors.SensorMgr import *
from Helpers.Logging import *
from Connection.MqttConn import *
from Helpers.Compress import *
from Helpers.WifiConn import *

saveFile = Logging()
mqttServer = MqttConn()

sensorMgr = SensorMgr()
t = threading.Thread(target=sensorMgr.Main, args=(saveFile,mqttServer,Compress,))
t.start()

t = threading.Thread(WifiConn.EstablishConn)
t.start();

"""r

blStart=Bluetooth()
t = threading.Thread(target=blStart.Main,args=(liSnr,imuSnr,envSnr,))
t.setDaemon(True)#thread guard
t.start()

 
 """
 

 