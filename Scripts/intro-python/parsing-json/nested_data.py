#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""

import json
import os
from pprint import pprint

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Analise o conteúdo do arquivo JSON em uma variável





    json_txt = file.read()
    json_data = json.loads(json_txt)
    print("=" * 90)
    print("Geral")
    print("=" * 90)
    pprint(json_data)
    print("=" * 90)
    print("ietf-interfaces:interfaces")
    print("=" * 90)
    pprint(json_data['ietf-interfaces:interfaces'])

    # TODO: Loop through the interfaces in the JSON data and print out each
    # interface's name, ip, and netmask.

    print("=" * 90)
    print("-------- VARREDURA EM TODO O ARQUIVO JASON ---------")
    print("=" * 90)


    # ietf = json_data["ietf-interfaces:interface"]
    # print(f'Somente ietf name --> {ietf["name"]}\n')
    print("=" * 90)
    print("interface")
    print("=" * 90)
    pprint(json_data['ietf-interfaces:interfaces']['interface'])
    print("-" * 90)
    print("Dentro de cada interface")
    interfaces = json_data['ietf-interfaces:interfaces']['interface']
    print("-" * 90)

    for c in range(len(interfaces)):
        print(f'  ------ Interface {c} ------')
        interno = json_data['ietf-interfaces:interfaces']['interface'][c]
        for int, valor in interno.items():
            print(int, valor)
            if type(valor) == dict and len(valor) > 0:
                print(f'  ------ Dentro {int} ------')
                int_ietf = json_data['ietf-interfaces:interfaces']['interface'][c][int]['address'][0]
                for ietf, v_ietf in int_ietf.items():
                    print(f'{v_ietf} ',end='')

                print(f'\n  --------------------------------')

    print("=" * 90)
    print("=" * 90)
    print("-------- INICIO DO EXERCICO COMO FOI PEDIDO O ENUNCIADO ---------")
    print("=" * 90)

    interfaces = json_data['ietf-interfaces:interfaces']['interface']

    for c in range(len(interfaces)):
        print(f'  ------ Interface {c} ------')
        interno = json_data['ietf-interfaces:interfaces']['interface'][c]
        for int, valor in interno.items():
            if int == 'name': print(f'{valor}: ',end='')
            if type(valor) == dict and len(valor) > 0:
                # print(f'  ------ Dentro {int} ------')
                int_ietf = json_data['ietf-interfaces:interfaces']['interface'][c][int]['address'][0]
                for ietf, v_ietf in int_ietf.items():
                    print(f'{v_ietf} ',end='')

                print(f'\n  --------------------------------')