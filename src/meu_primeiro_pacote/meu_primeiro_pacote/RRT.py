import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
from math import *
from matplotlib.colors import Normalize
import random

pgmf = open('src/meu_primeiro_pacote/meu_primeiro_pacote/my_map.pgm', 'rb')
matrix = plt.imread(pgmf)

matrix_copia = 1.0 * (matrix > 250)

inicio = (300, 25) 
final = (19, 298) 

matrix_copia[final[0]][final[1]] = 0 
matrix_copia[inicio[0]][inicio[1]] = 0   

#algoritmo
f_crescimento = 10
arvore = [inicio] 
caminho = []
pais =list()
filhos = list()
max_interacoes = 1000

def achando_no_proximo(arvore, ponto_aleatorio):
    menor_dist = math.dist((350,0), (0,350))
    no_mais_prox = 0
    for n in arvore:
        dist = math.dist(n, ponto_aleatorio)
        if dist < menor_dist:
            menor_dist = dist
            no_mais_prox = n
    return no_mais_prox

def gerando_novo_no(no_mais_prox, ponto_aleatorio, f_crescimento):
    vet_direcao = (ponto_aleatorio[0] - no_mais_prox[0], ponto_aleatorio[1] - no_mais_prox[1])
    modulo_vet = math.sqrt(vet_direcao[0]**2 + vet_direcao[1]**2)

    if modulo_vet < f_crescimento:
        return ponto_aleatorio
    
    fator = f_crescimento / modulo_vet
    novo_no = (int(no_mais_prox[0] + vet_direcao[0] * fator), int(no_mais_prox[1] + vet_direcao[1] * fator))
    
    return novo_no

for i in range(max_interacoes):
    ponto_aleatorio = (random.randint(0, 350), random.randint(0, 350))  

    no_mais_proximo = achando_no_proximo(arvore, ponto_aleatorio)
    novo_no = gerando_novo_no(no_mais_proximo, ponto_aleatorio, f_crescimento)

    if matrix_copia[novo_no[0]][novo_no[1]] == 1.0: 
        arvore.append(novo_no)  
        caminho.append((no_mais_proximo, novo_no)) 
        pais.append(no_mais_proximo)
        filhos.append(novo_no)

        if math.dist(novo_no, final) < f_crescimento:
            print("chegou")
            break

matrix_copia = cv2.cvtColor(matrix.copy(), cv2.COLOR_GRAY2RGB)


for (ponto1, ponto2) in caminho:
    cv2.line(matrix_copia, ponto1[::-1], ponto2[::-1], (0, 0, 255), 1)

caminho_correto = []
filho = no_mais_proximo
pai = novo_no

while(1):
    ind = filhos.index(filho)
    pai = pais[ind]
    caminho_correto.append((pai, filho))
    filho = pai
    if(filho == inicio):
        break

for (ponto1, ponto2) in caminho_correto:
    cv2.line(matrix_copia, ponto1[::-1], ponto2[::-1], (255, 0, 0), 1) 

plt.imshow(matrix_copia)
plt.title('Caminho calculado usando RRT')
plt.show()
