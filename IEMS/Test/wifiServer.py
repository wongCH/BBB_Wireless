import socket
import select
from threading import Thread
import time
import json
import random

class WifiConnServer:
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 10000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(1)

    def listen_for_clients(self):
        print('Listening...')
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
        data = {"deviceId":"len_123456","created":None,"lux":0,"tem":0,"hum":0,"pre":0,"gyr": {"x":0,"y":0,"z":0},"acc":{"x":0,"y":0,"z":0}}
        while not stop:
            try:

                data["created"] = int(time.time() * 1000)
                data["lux"] = random.randint(1, 100)
                data["tem"] = random.randint(1, 100)
                data["hum"] = random.randint(1, 100)
                data["pre"] = random.randint(1, 100)
                data["gyr"]["x"] = random.randint(1, 100)
                data["gyr"]["y"] = random.randint(1, 100)
                data["gyr"]["z"] = random.randint(1, 100)
                data["acc"]["x"] = random.randint(1, 100)
                data["acc"]["y"] = random.randint(1, 100)
                data["acc"]["z"] = random.randint(1, 100)

                print("enter loop")
                message =  json.dumps(data, separators=(',',': '))
                print('------------')
                print(message)
                print (str.encode(message))
                client_socket.send(str.encode(message))
                
                time.sleep(1)

            except socket.error:
                client_socket.close()
                print('Client exit')
                return False
        client_socket.close()


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 10000
    maxConnections = 1
    main = WifiConnServer()
    # start listening for clients
    main.listen_for_clients()