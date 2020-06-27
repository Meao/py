"""
Krivcun Marina IVT3
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * x*x + b * x + c
# Define the data https://spb.cian.ru/kupit-1-komnatnuyu-kvartiru-sankt-peterburg-morskaya-naberezhnaya-024310/
ydata = [4750000, 4890000, 4920000, 5200000, 5250000, 5250000, 5320000, 5650000, 5650000, 6150000, 6700000, 6900000, 6950000, 7500000, 8800000, 10000000]
xdata = np.arange(len(ydata))
plt.plot(xdata, ydata, '.', label='данные')
# Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, xdata, ydata)
# отклонение данных модели от реальных данных.
print(pcov)
plt.plot(xdata, func(xdata, *popt), 'r-',
         label='модель: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
# Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
# popt, pcov = curve_fit(func, xdata, ydata)
# popt

#plt.plot(xdata, func(xdata, *popt), 'g--',
#         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
# plt.xlabel('Квартиры с ценами от минимальной до максимальной')
plt.title('Модель (квадратичная функция) предсказания цен')
plt.ylabel('Цена 1-комнатной квартиры')
plt.legend()
# plt.show()
plt.savefig('graph.png')
