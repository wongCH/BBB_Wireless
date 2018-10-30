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
from Connection.WifiConnServer import *

saveFile = Logging()
mqttServer = MqttConn()
wifiConn = WifiConnServer()

sensorMgr = SensorMgr()
t = threading.Thread(target=sensorMgr.Main, args=(saveFile,mqttServer,Compress,))
t.start()

t = threading.Thread(target=wifiConn.listen_for_clients, args=())
#t.daemon = True
t.start()


"""r

blStart=Bluetooth()
t = threading.Thread(target=blStart.Main,args=(liSnr,imuSnr,envSnr,))
t.setDaemon(True)#thread guard
t.start()

 
 """
 

 