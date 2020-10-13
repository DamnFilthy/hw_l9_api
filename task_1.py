import requests
import os
from pprint import pprint

# Нужно вызвать всех героев по ID - дальше отфильтровать по имени
# и вывести самого умного, но сайт не дает всех героев по ID
# (сайт дает какую то часть героев но не всех) Поэтому пришлось по имени
# вызывать нужных героев отдельным запросом
# response = requests.get(\
# "https://superheroapi.com/api/2619421814940190/search/id",\
# headers={"User-Agent": "superman"})
# data = response.json()
# pprint(data)


# Ищем Халка
response = requests.get(\
"https://superheroapi.com/api/2619421814940190/search/hulk",\
headers={"User-Agent": "superman"})
data = response.json()["results"]

for post in data:
    name = post["name"]
    id = post["id"]
    powerstats = post["powerstats"]
    intelligence = powerstats["intelligence"]

    if name != "Hulk":
        continue

    hulk_name = name
    hulk_int = intelligence

print(hulk_name, ' int ', hulk_int)

# Ищем Капитана Америку
response = requests.get(\
"https://superheroapi.com/api/2619421814940190/search/Captain",\
headers={"User-Agent": "superman"})
data = response.json()["results"]

for post in data:
    name = post["name"]
    id = post["id"]
    powerstats = post["powerstats"]
    intelligence = powerstats["intelligence"]

    if name != "Captain America":
        continue

    captain_name = name
    captain_int = intelligence
    print(captain_name, ' int ', captain_int)

# Ищем Таноса
response = requests.get(\
"https://superheroapi.com/api/2619421814940190/search/Thanos",\
headers={"User-Agent": "superman"})
data = response.json()["results"]

for post in data:
    name = post["name"]
    id = post["id"]
    powerstats = post["powerstats"]
    intelligence = powerstats["intelligence"]

    if name != "Thanos":
        continue

    thanos_name = name
    thanos_int = intelligence
    print(thanos_name, ' int ', thanos_int)

print("\nКто же умнее из этих супер героев? хмм..")

# Выводим самого умного
result = [[hulk_name, hulk_int],[captain_name, captain_int], [thanos_name, thanos_int]]
print(max(result))
