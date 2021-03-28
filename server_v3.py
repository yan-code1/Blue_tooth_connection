from threading import Thread

import bluetooth
import sys
uuid = "e36b2853-e511-4389-b83d-c2928dfc7d82"
def serverListen(uuid = uuid):
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(5)

    dataport = server_sock.getsockname()[1]
    clientID = 0
    bluetooth.advertise_service(server_sock, "SampleServer",
                      service_id=uuid,
                      service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                      profiles=[bluetooth.SERIAL_PORT_PROFILE],
                      #                   protocols = [ OBEX_UUID ]
                      )
    # services = bluetooth.find_service(uuid=uuid)
    # addr = services[0]["host"]
    #
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
    