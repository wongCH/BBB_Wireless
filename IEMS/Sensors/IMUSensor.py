
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
       Device = I2C.Device(address=0x69,busnum=2) #i2c address and busNum in BBB
       Device.write8(0x7E,0x11) #waking up the sensor and set it to Normal Mode
       Device.write8(0x7E,0x15) #waking up gyro set to normal mode
       Device.write8(0x7E,0x19) #waking up magnetometer to normal mode
       #Device.writeList(0x73,bytearray(b'\0x11\0x15\0x19'))
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
       Device.write16(0x41,0x03)#0x41=acc conf address, setting acc range to support +-2sg 
       Device.write16(0x43,0x01) #setting gyro range to support +-1000degree/second
     

   
     
      
    def getSensors(self):
      device = I2C.get_i2c_device(0x69,2)
      ##reading all the register for gyro and acc#####
      acc_x = (device.readS16(0x12) | device.readS16(0x13) << 8)
      acc_y = (device.readS16(0x14) | device.readS16(0x15) << 8)
      acc_z = (device.readS16(0x16) | device.readS16(0x17) << 8)

      gyr_x = (device.readS16(0x0C) | device.readS16(0x0d) << 8)
      gyr_y = (device.readS16(0x0E) | device.readS16(0x0f) << 8)
      gyr_z = (device.readS16(0x10) | device.readS16(0x11) << 8)
      
      mag_x = (device.readS16(0x04) | device.readS16(0x05) << 8)
      mag_y = (device.readS16(0x06) | device.readS16(0x07) << 8)
      mag_z = (device.readS16(0x08) | device.readS16(0x09) << 8)
      
      #print("Before: ac_x: {0} | ac_y: {1} | ac_z: {2}".format(acc_x,acc_y, acc_z))
      #print("Before: gyr_x: {0} | gyr_y: {1} | gyr_z: {2}".format(acc_x,acc_y, acc_z))
      acc_x = (acc_x*9.8 ) / (0x8000/2) # When the range is ± 2g, the conversion formula for conversion to g / s is 
      acc_y = (acc_y*9.8)/(0x8000/2) # The acceleration is converted to g/s when the range is ±2g The conversion formula 
      acc_z = (acc_z*9.8)/(0x8000/2) #  When the range is ±2g, the conversion formula for conversion to g/s is 
      print("After: ac_x: {0} | ac_y: {1} | ac_z: {2}".format(acc_x,acc_y, acc_z))
      print("After gyr_x: {0} | gyr_y: {1} | gyr_z: {2}".format(gyr_x,gyr_y, gyr_z))
      print("After Mag: {0} | Mag_y: {1} | Mag_z: {2}".format(mag_x,mag_y, mag_z))
      print("#######################################################################################")
      """
      #loop through all the register address to get the data of x,y,z axis for acc n gyro
         #Acceleration conversion formula converted to g/s when the range is ±2g
      x =( i2c_read_one_byte(0x12) &0xff);  #0x12 = acc_x_7_0
	  x = x|(( i2c_read_one_byte(0x13) &0xff)<<8);   # 0x13=acc_x_15_8
	  acc_x = (signed short)x;
      acc_x = (signed short)(acc_x*9.8)/(0x8000/2);  

      Acceleration Each axis occupies two bytes, so the value read from the sensor needs to be spliced
      according to the high and low bits, and because each axis of the acceleration is directional,
     that is, the value of each axis of the acceleration should be positive. 
      Negative, so the value after splicing forces the type to be " signed short " . 
      After the conversion, we need to convert the converted value into units of acceleration.
     The conversion formula is as follows:
      Acc_x = (signed short)(acc_x*9.8)/(0x8000/2);
      9.8 is the standard gravitational acceleration value; because the default range is ± 2g, 
      difference between the maximum and minimum 4g, and the above equation, 
      we take half the range, i.e. 2g; for " acc_x " 
      corresponding to " Signed Short " range It is " - 32768 ~ +32767 " , 
      the maximum to the minimum is a total of 65536 values, 
      equivalent to 65536 scales, and the same half is 0x8000. 
      The above formula multiplies the value read by the sample by g after the corresponding conversion,
      so that the range of the sampled acquisition value 0x8000 needs to be divided by 2.
      """