# pip install pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from matplotlib import pyplot as plt

pgmf = open('aprendendo_ros2/src/meu_primeiro_pacote/meu_primeiro_pacote/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)
print (matrix)

matrix = 1.0 * (matrix > 250)
plt.imshow(matrix, interpolation='nearest', cmap='gray')
plt.show()

x_inicio = 650
y_inicio = 400

x_final = 700
y_final = 100

#continuar!
