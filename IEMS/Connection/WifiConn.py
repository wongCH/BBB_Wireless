import time
import socket
import select

class WifiConn(object):
    """description of class"""

HOST='beaglebone.local'
PORT=5002

def EstablishConn():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr=s.accept()
    strMessage ="Test"
    byteMessage =strMessage.encode()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    print ('Connected by', addr)

    while True:
        try:
            ready_to_read, ready_to_write, in_error = \
            select.select([conn,], [conn,], [], 5)
            #conn.send(byteMessage)
            #time.sleep(2)
        except select.error:
            conn.shutdown(2) #0 =done receiving, 1=done sending, 2=both
            conn.close()
            print ("Connection broken")
            break

        if len(ready_to_read) > 0:
            recv = conn.recv(2048)
            print (recv)
            # do stuff with received data
            print ('received:'+ recv)
        if len(ready_to_write) > 0:
        # connection established, send some stuff
           conn.send('some stuff'.encode())
    s.close()