import socket
import select
from threading import Thread
import time
from Helpers.Constant import *
class WifiConnServer:
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 9999
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(1)

    def listen_for_clients(self):
        print('Listening on'+ self.host +' at port' + self.port)
        while True:
            client, addr = self.server.accept()
            print(
                'Accepted Connection from: ' + str(addr[0]) + ':' + str(addr[1])
            )
            thrNewJob = Thread(target=self.handle_client, args=(client, addr))
            thrNewJob.start()

    def handle_client(self, client_socket, address):
        size = 1024
        stop = False
        
        while not stop:
            try:
                print("enter loop")
                client_socket.send(str.encode(Constant.STR_JSON_DATA))
                time.sleep(1)

            except socket.error:
                client_socket.close()
                print('Client disconnectd.Close client connection.')
                return False
        client_socket.close()


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 10000
    maxConnections = 1
    main = WifiConnServer(host, port)
    # start listening for clients
    main.listen_for_clients()