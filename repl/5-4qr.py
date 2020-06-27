"""
4.2. Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать изображение QR-кода на основе переданной в программу текстовой строки.

4.3. Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения в несколько случайно определяемых цветов.
"""

import pyqrcode
import random


def qr_blackwhite(data, filename):
    qr = pyqrcode.create(data)
    qr.png(filename)

def qr_colored(data, filename, scale = 10):
    color1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    color2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    qr = pyqrcode.create(data)
    qr.png(filename, scale = scale, module_color = color1, background = color2)


if __name__ == '__main__':
    url = 'https://youtu.be/S7Qa7xgxl6Y'
    qr_blackwhite(url, 'qr_blackwhite.png')
    qr_colored(url, 'qr_colored.png')
