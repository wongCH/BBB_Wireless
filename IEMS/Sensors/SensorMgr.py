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
                unixTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                
                
                #print (envData)
                #print(imuData)
                #print(liData )
                #cannot return, the whole thing will be terminated if return
                #objJson["data"]

                
                ojbchild["dateTime"] =unixTime
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
                
                objJson["data"].append(ojbchild)
                
                strJson = json.dumps(objJson, separators=(',',': '))
                mqttServer.Send(strJson)
                #loggingMgr.Save(strJson)
                print (strJson)
                
            except Exception  as e:
                print ("Error at sensor:" + str(e))

            time.sleep(Constant.SNR_SLEEP)
