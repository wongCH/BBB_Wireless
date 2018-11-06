using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Text;

namespace IEMS.Mobile.Models
{
    public class SensorItem : INotifyPropertyChanged
    {
        public SensorItem() {

        }
        private string deviceId;
        public string DeviceId
        {
            get { return deviceId; }
            set
            {
                deviceId = value;
                OnPropertyChanged("DeviceId");
            }
        }
        private Int64 created;
        public Int64 Created {
            get { return created; }
            set {
                created = value;
                OnPropertyChanged("Created");
            }
        }

        private Int32 lux;
        public Int32 Lux { get { return lux; }
            set {
                lux = value;
                OnPropertyChanged("Lux");
            }
        }

        private Int32 tem;
        public Int32 Tem { get {
                return tem;
            }
            set {
                tem = value;
                OnPropertyChanged("Tem");
            }
        }

        private Int32 hum;
        public Int32 Hum { get { return hum; } set {
                hum = value;
                OnPropertyChanged("Hum");
            } }

        private Int32 pre;
        public Int32 Pre
        {
            get { return pre; }
            set
            {
                pre = value;
                OnPropertyChanged("Pre");
            }
        }

        [JsonIgnore]
        public Int32 ACC_X {
            get;set;
        }
        [JsonIgnore]
        public Int32 ACC_Y
        {
            get; set;
        }
        [JsonIgnore]
        public Int32 ACC_Z
        {
            get; set;
        }
        [JsonIgnore]
        public Int32 GYR_X { get; set; }
        [JsonIgnore]
        public Int32 GYR_Y { get; set; }
        [JsonIgnore]
        public Int32 GYR_Z { get; set; }

        private Gyro gyr;
        public Gyro Gyr {
            get
            {
               
                return gyr;
            }
            set {
                gyr = value;
                this.GYR_X = value.X;
                this.GYR_Y = value.Y;
                this.GYR_Z = value.Z;
                OnPropertyChanged("Gyr");
            }
        }

        private Acce acc;

      
        public Acce Acc {
            get
            {
 
                return acc;
            }
            set {
                acc = value;
                this.ACC_X = value.X;
                this.ACC_Y = value.Y;
                this.ACC_Z = value.Z;

                OnPropertyChanged("Acc");
            } }

        public event PropertyChangedEventHandler PropertyChanged;

      
        private void OnPropertyChanged(string propertyName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
        }
    }

    public class Gyro: INotifyPropertyChanged
    {

        public event PropertyChangedEventHandler PropertyChanged;

        private void OnPropertyChanged(string propertyName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
        }

        private Int32 x;
        public Int32 X {
            get { return x; }
            set {
                x =value;
                OnPropertyChanged("Gyro.X");
            }
        }

        private Int32 y;
        public Int32 Y {
            get { return y; }
            set {
                y = value;
                OnPropertyChanged("Gyro.Y");
            }
        }

        private Int32 z;
        public Int32 Z {
            get { return z; }
            set {
                z = value;
                OnPropertyChanged("Gyro.Z");
            }
        }
    }

    public class Acce : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;

        private void OnPropertyChanged(string propertyName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
        }

        private Int32 x;
        public Int32 X {
            get {
                return x;
            }
            set {
                x = value;
                OnPropertyChanged("Acc.X");
            }
        }

        private Int32 y;
        public Int32 Y {
            get {
                return y;
            }
            set {
                y = value;
                OnPropertyChanged("Acc.Y");
            }
        }
        private Int32 z;
        public Int32 Z {
            get {
                return z;
            }
            set {
                z = value;
                OnPropertyChanged("Acc.Z");
            }
        }
    }
}
