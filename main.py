import requests 
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'efddae437575ab83b5c29b06f130f98b'
HEADER = {'content_Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "shamahin",
    "photo_id": 4
}

body_redact = {
    "pokemon_id": "271573",
    "name": "dvor0ecki",
    "photo_id": 2
}
body_in_pok ={
    "pokemon_id": "271573"
}

'''responce_create = requests.post(url=f'{URL}/pokemons',headers=HEADER,json = body_create)
print(responce_create.json())
pokemon_id = responce_create.json()['id']
print(pokemon_id)'''

'''responce_redact = requests.patch(url=f'{URL}/pokemons',headers=HEADER,json = body_redact)
print(responce_redact.json())
pokemon_id = responce_redact.json()
print(pokemon_id)'''
 

responce_in_pok = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json = body_in_pok)
print(responce_in_pok.json())
pokemon_id = responce_in_pok.json()['id']
print(pokemon_id)