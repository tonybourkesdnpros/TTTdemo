#!/usr/bin/python3

#### Variables (Simple and complex)

### Simples Variables

import yaml

i = 1  # This is an integer

x = "Hello" # This is a string
y = "world!"
z = x + " " + y

event = True # This is a boolean

### Complex Variables (dictionaries, lists)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranaus', 'Neptune'] # This is a list

captains = {'1701': 'Kirk', 
            '1701-D': 'Picard', 
            '74656': 'Janeway', 
            '1864': 'Khan'}

# for key, value in captains.items():
#     print(key, value)


#### Load YAML into dictionary
    
file = open('underlay.yml', 'r')

underlay = yaml.safe_load(file)

for switch in underlay:
    print(switch)
    for interface in underlay[switch]['interfaces']:
        print("  ", interface)