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


saveFile = Logging()
#saveFile.Save()

"""
sensorMgr = SensorMgr()
t = threading.Thread(target=sensorMgr.Main, args=(saveFile))
t.start()
"""
 

"""r

blStart=Bluetooth()
t = threading.Thread(target=blStart.Main,args=(liSnr,imuSnr,envSnr,))
t.setDaemon(True)#thread guard
t.start()

 
 """
 

 