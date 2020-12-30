import requests
from pprint import pprint

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload={}
headers = {
  'Cookie': '__cfduid=d6b94ae52348d2c29d366dc59c803cd421604349060'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

baralho = response.json()
baralho_id = baralho['deck_id']
print (baralho_id)
print ("="*60)
print ()
#=========== 2o teste ===========

url = " https://deckofcardsapi.com/api/deck/new/shuffle/"
querystring = {"deck_count": input("Quantos Baralhos?")}
headers = {
'Cache-Control': "no-cache",
'Postman-Token ': "dd1d8ca5-7000-21b2-2230-39969d585419"
}
response = requests.request ("GET", url, headers = headers, params = querystring)

print (response.text)
deck = response.json ()
deck_id = deck ['deck_id']
pprint (deck_id)

print ("="*60)
print ()

#=========== 3o teste compra carta ===========

#url = "https://deckofcardsapi.com/api/deck/"+deck_id+"/draw//?count=2"
url = "https://deckofcardsapi.com/api/deck/"+deck_id+"/draw/"
Qtas_Cartas = {"count": input("Quantas Cartas vai Comprar?")}
payload={}
headers = {
  'Cookie': '__cfduid=d6b94ae52348d2c29d366dc59c803cd421604349060'
}

# original --> response = requests.request("GET", url, headers=headers, data=payload)
response = requests.request("GET", url, headers=headers, data=payload, params = Qtas_Cartas)
#pprint(response.text)
baralhos = response.json ()
cartas = baralhos ['cards']
cod_carta = cartas[0]
pprint (cartas)
#pprint (cod_carta)

print ()
print ("-----  Cartas sorteadas ------\n")
for c in range(len(cartas)):
  carta = cartas[c]
  print(f"-> Carta {c+1}  é  {cartas[c]['value']} de {cartas[c]['suit']} ")

'''
  print(f"Codigo carta é {carta['code']}")
  
  for i in interno.items():
    if int == 'name': print(f'{valor}: ', end='')
    if type(valor) == dict and len(valor) > 0:
      # print(f'  ------ Dentro {int} ------')
      int_ietf = json_data['ietf-interfaces:interfaces']['interface'][c][int]['address'][0]
      for ietf, v_ietf in int_ietf.items():
        print(f'{v_ietf} ', end='')

      print(f'\n  --------------------------------')
'''