# import bluetooth
# import sys
# import time
# name='DESKTOP-FO1D13O'#'BT'#需连接的设备名字
# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print(nearby_devices)#附近所有可连的蓝牙设备
#
# addr=None
# for device in nearby_devices:
#     if name==device[1]:
#         addr = device[0]
#         print("device found!",name," address is: ",addr)
#         break
# if addr==None:
#     print("device not exist")
# services = bluetooth.find_service(address=addr)
# print(services)
# for svc in services:
#     print("Service Name: %s"    % svc["name"])
#     print("    Host:        %s" % svc["host"])
#     print("    Description: %s" % svc["description"])
#     print("    Provided By: %s" % svc["provider"])
#     print("    Protocol:    %s" % svc["protocol"])
#     print("    channel/PSM: %s" % svc["port"])
#     print("    svc classes: %s "% svc["service-classes"])
#     print("    profiles:    %s "% svc["profiles"])
#     print("    service id:  %s "% svc["service-id"])	#打印蓝牙设备的各种属性
#
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# '''sock.connect((addr, 2))
# print("连接成功，端口：")'''
# i=0
# while i<255:
#     try:
#         sock.connect((addr, i))
#         print("连接成功，端口：",i)
#         # sock.send("12345")
#         break
#     except Exception as e:
#         print("端口：",i,"连接失败",e)
#         i=i+1							#遍历端口号，进行连接





#server
import time
import sys
import bluetooth

#uuid = "98B97136-36A2-11EA-8467-484D7E99A198"
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print(nearby_devices)
uuid = "00001101-0000-1000-8000-00805f9b34fb"
service_matches = bluetooth.find_service( uuid = uuid )
if len(service_matches) == 0:
    print("couldn't find the FooBar service")
    sys.exit(0)

first_match = service_matches[0]
print(first_match)
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
'''sock.connect((addr, port))
print("连接成功")'''
sock.connect((host, port))
print("连接成功")
while True:								#进入循环，不然通讯会自动关闭
	sock.send("12345".encode('utf-8'))
	sock.send("hello".encode('utf-8'))
	data=sock.recv(1024)				#1024为数据长度
	print("received:%s",data)
	time.sleep(5)

#client
