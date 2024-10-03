import numpy as np
from matplotlib import pyplot as plt
from collections import deque

# Carrega o mapa
pgmf = open('src/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)

# Normaliza o mapa (obstáculos serão 0, áreas livres 1)
matrix = 1.0 * (matrix > 250)
matrix[100][800] = 0  # Obstáculo
matrix[100][700] = 2  # Objetivo final

# Configura o tamanho da grid e posições do objetivo
goal_x, goal_y = 700, 100
matrix[goal_y][goal_x] = 2  # Define o objetivo no grid

# Criação da fila para a propagação do Wavefront
queue = deque([(goal_y, goal_x)])

# Vetores de movimento (cima, baixo, esquerda, direita)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Propagação da onda
while queue:
    y, x = queue.popleft()
    
    # Verifica as 4 direções ao redor do ponto atual
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        
        # Verifica se está dentro dos limites e se a célula é livre
        if 0 <= ny < matrix.shape[0] and 0 <= nx < matrix.shape[1]:
            if matrix[ny][nx] == 1:  # Célula livre
                # Define o valor da célula como o valor da célula anterior + 1
                matrix[ny][nx] = matrix[y][x] + 1
                queue.append((ny, nx))

# Exibe o mapa resultante
plt.imshow(matrix, interpolation='nearest', cmap='gray')
plt.show()
