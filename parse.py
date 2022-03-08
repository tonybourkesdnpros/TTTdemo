#!/usr/bin/python3

import json

file = open('interfaces.json', 'r')

thing = json.load(file)


# print(thing['interfaces']['Ethernet2']['interfaceAddress']['ipAddr']['address'])

for interface in thing['interfaces']:
    print("The IP address of", interface, "is", thing['interfaces'][interface]['interfaceAddress']['ipAddr']['address'])

