import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


# Define the data https://spb.cian.ru/kupit-1-komnatnuyu-kvartiru-sankt-peterburg-morskaya-naberezhnaya-024310/
ydata = [4750000, 4890000, 4920000, 5200000, 5250000, 5250000, 5320000, 5650000, 5650000, 6150000, 6700000, 6900000, 6950000, 7500000, 8800000, 10000000]
xdata = np.arange(len(ydata))

np_x = np.array(xdata)
np_y = np.array(ydata)

x2 = list(range(len(ydata)))

plt.scatter(xdata, ydata, label=u'Исходные данные', color='r')

f3 = sp.poly1d(np.polyfit(np_x, np_y, 3))
plt.plot(x2, f3(x2), linewidth=3, label=u' полином 3 степени')

f4 = sp.poly1d(np.polyfit(np_x, np_y, 4))
plt.plot(x2, f4(x2), linewidth=3, label=u' полином 4 степени')

f5 = sp.poly1d(np.polyfit(np_x, np_y, 10))
plt.plot(x2, f5(x2), linewidth=3, label=u' полином 10 степени')

plt.title('Интерполяция многочлена заданного порядка к набору значений')
plt.legend()
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
# plt.xlabel('Квартиры с ценами от минимальной до максимальной')
plt.ylabel('Цена 1-комнатной квартиры')
plt.show()
plt.savefig('plot.png')
