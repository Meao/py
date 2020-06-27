"""
Krivcun Marina IVT3
If you see errors, please restart, recursive errors are due to the CBR API limits.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

from urllib.request import urlopen
from xml.etree import ElementTree as ET

def get_currencies(currencies_ids_lst=["R01239", "R01235", "R01035", "R01720", "R01760", "R01770", "R01775", "R01810", "R01815", "R01820"]):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
    # курс валют с сайта Центробанка РФ (http://www.cbr.ru) с использованием сервиса, который они предоставляют (описание сервиса: http://www.cbr.ru/development/SXML/).

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')

        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            valute_cur_name = el.find('CharCode').text
            result[valute_cur_name] = valute_cur_val

    return result


# TODO 0

# Вывести на графике 10 валют (получить по кодам валюты из ЦБС)

cur_vals = get_currencies()
objects = cur_vals.keys()

print(cur_vals)
y_pos = np.arange(len(objects))

# TODO #1 переписать лямбда-функцию из следующей строки через list comprehension

# или генераторы списков (как мы их называем)
# performance = list(
#    map(lambda x: float(x.replace(",", ".")), cur_vals.values()))

performance = [float(x.replace(",", ".")) for x in cur_vals.values()]
y_ls = np.arange(len(performance))
# TODO #2

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков),
# столбцы должны быть разных цветов с легендой

# TODO #3

# Нарисовать отдельный график с колебанием одной (выбранной вами) валюты
# (получить данные с сайта ЦБ за год) и отобразить его наиболее
# оптимальным образом (типом графика)

def get_currency_var(currency_id="R01035"):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=14/03/2001&VAL_NM_RQ=R01035")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    records = root.findall('Record')
    for el in records:
        record_id = el.get('Date')
        valute_cur_val = el.find('Value').text
        result[record_id] = valute_cur_val

    return result
cur_v = get_currency_var()
days = cur_v.keys()
xs = np.arange(len(days))
ys = [float(x.replace(",", ".")) for x in cur_v.values()]
# TODO #4

# Отобразить это на одном изображении (2 графика)
colors = ["#00cc66", "#33cc33", "#99ff33", "#99cc00", "#009900", "#009933", "#00cc00", "#00cc66", "#00cc99", "#33cccc"]

plt.subplot(2, 1, 1)
plt.plot(xs, ys)
plt.title('Exchange rates of EUR')

plt.subplot(2, 1, 2)
for x,y,c,lb in zip(y_pos, performance, colors, objects):
    plt.bar(x, y, color=c,label=lb)
plt.legend(bbox_to_anchor=(1, 1.3))
plt.xticks(y_pos, objects)
plt.yticks(y_ls, performance)
plt.xlabel('Currencies')
plt.ylabel('Roubles')
plt.title('Exchange rates')

# plt.show() # savetofig
plt.savefig('graph.png')
