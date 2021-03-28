from bluetooth import *
import sys
#android有关bluetooth的API，用于普通蓝牙适配器和android手机蓝牙模块连接的，而且这个UUID的值必须是00001101-0000-1000-8000-00805F9B34FB。

addr = "D0:57:7B:80:C1:A8"
uuid = "e36b2853-e511-4389-b83d-c2928dfc7d82"
# nearby_devices = discover_devices(lookup_names=True)
# print(nearby_devices)#附近所有可连的蓝牙设备
# uuid = "00001101-0000-1000-8000-00805F9B34FB"
# search for the SampleServer service
# service_matches = find_service(uuid = addr )
#
# if len(service_matches) == 0:
#     print("couldn't find the SampleServer service =(")
#     sys.exit(0)

# Create the client socket
sock=BluetoothSocket(RFCOMM)
advertise_service(sock,"client",service_id=uuid,
                  service_classes=[uuid, SERIAL_PORT_CLASS],
                  profiles=[SERIAL_PORT_PROFILE],
                  )
sock.connect((addr,4))
print("ready to connect")
# try:
#     while True:
#         data = sock.recv(1024)
#         if len(data) == 0: break
#         print("received [%s]" % data)
# except IOError:
#     sock.close()
#     print("disconnected")
#send
try:
    while True:
        data = "client"
        if not data : break
        sock.send(data)
        re_data = sock.recv(1024)
        if re_data:
            print("received: %s" % re_data.decode('utf-8'))
except IOError:
    sock.close()
    print("disconnected")
sock.close()
# import bluetooth
# from bluetooth.btcommon import BluetoothError
# import time
#
# class DeviceConnector:
#     TARGET_NAME =  "DESKTOP-55TDMGV"
#     TARGET_ADDRESS = None
#     TARGET_PORT = 1
#     SOCKET = None
#
#     def __init__(self):
#         pass
#
#     def getConnectionInstance(self):
#         self.deviceDiscovery()
#         if(DeviceConnector.TARGET_ADDRESS is not None):
#             print('Device found!')
#             self.connect_bluetooth_addr()
#             return DeviceConnector.SOCKET
#         else:
#             print('Could not find target bluetooth device nearby')
#
#     def deviceDiscovery(self):
#         tries=0
#         try:
#             nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)
#             while nearby_devices.__len__() == 0 and tries < 3:   #多次
#                 nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)  ##查找。名称可见
#                 tries += 1
#                 time.sleep (2)
#                 print ('couldn\'t connect! trying again...')
#             for bdaddr, name in nearby_devices:
#                 print(bdaddr,name)
#             for bdaddr, name in nearby_devices:
#                 if bdaddr and name == DeviceConnector.TARGET_NAME:  ##查找目标
#                     DeviceConnector.TARGET_ADDRESS = bdaddr
#                     # DeviceConnector.TARGET_NAME = name
#         except BluetoothError as e:
#             print ('bluetooth is off')
#
#     def connect_bluetooth_addr(self):
#         for i in range(1,5):
#             time.sleep(1)
#             sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  #服务器协议选择
#             try:
#                 sock.connect((DeviceConnector.TARGET_ADDRESS, 4)) # DeviceConnector.TARGET_PORT #连接目标
#                 sock.setblocking(False)  #阻塞
#                 data = '12345'
#                 sock.send( data.encode('utf-8') )
#                 DeviceConnector.SOCKET = sock
#                 print('it has connected a device successfully')
#                 return
#             except BluetoothError as e:
#                 print('Could not connect to the device')
#                 DeviceConnector.SOCKET.close()
#         return None
#
#     def createService(self,way=bluetooth.RFCOMM):
#         server_sock = bluetooth.BluetoothSocket(way)  ## bluetooth.L2CAP     ## RFCOMM    ##
#         server_sock.bind(('', 4))
#         server_sock.listen(2)   #监听
#         print('开始监听....................')
#         while True:
#             client_sock, address = server_sock.accept()  # 接受请求
#             print("Accepted connection from ", address)
#             while True:
#                 data = client_sock.recv(5)#等待接受数据。 数据长度为1（这个根据自己的情况任意改，只有接受够这么多长度的数据，才会结束这个语句）
#                 if not data:
#                     break
#                 client_sock.send(data) # 数据返回
#                 print("received [%s]" % data.decode('utf-8') )
#             client_sock.close()  #连接关闭
#             server_sock.close()
#
# bluez = DeviceConnector()
# # bluez.getConnectionInstance()
# bluez.createService()
