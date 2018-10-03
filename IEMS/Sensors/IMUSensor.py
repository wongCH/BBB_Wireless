
from Sensors.BaseSensor import *
import datetime
import time
 

class IMUSensor(BaseSensor):
    
    def __init__(self, deviceAddr=0x69, busNum=2,interface=None, bitSize=2):
       """
            Reading from IMU
            I2C address= 0x69
            busNum=2
            bitSize = 2 (7bit)
       """
       super().__init__(deviceAddr,busNum,interface,bitSize)
       
       # step1: wake up the sensor device and set it to Normal Mode (refer to datasheet)
       self.Device = I2C.Device(address=deviceAddr,busnum=busNum) #i2c address and busNum in BBB
       #self.Device.writeList(0x7E,bytearray(b'\x11\x15\x19')) #set gyro to normal 
       self.Device.write8(0x7E,0x11)#write to gyro
       self.Device.write8(0x7E,0x15) #write to accel
       time.sleep(0.1) #sensor need 100ms to initialize with Bmm150 (see page
      
       
       """
        step2:set the acc and gyro range
        configuration:
             Acc Range
               0x03 acceleration range: ±2g (default if we don't set)
               0x05 acceleration range: ±4g 
               0x08 acceleration range: ±8g
               0x0C acceleration range: ±16g
            Gyro Range
               0x00 ±2000d/s (default if we don't set)
               0x01 ±1000d/s 
               0x0A ±500d/s
               0x0B ±250d/s
               0x64 ±125d/s
       """
       #Device.write8(0x41,0x03)#0x41=acc conf address, setting acc range to support +-2sg 
       #Device.write8(0x43,0x01) #setting gyro range to support +-1000degree/second
     

    def getSensors(self):
      gyro_x = self.Device.readU8(0x0C)  #read byte data function like c=  i2c_read_byte (0x0C) & 0xFF);
      gyro_x = gyro_x | (self.Device.readU8(0x0D) <<8)
     
      gyro_y = self.Device.readU8(0x0E)  #read byte data function like c=  i2c_read_byte (0x0C) & 0xFF);
      gyro_y = gyro_y | (self.Device.readU8(0x0F) <<8)
      
      gyro_z = self.Device.readU8(0x10)  #read byte data function like c=  i2c_read_byte (0x0C) & 0xFF);
      gyro_z = gyro_z | (self.Device.readU8(0x11) <<8)


      if (gyro_x >0x7FFF):
          gyro_x =- (0x7FFF-gyro_x)

      if (gyro_y >0x7FFF):
          gyro_y =- (0x7FFF-gyro_y)
     
      if (gyro_z >0x7FFF):
          gyro_z =- (0x7FFF-gyro_z)
     

      gyro_x = (gyro_x*2000)/0x7FFF #when range is 2000dps
      gyro_y = (gyro_y*2000)/0x7FFF #when range is 2000dps
      gyro_z = (gyro_z*2000)/0x7FFF #when range is 2000dps


      acc_x =self.Device.readU8(0x12) 
      acc_x = acc_x | ( self.Device.readU8(0x13)<<8)

      acc_y =self.Device.readU8(0x14) 
      acc_y = acc_y | ( self.Device.readU8(0x15)<<8)
      acc_z =self.Device.readU8(0x16) 
      acc_z = acc_z | ( self.Device.readU8(0x17)<<8)
      
      if(acc_x>0x7fff) :
        acc_x = -(0xffff- acc_x); 

      if(acc_y>0x7fff) :
        acc_y = -(0xffff- acc_y); 

      if(acc_z>0x7fff) :
         acc_z = -(0xffff- acc_z); 
      
         
      acc_x = (acc_x*9.8 ) / (0x8000/2) # When the range is ± 2g, the conversion formula for conversion to g / s is 
      acc_y = (acc_y*9.8 ) / (0x8000/2) # When the range is ± 2g, the conversion formula for conversion to g / s is 
      acc_z = (acc_z*9.8 ) / (0x8000/2) # When the range is ± 2g, the conversion formula for conversion to g / s is 
      
      print("Gyro X: {0} | Y: {1} | Z: {2} :".format(gyro_x,gyro_y,gyro_z))
      print("Accel X: {0} | Y: {1} | Z: {2} :".format(acc_x,acc_y,acc_z))
      return {"gyro_x":gyro_x, "gyro_y":gyro_y,"gyro_z":gyro_z,"acc_x":acc_x,"acc_y":acc_y,"acc_z":acc_z}


      def check(axisValue):
          if(axisValue >0x7FFF):
              return -(0xFFF-axisValue)
          return axisValue