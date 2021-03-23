from bluetooth import *
import sys
uuid = "00001101-0000-1000-8000-00805F9B34FB"
# # search for the SampleServer service
# service_matches = find_service(uuid = uuid )
# if len(service_matches) == 0:
#     print("couldn't find the SampleServer service =(")
#     sys.exit(0)
# print(service_matches)
#
server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

advertise_service(server_sock, "SampleServer",
                  service_id=uuid,
                  service_classes=[uuid, SERIAL_PORT_CLASS],
                  profiles=[SERIAL_PORT_PROFILE],
                  #                   protocols = [ OBEX_UUID ]
                  )

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
        client_sock.send("from server")
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
