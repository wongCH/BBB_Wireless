"""
 Sensor Model : BME280
"""
import Adafruit_GPIO.I2C as I2C
from Sensors import BME280
from Sensors.BaseSensor import *
from enum import Enum

from Sensors.BME280 import *


class EnvironmentalSensor(BaseSensor):
    """
        This class is to defined BMP280 sensors configuration and also settings
    """
     
    #I2C Address/BITS/Settings
    __BMP280_ADDRESS = 0x77
    __BMP280_CHIPID  = 0x58
    __BBB_BUSNO      = 2
    __BMP280_BITSIZE = 2
    #Registers                  

    
    def __init__(self):
        super().__init__( self.__BMP280_ADDRESS, self.__BBB_BUSNO, None, self.__BMP280_BITSIZE)
        self.bme = BME280()

    def getSensors(self):
        t, p, h = self.bme.get_data()
        #print ("Temperature:{0}, Pressure:{1}, Humidity;{2}".format(t,p,h))
        return  {"temp":t,"humi":h, "pres":p}
        