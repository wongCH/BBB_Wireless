from Sensors.IMUSensor import *
from Sensors.EnvironmentalSensor import *
from Sensors.LightSensors import *
from Helpers.Constant import *
class SensorMgr(object):
    """Manager class in charge of calling all the Sensors"""

    def Main(): 
        liSnr   = LightSensors()
        imuSnr  = IMUSensor()
        envSnr  = EnvironmentalSensor()
        while Constant.SENSOR_WORKING:
            unixTime = Constant.CURRENT_TIME
            liData   = liSnr.getSensors()
            imuData  = imuSnr.getSensors()
            envData  =envSnr.getSensors()
            return (liData,envData['temp'],envData['humi'],envData['pres'],imuData['gyro_x'], imuData['gyro_y'],imuData['gyro_z'],imuData['acc_x'],imuData['acc_y'],imuData['acc_z'])


