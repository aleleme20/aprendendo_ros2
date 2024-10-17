import math
import numpy as np
from matplotlib import pyplot as plt

# Carregar o mapa
pgmf = open('src/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)

# Transformar a imagem do mapa em matriz binária (obstáculos = 0, livre = 1)
matrix = 1.0 * (matrix > 250)
print(f"Dimensões da matriz: {matrix.shape}")

# Ponto inicial e final
x_inicio = 650
y_inicio = 400
x_final = 833
y_final = 85

print(f"Valor do ponto inicial: {matrix[y_inicio][x_inicio]}")
print(f"Valor do ponto final: {matrix[y_final][x_final]}")

# Função para cálculo da heurística (distância euclidiana)
def calcula_h(node, end):
    return math.sqrt((node[0] - end[0])**2 + (node[1] - end[1])**2)

# nó = lista [x, y, g, h, f, parent]
start_node = [x_inicio, y_inicio, 0, 0, 0, None]
end_node = [x_final, y_final, 0, 0, 0, None]

g = 0
h = calcula_h(start_node, end_node)
f = g + h

# Atualiza o nó inicial
start_node[2] = g
start_node[3] = h
start_node[4] = f

open_list = []  # nós a serem explorados
closed_list = []  # nós já explorados

open_list.append(start_node)

# Função para encontrar o nó com menor f na open list
def encontra_menor_f(open_list):
    menor_f = open_list[0]
    for node in open_list:
        if node[4] < menor_f[4]:  # compara valor de f (ind.4)
            menor_f = node
    return menor_f

# Função para verificar vizinhos
def verifica_vizinhos(node, matrix):
    vizinhos = []
    x, y = node[0], node[1]

    movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0),  # Lateral e vertical
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonais

    for move in movimentos:
        new_x = x + move[0]
        new_y = y + move[1]

        # Verificar se o vizinho está dentro dos limites da matriz
        if 0 <= new_x < matrix.shape[1] and 0 <= new_y < matrix.shape[0]:
            # Verificar se o vizinho é transitável
            if matrix[new_y][new_x] == 1:
                new_node = [new_x, new_y, 0, 0, 0, node]
                vizinhos.append(new_node)
        else:
            print(f"Coordenada fora dos limites: ({new_x}, {new_y})")

    print(f"Vizinhos de ({x}, {y}): {vizinhos}")
    return vizinhos

# Loop principal do A*:
caminho = []
iteration = 0  # Adicionando contador de iterações para depuração

while len(open_list) > 0:
    iteration += 1
    print(f"Iteração: {iteration}")
    
    # Encontrar o nó com menor valor de f na open list
    current_node = encontra_menor_f(open_list)
    
    print(f"Analisando nó: {current_node}")

    # Verificar se alcançamos o nó final
    if current_node[0] == x_final and current_node[1] == y_final:
        print("Nó final encontrado!")
        while current_node is not None:
            caminho.append([current_node[0], current_node[1]])
            current_node = current_node[5]  # Caminho de volta pelo nó pai
        caminho.reverse()  # Inverte o caminho para ficar do início ao fim
        break
    
    # Remover o nó atual da open list e adicionar à closed list
    open_list.remove(current_node)
    closed_list.append(current_node)
    
    # Expandir os vizinhos do nó atual
    vizinhos = verifica_vizinhos(current_node, matrix)

    # Caso não haja vizinhos transitáveis, evitar o loop infinito
    if not vizinhos:
        print(f"Nenhum vizinho transitável encontrado para o nó: {current_node}")
        continue
    
    for vizinho in vizinhos:
        # Se o vizinho já está na lista fechada, ignora
        if any(v[0] == vizinho[0] and v[1] == vizinho[1] for v in closed_list):
            continue

        # Calcular o custo g (movimento lateral/vertical = 1, diagonal = sqrt(2))
        movimento_diagonal = abs(vizinho[0] - current_node[0]) == 1 and abs(vizinho[1] - current_node[1]) == 1
        if movimento_diagonal:
            vizinho[2] = current_node[2] + math.sqrt(2)
        else:
            vizinho[2] = current_node[2] + 1

        # Calcular h e f
        vizinho[3] = calcula_h(vizinho, end_node)
        vizinho[4] = vizinho[2] + vizinho[3]

        # Verificar se o vizinho já está na open list
        vizinho_aberto = next((v for v in open_list if v[0] == vizinho[0] and v[1] == vizinho[1]), None)
        if vizinho_aberto:
            # Se o novo caminho for melhor, atualiza os valores e o nó pai
            if vizinho[2] < vizinho_aberto[2]:
                vizinho_aberto[2] = vizinho[2]
                vizinho_aberto[3] = vizinho[3]
                vizinho_aberto[4] = vizinho[4]
                vizinho_aberto[5] = current_node
        else:
            # Se o vizinho não está na open list, adiciona
            open_list.append(vizinho)

    # Garantir que o nó está progredindo
    if current_node in open_list:
        print(f"Erro: o nó {current_node} não foi removido corretamente da open_list!")

# Exibir o mapa e o caminho
plt.imshow(matrix, interpolation='nearest', cmap='gray')

print("Caminho:", caminho)

if caminho:
    caminho_x = [coord[0] for coord in caminho] 
    caminho_y = [coord[1] for coord in caminho]  

    plt.plot(caminho_x, caminho_y, marker='o', color='r', linewidth=2)  
    plt.scatter(x_inicio, y_inicio, color='blue', label='Início')  
    plt.scatter(x_final, y_final, color='green', label='Final')   

    plt.legend()
    plt.show()
else:
    print("Nenhum caminho encontrado.")
