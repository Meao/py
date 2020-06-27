from datetime import datetime
import numpy as np


my_array = []
n = int(input("Size of matrix:"))
print('matrix1')
for i in range(n):
    my_array.append([])
    for j in range(n):
        my_array[i].append(float(input("Element:")))
matrix1 = np.array(my_array)
print(np.floor(matrix1))
print('matrix2')
my_array = []
for i in range(n):
    my_array.append([])
    for j in range(n):
        my_array[i].append(float(input("Element:")))
matrix2 = np.array(my_array)
print(np.floor(matrix2))
startTime = datetime.now()
print('mutiplied')
res = np.dot(matrix1, matrix2)
print(np.floor(res))
endTime = datetime.now()
print(f'\nTime elapsed: {endTime - startTime} ')
# to test https://code-maven.com/mocking-input-and-output-for-python-testing
