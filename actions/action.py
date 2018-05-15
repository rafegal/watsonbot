__author__ = 'galleani'

from .constants import TOKEN_CLIMA_TEMPO
from core.models import Message
import requests
import datetime
import random
import secrets


class Action:
    def __init__(self, user, output):
        self.data = []
        self.output = output
        self.user = user
        self.text = output['output']['text'][0]


    def get_clima(self):
        city = self.output['context']['cidade']
        url_get_city_id = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={city}&token={token}".format(city=city, token=TOKEN_CLIMA_TEMPO)
        response = requests.get(url_get_city_id)
        print(response)
        city_id = response.json()[0]['id']
        url_get_clima = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{city_id}/days/15?token={token}".format(city_id=city_id, token=TOKEN_CLIMA_TEMPO)
        response = requests.get(url_get_clima)
        clima = response.json()['data'][0]['text_icon']['text']['pt']
        url_get_temperatura = "http://apiadvisor.climatempo.com.br//api/v1/forecast/locale/{city_id}/hours/72?token={token}".format(city_id=city_id, token=TOKEN_CLIMA_TEMPO)
        response = requests.get(url_get_temperatura)
        date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:00:00')
        for i in response.json()['data']:
            if date_now == i['date']:
                temperatura = i['temperature']['temperature']
                break
        new_text = self.text.format(clima=clima, temperatura=temperatura)
        return [{'type':'text', 'text':new_text}]


    def get_pokemon(self):
        number = random.randrange(0, 201, 2)
        url_pokemon = "http://pokeapi.co/api/v2/pokemon/{}".format(number)
        response = requests.get(url_pokemon)
        pokemon_name = response.json()['forms'][0]['name']
        pokemon_image_url = response.json()['sprites']['front_default']
        pokemon_image = requests.get(pokemon_image_url).content
        new_text = []
        new_text.append({'type':'text', 'text':self.text.format(pokemon=pokemon_name.title())})
        new_text.append({'type':'image', 'image':pokemon_image})
        return new_text


    def get_url_password(self):
        system = self.output['context']['sistema']
        token = secrets.token_hex(16)
        link = 'http://{0}.devinho.com.br/troca_senha/{1}/{2}'.format(system.lower(), self.user.id, token)
        new_text = [{'type':'text', 'text':self.text.format(link=link)}]
        return new_text


    def get_total_message(self):
        total = Message.objects.count()
        new_text = [{'type':'text', 'text':self.text.format(total=total)}]
        return new_text
