from Sensors.IMUSensor import *
from Sensors.EnvironmentalSensor import *
from Sensors.LightSensors import *
from Helpers.Constant import *
class SensorMgr(object):
    """Manager class in charge of calling all the Sensors"""

    def __init__(self): 
        self.liSnr   = LightSensors()
        self.imuSnr  = IMUSensor()
        self.envSnr  = EnvironmentalSensor()

    def Main(self,loggingMgr):
         while Constant.SENSOR_WORKING:
            try:
                print(Constant.SENSOR_WORKING)
                unixTime = Constant.CURRENT_TIME
                liData   = self.liSnr.getSensors()
                imuData  = self.imuSnr.getSensors()
                envData  = self.envSnr.getSensors()
            
                #print (envData)
                #print(imuData)
                #print(liData )
                #cannot return, the whole thing will be terminated if return

                #return (liData,envData['temp'],envData['humi'],envData['pres'],imuData['gyro_x'], imuData['gyro_y'],imuData['gyro_z'],imuData['acc_x'],imuData['acc_y'],imuData['acc_z'])
                time.sleep(Constant.SNR_SLEEP3)
            except:
                print ("error at sensor")


