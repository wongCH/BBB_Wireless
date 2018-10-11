from Sensors.IMUSensor import *
from Sensors.EnvironmentalSensor import *
from Sensors.LightSensors import *
from Helpers.Constant import *
import copy
import json
import pprint
class SensorMgr(object):
    """Manager class in charge of calling all the Sensors"""

    def __init__(self): 
        self.Initialize()

    def Initialize(self):
        """
            use this method to initialize the sensors
            this method also needed when we build self-recovery function
        """
        self.liSnr   = LightSensors()
        self.imuSnr  = IMUSensor()
        self.envSnr  = EnvironmentalSensor()

    def Main(self,loggingMgr,mqttServer,clsCompress):
         
         objJson = {"data":[]}
         #objchild = Constant.INTERFACE_JSON

         intMsgCount = 0
         while Constant.SENSOR_WORKING:
            try:
                objchild = Constant.INTERFACE_JSON
                liData   = self.liSnr.getSensors()
                imuData  = self.imuSnr.getSensors()
                envData  = self.envSnr.getSensors()
                
                objchild["created"] = int(time.time() * 1000)
                objchild["lux"] =liData
                objchild["tem"] =envData['temp']
                objchild["hum"] = envData['humi']
                objchild["pre"] =envData['pres']
               
                objchild["gyr"]['x'] = imuData['gyro_x']
                objchild["gyr"]['y'] = imuData['gyro_y']
                objchild["gyr"]['z'] = imuData['gyro_z']
                objchild["acc"]['x'] = imuData['acc_x']
                objchild["acc"]['y'] = imuData['acc_y']
                objchild["acc"]['z'] =imuData['acc_z']
                
                objJson["data"].append(objchild.copy())
 
                #print(copy.copy(objchild)
                if intMsgCount == Constant.MSG_COUNT :
                
                    intMsgCount = 0
                   
                    strJson = json.dumps(objJson, separators=(',',': '))
                    
                    loggingMgr.Save(strJson)

                    compressedJson = clsCompress.GZipStr(strJson)
                    mqttServer.Send(compressedJson)
                    mqttServer.Send(strJson)


                    objJson = {"data":[]}
                    print ("data Sent")
                intMsgCount += 1         
            except Exception  as e:
                print ("Error at sensor:" + str(e))

            time.sleep(Constant.SNR_SLEEP)
