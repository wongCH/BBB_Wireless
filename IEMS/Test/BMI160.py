
import Adafruit_GPIO.I2C as I2C
import time
class BMI160(object):
    """
     BM160 focusing on Gyro and accel using all default value
          Reading from IMU
           I2C address= 0x69
           busNum=2
           bitSize = 2 (7bit)
    --------------------------------------------------------------
    Important Register:
       Chip ID Register: CHIPID register, value 0xd1 
       0x03: pmu_status--- BMI160 current working mode/status register 

        Accelerometer field data 
        X-axis 16bit acceleration data 
         0x12: ACCD_X_LSB acc_x_lsb [7:0] bit0--bit7 
         0x13: ACCD_X_MSB acc_x_msb[15:8] bit0--bit7

        Y-axis 16-bit acceleration data 
         0x14: ACCD_Y_LSB acc_y_lsb[7:0] bit0--bit7 
         0x15: ACCD_Y_MSB acc_y_msb[15:8] bit0 --bit7 

        Z-axis 16-bit acceleration data 
         0x16: ACCD_Z_LSB acc_z_lsb[7:0] bit0--bit7 
         0x17: ACCD_Z_MSB acc_z_msb[15:8] bit0--bit7 

       Acceleration range configuration register 0x41: ACC_RANGE 
         0B0011: +-2G RANGE; 0b0101+-4g; 0b1000: +-8g; 0b1100: +-16g 
    
     Control register 0x7e 
        0x11: set pmu mode of accelerometer to normal  (0x11-0x12)
        0x15:set pmu mode of gyroscope to normal (0x15 or 0x17)
        0x18: set pmu mode of magnetometer to normal (0x18-0x1B)

    Gyro angular velocity data gyroscope field data 
        X-axis angular velocity data 16 BIT ( LSB/°/s) 
         0x0c:gyr_x_lsb[7:0] bit0--bit7 
         0x0d:gyr_x_msb[15:8] bit0--bit7 

        Y-axis angular velocity data 16 BIT(LSB/°/s) 
         0x0e:gyr_y_lsb[7:0 ] bit0--bit7
         0x0f:gyr_y_msb[15:8] bit0--bit7 

        Z-axis angular velocity data 16 BIT(LSB/°/s) 
         0x10:gyr_z_lsb[7:0] bit0--bit7 
         0x11:gyr_z_msb[15:8] bit0--bit7 

         Acceleration range configuration register r0x41: ACC_RANGE 
         0B0011: +-2G RANGE; 0b0101+-4g; 0b1000: +-8g; 0b1100: +-16g 

                      
        It is recommended that the acceleration and gyro modules use the system default reference configuration 
           0x41(acc_range):0x03 (default value) : acceleration range ±2g 
           0x40(acc_conf): 0x28 (default value)
                
           0x42(gyro_config):0x28  (default value)
           0x43(gyro_range):0x00 (default)angular velocity ±2000°/ s 

      * Burst Read(0x24 - FIFO_DATA) :only support for all normal mode
    """
    
    def __init__(self):
        #step 1: set cmd for both accel and gyro
        self.Device = I2C.Device(address=0x69,busnum=2) #i2c address and busNum in BB
        #self.Device.writeList(0x7E,bytearray(b'\x11\x15\x19')) #\x19 set gyro to normal 
        self.Device.write8(0x7E,0x11)#write to gyro
        self.Device.write8(0x7E,0x15) #write to accel
        time.sleep(0.1) #sensor need time of 100ms to set
        #print("PMU status: {0}".format(self.Device.readList(0x03,3)))

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

        meg_x =self.Device.readU8(0x12) 
        meg_x = meg_x | ( self.Device.readU8(0x13)<<8)
        #print (self.Device.readList(0x24,2))
        #print ("MAG_IF_0:{0}".format(self.Device.readU8(0x4B)))
        #print (self.Device.readU8(0x4C))
        #print (self.Device.readU8(0x4D))
        #print (self.Device.readU8(0x4E))
        #print (self.Device.readU8(0x4F))
       
