#!/usr/bin/env python
from netmiko import Netmiko

# Sending device ip's stored in a file 
with open('devices_list') as f:
    devices_list = f.read().splitlines()

# Iterate through device list and configure the devices 
for devices in devices_list:
    print 'Connecting to device ' + devices
    ip_address_of_device = devices
    
    # SSH Connection details 
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': 'cisco',
        'password': 'cisco'
    }
 
    net_connect = Netmiko(**ios_device)
    output = net_connect.send_config_from_file('reset_config')
    print (output)