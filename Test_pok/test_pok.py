
import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'efddae437575ab83b5c29b06f130f98b'
HEADER = {'content_Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '27268'
def test_status_code():
    responce = requests.get(url=f'{URL}/trainers',params= {'trainer_id':TRAINER_ID})
    assert responce.status_code == 200 

def test_trainer_id():
    responce_get = requests.get(url=f'{URL}/trainers',params= {'trainer_id':TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == 'Smollvile'

