import bluetooth
import threading


server_socket=None
def serveSocket(sock,info):
    while True:
        receive=sock.recv(1024).decode('utf-8')
        print('['+str(info)+']'+receive)
        receive=receive+"\n"
        sock.send("FROM BBBBL:"+receive.encode('utf-8'))

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("",1))
server_socket.listen(1)
while True:
    sock,info=server_socket.accept()
    print(str(info[0])+'Connected!')
    t=threading.Thread(target=serveSocket,args=(sock,info[0]))
    t.setDaemon(True)
    t.start()
