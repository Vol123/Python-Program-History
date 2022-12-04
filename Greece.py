import random
from typing import List, Any


class Gods:
    def __init__(self, name, definition):
        self.name = name
        self.definition = definition


arrNames = []
arrDif = []


def getRandomValue(arr, arrName: True):
    if arrName:
        while True:
            if len(arrNames) == len(arr):
                return
            value = random.randint(0, len(arr) - 1)
            if len(arrNames) == 0:
                arrNames.append(value)
                return value
            exist = False
            for i in range(len(arrNames)):
                if value == arrNames[i]:
                    exist = True
                    break
            if not exist:
                arrNames.append(value)
                return value
    else:
        while True:
            if len(arrDif) == len(arr):
                return
            value = random.randint(0, len(arr) - 1)
            if len(arrDif) == 0:
                arrDif.append(value)
                return value
            exist = False
            for i in range(len(arrDif)):
                if value == arrDif[i]:
                    exist = True
                    break
            if not exist:
                arrDif.append(value)
                return value


gods = [
    Gods('Zeus', 'władca bogów, bóg świata'),
    Gods('Posejdon', 'Władca mórz'),
    Gods('Hades', 'władca świata podziemnego'),
    Gods('Hera', 'opiekunka małżeństw'),
    Gods('Atena', 'boginia mądrości'),
    Gods('Hefajstos', 'bóg kowali i rzemieślników'),
    Gods('Afrodyta', 'boginia piękna i miłości'),
    Gods('Apollo', 'bóg muzyki, prawdy i porządku'),
    Gods('Artemida', 'boginia łowów, przyrody, księżyca'),
    Gods('Hermes', 'bóg handlu'),
    Gods('Ares', 'bóg wojny'),
    Gods('Temida', 'boginia sprawiedliwości'),
    Gods('Nike', 'boginia zwycięstwa'),
    Gods('Dionizos', 'bóg wina'),
    Gods('Persefona(Kora)', 'opiekunka dusz zmarłych'),
    Gods('Pan', 'opiekun lasów i pól'),
    Gods('Nemezis', 'boginia zemsty i przeznaczenia'),
    Gods('Tyche', 'boginia przypadku, szczęścia i niesczęścia'),
    Gods('Chronos', 'bóg czasu'),
    Gods('Charon', 'przewoznik dusz przez rzekę Styks'),
    Gods('Eros', 'bóg miłości i namiętności'),
    Gods('Prometeusz', 'twórca ludzi'),
    Gods('Kalliope', 'muza poezji epickiej oraz filosofu i retoryki'),
    Gods('Klio', 'muza historii'),
    Gods('Erato', 'muza poezji miłosnej'),
    Gods('Euterpe', 'muza poezji lirycznej'),
    Gods('Melpomene', 'muza tragedii i śpiewu'),
    Gods('Polichymnia', 'muza pieśni i pantomimy'),
    Gods('Talia', 'muza komedii'),
    Gods('Terpsychora', 'muza tańca'),
    Gods('Urania', 'muza astronomii i geometrii')
]

print("1 - bogi(muzy), 2 - definicji")
answer = input()
if answer == "1":
    for i in range(len(gods)):
        temp = getRandomValue(gods, True)
        print(gods[temp].name)
        input()
        print(gods[temp].definition)
else:
    for i in range(len(gods)):
        temp = getRandomValue(gods, False)
        print(gods[temp].definition)
        input()
        print(gods[temp].name)
