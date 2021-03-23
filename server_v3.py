from threading import Thread

from bluetooth import *
import sys
uuid = "00001101-0000-1000-8000-00805F9B34FB"
def serverListen(uuid = uuid):
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(5)

    dataport = server_sock.getsockname()[1]
    clientID = 0
    advertise_service(server_sock, "SampleServer",
                      service_id=uuid,
                      service_classes=[uuid, SERIAL_PORT_CLASS],
                      profiles=[SERIAL_PORT_PROFILE],
                      #                   protocols = [ OBEX_UUID ]
                      )

    print("Waiting for connection on RFCOMM channel %d" % dataport)
    while True:
        client_sock, client_info = server_sock.accept()
        clientThread = Thread(target = clientHandler , args = (clientID, client_sock,dataport))
        print("Accepted connection from ", client_info)
        clientThread.start()
        dataport += 1
        clientID += 1
def clientHandler(clientID, client_sock,dataport):
    try:
        while True:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("received from :[%s]" % data)
            client_sock.send("from server")
    except IOError:
        pass

    print("disconnected")
    client_sock.close()
    # server_sock.close()

def main():
    serverListen()
if __name__ == '__main__':
    main()
    