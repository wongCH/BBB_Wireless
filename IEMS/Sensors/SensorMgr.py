from Sensors.IMUSensor import *
from Sensors.EnvironmentalSensor import *
from Sensors.LightSensors import *
from Helpers.Constant import *
import json
import pprint
class SensorMgr(object):
    """Manager class in charge of calling all the Sensors"""

    def __init__(self): 
        self.liSnr   = LightSensors()
        self.imuSnr  = IMUSensor()
        self.envSnr  = EnvironmentalSensor()

    def Main(self,loggingMgr,mqttServer):
         objJson =  Constant.INTERFACE_JSON
         ojbchild = Constant.INTEFACE_CHILD
         while Constant.SENSOR_WORKING:
            try:
                liData   = self.liSnr.getSensors()
                imuData  = self.imuSnr.getSensors()
                envData  = self.envSnr.getSensors()
               
                
                
                #print (envData)
                #print(imuData)
                #print(liData )
                #cannot return, the whole thing will be terminated if return
                #objJson["data"]

                
                ojbchild["created"] = int(time.time() * 1000)
                ojbchild["lux"] =liData
                ojbchild["tem"] =envData['temp']
                ojbchild["hum"] = envData['humi']
                ojbchild["pre"] =envData['pres']
               
                ojbchild["gyr"]['x'] = imuData['gyro_x']
                ojbchild["gyr"]['y'] = imuData['gyro_y']
                ojbchild["gyr"]['z'] = imuData['gyro_z']
                ojbchild["acc"]['x'] = imuData['acc_x']
                ojbchild["acc"]['y'] = imuData['acc_y']
                ojbchild["acc"]['z'] =imuData['acc_z']
                
                #mqtt cannot append, need to send immediately
                mqttServer.Send(json.dumps(ojbchild, separators=(',',': ')))

                objJson["data"].append(ojbchild)
                strJson = json.dumps(objJson, separators=(',',': '))
                loggingMgr.Save(strJson)
                
              
                
                print (strJson)                
            except Exception  as e:
                print ("Error at sensor:" + str(e))

            time.sleep(Constant.SNR_SLEEP)
