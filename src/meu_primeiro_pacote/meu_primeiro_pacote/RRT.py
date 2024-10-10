import math
import numpy as np
from matplotlib import pyplot as plt

pgmf = open('src/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)
#print (matrix)

matrix = 1.0 * (matrix > 250)
print (matrix)
plt.imshow(matrix, interpolation='nearest', cmap='gray')
#plt.show()

x_inicio = 650
y_inicio = 400

x_final = 833
y_final = 85

