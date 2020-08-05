#!/usr/bin/python3
from netmiko import ConnectHandler

#Cisco_vios = {'device_type': 'cisco_ios','ip': '192.168.96.34','username': 'cisco','password': 'Cisco123'}
Cisco_vios = {
'device_type': 'cisco_ios',
'ip': '192.168.96.34',
'username': 'cisco',
'password': 'Cisco123'
}

x = ConnectHandler(**Cisco_vios)

out_1 = x.send_command('show run | inc hostname')
out_1 = out_1[9:]
print (out_1)

out_2 = x.send_command('show ip int brief')

with open((out_1+".txt"),"w+") as File:
    File.write(out_2)
