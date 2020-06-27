"""
requires a csv file
"""
import csv
import matplotlib.pyplot as plt
import numpy as np


ys, stations = [], []

with open("prices.csv") as file:
    data = csv.reader(file, delimiter=',')
    for line in data:
        stations.append(line[0])
        ys.append(int(line[1]))


xs = range(len(stations))

fig, ax = plt.subplots()


plt.scatter(xs, ys, label=u'1-комнатные квартиры', color='r')

plt.xlabel('Станции метро')
plt.ylabel('Стоимость квартиры в рублях')
plt.title('Средняя стоимость 1-комнатных квартир \nпо станциям метро Санкт-Петербурга\n(2020, domofond.ru)')

plt.xticks(xs, stations)
fig.autofmt_xdate(rotation=45)

plt.show()
