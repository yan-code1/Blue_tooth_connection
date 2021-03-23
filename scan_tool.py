
import bluetooth
import sys
import time
# # search for the SampleServer service
uuid = "00001101-0000-1000-8000-00805F9B34FB"
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print(nearby_devices)#附近所有可连的蓝牙设备


name='DESKTOP-55TDMGV'#'BT'#需连接的设备名字
addr=None
for device in nearby_devices:
    if name==device[1]:
        addr = device[0]
        print("device found!",name," address is: ",addr)
        break
if addr==None:
    print("device not exist")
services = bluetooth.find_service(address=addr)
print(services)
for svc in services:
    print("Service Name: %s"    % svc["name"])
    print("    Host:        %s" % svc["host"])
    print("    Description: %s" % svc["description"])
    print("    Provided By: %s" % svc["provider"])
    print("    Protocol:    %s" % svc["protocol"])
    print("    channel/PSM: %s" % svc["port"])
    print("    svc classes: %s "% svc["service-classes"])
    print("    profiles:    %s "% svc["profiles"])
    print("    service id:  %s "% svc["service-id"])	#打印蓝牙设备的各种属性
