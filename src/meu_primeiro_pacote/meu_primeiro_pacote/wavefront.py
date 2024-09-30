from matplotlib import pyplot as plt

pgmf = open('src/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)
print (matrix)

matrix = 1.0 * (matrix > 250)
matrix [100][800] = 0 #fica preto
matrix [100][700] = 2 #define coordenadas do objetivo final
plt.imshow(matrix, interpolation='nearest', cmap='gray')
plt.show()
