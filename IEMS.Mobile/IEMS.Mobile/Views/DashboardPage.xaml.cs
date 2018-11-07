using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


using System.Net.Sockets;
using System.Net;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using System.IO;
using System.Diagnostics;
using Newtonsoft.Json;
using IEMS.Mobile.Models;
using System.Collections.ObjectModel;
using Telerik.XamarinForms.Chart;

namespace IEMS.Mobile.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class DashboardPage : ContentPage
    {
        public DashboardPage()
        {
            InitializeComponent();
            SensorItems = new ObservableCollection<SensorItem>();

            BindingContext = this;
          
            
        }


        public  void StartClient()
        {
            // Data buffer for incoming data.  
            byte[] bytes = new byte[1024];

            // Connect to a remote device.  
            try
            {
                // Establish the remote endpoint for the socket.  
                // This example uses port 11000 on the local computer.  
                IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
                IPAddress ipAddress = IPAddress.Parse(txtIP.Text); //ipHostInfo.AddressList[0];
                IPEndPoint remoteEP = new IPEndPoint(ipAddress, int.Parse(txtPort.Text));

                // Create a TCP/IP  socket.  
                Socket sender = new Socket(ipAddress.AddressFamily,
                    SocketType.Stream, ProtocolType.Tcp);

                // Connect the socket to the remote endpoint. Catch any errors.  
                try
                {
                    sender.Connect(remoteEP);
                    while (isConnect)
                    {
                        Debug.WriteLine("Socket connected to {0}",
                        sender.RemoteEndPoint.ToString());

                        // Receive the response from the remote device.  
                        int bytesRec = sender.Receive(bytes);
                        var received = Encoding.ASCII.GetString(bytes, 0, bytesRec);
                        Debug.WriteLine("Echoed test = {0}", received);
                        Device.BeginInvokeOnMainThread(() =>
                        {

                            try
                            {
                                SensorItem item = JsonConvert.DeserializeObject<SensorItem>(received);
                                Debug.WriteLine(item.Acc.X);

                                SensorItems.Add(item);
                                lblTemp.Text = item.Tem.ToString();
                                gauIndicatorTemperature.Value = item.Tem;
                                if (SensorItems.Count > 5)
                                    SensorItems.RemoveAt(0);
                            }
                            catch (Exception e) {
                                Debug.WriteLine(e.ToString());
                            }
                        });

                       

                        Debug.WriteLine("Loop Done");
                    } 

                
                    // Release the socket.  
                    sender.Shutdown(SocketShutdown.Both);
                    sender.Close();

                }
                catch (ArgumentNullException ane)
                {
                    Debug.WriteLine("ArgumentNullException : {0}", ane.ToString());
                }
                catch (SocketException se)
                {
                    Debug.WriteLine("SocketException : {0}", se.ToString());
                }
                catch (Exception e)
                {
                    Debug.WriteLine("Unexpected exception : {0}", e.ToString());
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }


        bool isConnect = false;
        private void btnConnect_Clicked(object sender, EventArgs e)
        {
            if (txtIP.Text.Length ==0 || txtPort.Text.Length ==0)
            {
                return;
            }
            Debug.WriteLine("Entering task");
            isConnect = !isConnect;
            if (isConnect) {
                btnConnect.Text = "Disconnect";
                Task.Run(async () =>
                {
                    Debug.WriteLine("In task");

                    StartClient();
                });
            }
            else {
                btnConnect.Text = "Connect";
            }
          
        }
    
        public ObservableCollection<SensorItem> SensorItems {
            get;set;
        }

        private void btnClear_Clicked(object sender, EventArgs e)
        {
            SensorItems.Clear();
        }

       
    }
}