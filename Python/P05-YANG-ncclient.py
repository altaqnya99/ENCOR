from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='192.168.96.34', port=830, username='cisco',
                    password='Cisco123', device_params={'name': 'csr'})

for c in m.server_capabilities:
    print (c)

####################


schema = m.get_schema('ietf-ip')
print (schema)

####################


running_config = m.get_config('running')
print (running_config)

####################

Pretty_filter = '''
                <filter>
                    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    </native>
                </filter>
                '''

xmlDom = xml.dom.minidom.parseString( str( m.get_config('running', Pretty_filter)))
print(xmlDom.toprettyxml( indent = "  " ))
