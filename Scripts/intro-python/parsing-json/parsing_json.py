#!/usr/bin/env python
"""Parsing structured JSON text into native Python data structures...

...and how to access and work with nested data.
"""


import json
import os
from pprint import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


# Read in the JSON text
with open(os.path.join(here, "interface-config.json")) as file:
    json_text = file.read()


# Display the type and contents of the json_text variable
print("json_text is a", type(json_text))
print(json_text)


# Use the json module to parse the JSON string into native Python data
json_data = json.loads(json_text)


# Display the type and contents of the json_data variable
print("json_data is a", type(json_data))
pprint(json_data)



print()
print ("-"*50)
pprint(json_data["ietf-interfaces:interface"])
print()
print ("-"*50)
pprint(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"])
print()
print ("-"*50)
pprint(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"])
print()
print ("-"*50)
pprint(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0])
print()
print ("-"*50)
pprint(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])
print()
print("Teste de interacao leitura de item em lista e dicionario")
print ("="*60)
my_list = [0, 1, 2, 3, 4]
for it in my_list:
    print (f"- {it} -",end='')

print()
print ("-"*50)

fruit_inventory = {"apples": 5, "pears": 2, "oranges": 9}
for frutas, qtd in fruit_inventory.items():
    print (f"Voce tem {qtd} - {frutas}")

print()
print("=" * 60)

ietf = json_data["ietf-interfaces:interface"]
print (f'Somente ietf name --> {ietf["name"]}\n')


for i, inter in ietf.items():
#    if i == 'name':
       print(f'{i} = {inter}')

print()
print("=" * 60)
print("Fim")