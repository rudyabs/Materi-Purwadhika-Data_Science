import matplotlib.pyplot as plt
import numpy as np
import csv

# players = []
# with open('data.csv', 'r', encoding= 'utf-8') as fifa:
#     reader = csv.DictReader(fifa)
#     for i in reader:
#         players.append(dict(i))

# print(players[0])
# print(len(players))
# print(players[0]['Age'])
# print(type(players[0]['Overall']))

with open('data.csv', 'r', encoding='utf8') as fifa_db:
    reader = csv.DictReader(fifa_db)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

names = data['Name']
ages = data['Age']
overalls = data['Overall']

# plt.scatter(age, overall)
# plt.show()

