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

def calcula_h(node, end):
    return math.sqrt((node[0] - end[0])**2 + (node[1] - end[1])**2) #eurística = distancia euclidiana

# nó =  lista [x, y, g, h, f, parent]
start_node = [x_inicio, y_inicio, 0, 0, 0, None] 
end_node = [x_final, y_final, 0, 0, 0, None]

g = 0  
h = calcula_h(start_node, end_node)  
f = g + h 

# atualiza o nó inicial
start_node[2] = g 
start_node[3] = h 
start_node[4] = f 

open_list = [] #nós que ainda não foram abertos
closed_list = [] #nós já analizados

open_list.append(start_node)

#função para encontrar o nó com menor f na open list
def encontra_menor_f(open_list):
    menor_f = open_list[0]
    for node in open_list:
        if node[4] < menor_f[4]:  #compara valor de f - ind.4 na lista
            menor_f = node
    return menor_f

def verifica_vizinhos(node, matrix):
    vizinhos = []
    x, y = node[0], node[1]

    movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0),  # Lateral e vertical
              (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonais

    for move in movimentos:
        new_x = x + move[0]
        new_y = y + move[1]

        #verifica se ta dentro dos limites da matriz e se nao é um obstaculo
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] == 1:
            new_node = [new_x, new_y, 0, 0, 0, node]  # Cria um novo nó com parent
            vizinhos.append(new_node)

    print(f"Vizinhos de ({x}, {y}): {vizinhos}")
    return vizinhos

#loop principal do A*:
while len(open_list) > 0:
    # nó com o menor valor de 'f' da open list
    current_node = encontra_menor_f(open_list)
    
    caminho = []
    if current_node[0] == x_final and current_node[1] == y_final:
        #caminho = []
        print("Nó final encontrado!")
        while current_node is not None:
            caminho.append([current_node[0], current_node[1]])
            current_node = current_node[5]  # caminho de volta pelo nó pai
        caminho.reverse()  # inverte o caminho para ficar do início ao fim
        break
    
    # mover o nó atual da open list para a closed list
    open_list.remove(current_node)
    closed_list.append(current_node)
    
    # expandir os vizinhos do nó atual
    vizinhos = verifica_vizinhos(current_node, matrix)
    
    for vizinho in vizinhos:
        # se o vizinho já está na lista fechada, ignora
        if any(v[0] == vizinho[0] and v[1] == vizinho[1] for v in closed_list):
            continue
        
        movimento_diagonal = abs(vizinho[0] - current_node[0]) == 1 and abs(vizinho[1] - current_node[1]) == 1
        if movimento_diagonal:
            vizinho[2] = current_node[2] + math.sqrt(2)  # movimento diagonal tem custo g = sqrt(2)
        else:
            vizinho[2] = current_node[2] + 1  # movimento lateral/vertical tem custo g = 1

        # calcula h e f
        vizinho[3] = calcula_h(vizinho, end_node)  # h: distância euclidiana até o fim
        vizinho[4] = vizinho[2] + vizinho[3]  # f = g + h
        
        # se o vizinho já está na open list, verificar se o novo caminho é melhor
        vizinho_aberto = next((v for v in open_list if v[0] == vizinho[0] and v[1] == vizinho[1]), None)
        if vizinho_aberto:
            if vizinho[2] < vizinho_aberto[2]:
                # se o novo caminho for melhor, atualiza os valores e o nó pai
                vizinho_aberto[2] = vizinho[2]
                vizinho_aberto[3] = vizinho[3]
                vizinho_aberto[4] = vizinho[4]
                vizinho_aberto[5] = current_node
        else:
            # se o vizinho não está na lista aberta, adiciona
            open_list.append(vizinho)

    

plt.imshow(matrix, interpolation='nearest', cmap='gray')

print("Caminho:", caminho)

caminho_x = [coord[0] for coord in caminho]  # Lista de coordenadas x do caminho (colunas)
caminho_y = [coord[1] for coord in caminho]  # Lista de coordenadas y do caminho (linhas)

plt.plot(caminho_x, caminho_y, marker='o', color='r', linewidth=2)  # Linha vermelha com círculos nos pontos
plt.scatter(x_inicio, y_inicio, color='blue', label='Início')  # Inverter para o ponto inicial
plt.scatter(x_final, y_final, color='green', label='Final')    # Inverter para o ponto final

plt.legend()
plt.show()