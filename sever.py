# from bluetooth import *
#
# server_sock = BluetoothSocket(RFCOMM)
# server_sock.bind(("", PORT_ANY))
# server_sock.listen(1)
#
# port = server_sock.getsockname()[1]
#
# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#
# advertise_service(server_sock, "SampleServer",
#                   service_id=uuid,
#                   service_classes=[uuid, SERIAL_PORT_CLASS],
#                   profiles=[SERIAL_PORT_PROFILE],
#                   #                   protocols = [ OBEX_UUID ]
#                   )
#
# print("Waiting for connection on RFCOMM channel %d" % port)
#
# client_sock, client_info = server_sock.accept()
# print("Accepted connection from ", client_info)
#
#
# #receive
# # try:
# #     while True:
# #         data = client_sock.recv(1024)
# #         if len(data) == 0: break
# #         print("received [%s]" % data)
# # except IOError:
# #     pass
# #print("disconnected")
#
# #send
# while True:
#     data = input()
#     if len(data) == 0: break
#     sock.send(data)
#
# client_sock.close()
# server_sock.close()
import bluetooth
from bluetooth.btcommon import BluetoothError
import time

class DeviceConnector:
    TARGET_NAME = "DESKTOP-55TDMGV"
    TARGET_ADDRESS = None
    TARGET_PORT = 4
    SOCKET = None

    def __init__(self):
        pass

    def getConnectionInstance(self):
        self.deviceDiscovery()
        if(DeviceConnector.TARGET_ADDRESS is not None):
            print('Device found!')
            self.connect_bluetooth_addr()
            return DeviceConnector.SOCKET
        else:
            print('Could not find target bluetooth device nearby')

    def deviceDiscovery(self):
        tries=0
        try:
            nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)
            while nearby_devices.__len__() == 0 and tries < 3:   #多次
                nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)  ##查找。名称可见
                tries += 1
                time.sleep (2)
                print ('couldn\'t connect! trying again...')
            for bdaddr, name in nearby_devices:
                print(bdaddr,name)
            for bdaddr, name in nearby_devices:
                if bdaddr and name == DeviceConnector.TARGET_NAME:  ##查找目标
                    DeviceConnector.TARGET_ADDRESS = bdaddr
                    # DeviceConnector.TARGET_NAME = name
        except BluetoothError as e:
            print ('bluetooth is off')

    def connect_bluetooth_addr(self):
        for i in range(1,5):
            time.sleep(1)
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  #服务器协议选择
            try:
                sock.connect((DeviceConnector.TARGET_ADDRESS, 1)) # DeviceConnector.TARGET_PORT #连接目标
                sock.setblocking(False)  #阻塞
                data = '12345'
                sock.send( data.encode('utf-8') )
                DeviceConnector.SOCKET = sock
                print('it has connected a device successfully')
                return
            except BluetoothError as e:
                print('Could not connect to the device')
                DeviceConnector.SOCKET.close()
        return None

    def createService(self,way=bluetooth.RFCOMM):
        server_sock = bluetooth.BluetoothSocket(way)  ## bluetooth.L2CAP     ## RFCOMM    ##
        server_sock.bind(('', 4))
        server_sock.listen(2)   #监听
        print('开始监听....................')
        try:
            while True:
                client_sock, address = server_sock.accept()  # 接受请求
                print("Accepted connection from ", address)
                while True:
                    data = client_sock.recv(1024)#等待接受数据。 数据长度为1（这个根据自己的情况任意改，只有接受够这么多长度的数据，才会结束这个语句）
                    if not data:
                        break
                    client_sock.send("server") # 数据返回
                    print("received [%s]" % data.decode('utf-8') )
        except IOError:
            pass
        client_sock.close()  #连接关闭
        server_sock.close()

bluez = DeviceConnector()
bluez.getConnectionInstance()
bluez.createService()

