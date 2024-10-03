import numpy as np
from matplotlib import pyplot as plt

pgmf = open('src/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)

matrix = 1.0 * (matrix > 250)
matrix[400][850] = 0  # Robô
matrix[100][700] = 2  # Objetivo final

obj_x, obj_y = 700, 100
matrix[obj_y][obj_x] = 2  

fila = [(obj_y, obj_x)]

direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)] #(cima, baixo, esquerda, direita) 


while fila:
    y, x = fila.pop(0)  #remove o primeiro elemento da fila
    
    # verifica as 4 direções ao redor do ponto atual
    for dy, dx in direcoes:
        ny, nx = y + dy, x + dx
        if 0 <= ny < matrix.shape[0] and 0 <= nx < matrix.shape[1]:
            if matrix[ny][nx] == 1:  # celula livre
                matrix[ny][nx] = matrix[y][x] + 1
                fila.append((ny, nx))  # add a celula na fila


plt.imshow(matrix, interpolation='nearest', cmap='viridis')
plt.colorbar() #deixa o mapa colorido
plt.show()
