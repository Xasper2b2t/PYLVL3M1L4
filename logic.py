from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, name, image, type_, hp, attack, defense, speed, abilities, pokemon_trainer):
        self.name = name
        self.image = image
        self.type_ = type_
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.abilities = abilities
        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.type_=self.get_type()
        self.hp=self.get_hp()
        self.attack=self.get_attack()
        self.deffense=self.get_deffense()
        self.speed=self.get_speed()
        self.abilities=self.get_abilities()
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json
            return (data["sprites"]["others"]["official_artwork"]["front_default"])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['types'])
        else:
            return "Pikachu"
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats']['stat']['name']['hp'])
        else:
            return "Pikachu"
    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats']['stat']['name']['attack'])
        else:
            return "Pikachu"
    def get_deffense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats']['stat']['name']['deffense'])
        else:
            return "Pikachu"
    def get_speed(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats']['stat']['name']['speed'])
        else:
            return "Pikachu"
    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities']['ability']['name'])
        else:
            return "Pikachu"
    def feed(self):
        self.hp += randint(5, 10)
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"
    def info(self):
        return f"Имя покемона: {self.name}, Уровень: {self.level}, HP: {self.hp}, Атака: {self.attack}, Защита: {self.defense}, Скорость: {self.speed}"
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    



