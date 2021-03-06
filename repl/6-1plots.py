# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 2
"""
Используя обучающий набор данных о пассажирах Титаника,
находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), визуализируйте данные:
- стоимости билетов пассажиров с помощью диаграммы рассеяния (scatterplot):
по оси X - пассажиры в порядке увеличения PassengerId, по оси Y - стоимость билетов
- проанализировать как наилучшим образом визуализировать данные о ценовом распределении билетов (предложить собственный вариант реализации после создании визуализации ниже).

 Отобразить два графика (subplot) на одном изображении (figure): 
 1. График типа boxplot, на котором отобразить распределение цен билетов по классам (1, 2, 3).
 2. Столбчатую диаграмму (countplot) с распределением средних цен на билеты сгруппированным по трем портам (S, C, Q).

Сохранить получившиеся графики в файлах: result1.png, result2.png.
Настроить название графиков, подписи осей, отобразить риски со числовыми значениями на графике, сделать сетку на графике
(если необходимо для улучшения изучения данных на графике).


"""

import pandas  # импортирование библиотеки для считывания данных
import matplotlib.pyplot as plt  # импорт библиотеки для отрисовки графика
import math
import numpy as np  # импорт библиотеки для реализации вычислений значений
import seaborn as sns

    
fig = plt.figure()
ax = fig.add_subplot(121)
sns.boxplot(x = 'Pclass', y = 'Fare', data = data)
plt.title('цены по классам (1, 2, 3).')
bx = fig.add_subplot(122)
g = sns.countplot(data=data, x='Embarked', hue='Fare')
plt.title('цены по портам (S, C, Q).')
bx.legend_.remove()
plt.show()
fig.savefig('result1.png')
