import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
from math import *
from matplotlib.colors import Normalize

pgmf = open('my_map.pgm', 'rb')
<<<<<<< HEAD
matrix = plt.imread(pgmf)

matrix_copia = 1.0 * (matrix > 250)

final = (35, 373) 
inicio = (359, 36) 

matrix_copia[final[0]][final[1]] = 0 
matrix_copia[inicio[0]][inicio[1]] = 0   

#fig = plt.figure()
#fig.canvas.manager.set_window_title('Figura 1')

#plt.imshow(matrix_copia, interpolation='nearest', cmap='gray')
#plt.title('Imagem inicial')
#plt.show()
=======
image = plt.imread(pgmf)

image_copia = 1.0 * (image > 250)

goal = (80, 325) 
robo = (300, 25) 

image_copia[goal[0]][goal[1]] = 0 
image_copia[robo[0]][robo[1]] = 0   

fig = plt.figure()
fig.canvas.manager.set_window_title('Figura 1')

plt.imshow(image_copia, interpolation='nearest', cmap='gray')
plt.title('Imagem inicial')
plt.show()
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5

def indice_menor_valor(lista_f, lista_c):
    if not lista_f or not lista_c :
        return 
    
    lista_f = np.array(lista_f)
    lista_c = np.array(lista_c)

    lista_ind = np.where(lista_f == min(lista_f))
    lista_ind = lista_ind[0]

<<<<<<< HEAD
    h_min = math.dist(lista_c[lista_ind[0]], final)
=======
    h_min = math.dist(lista_c[lista_ind[0]], goal)
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5

    menor_indice = lista_ind[0]

    for i in lista_ind:
<<<<<<< HEAD
        h = math.dist(lista_c[i], final)
=======
        h = math.dist(lista_c[i], goal)
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5
        if (h < h_min):
            h_min = h
            menor_indice = i

    return menor_indice

#algoritmo de busca pelo ponto
<<<<<<< HEAD
matrix_copia[final[0]][final[1]] = 2 #objetivo é 2
matrix_copia[inicio[0]][inicio[1]] = 1 #inicio é 1

menor_h = 1000
ponto = inicio
=======
image_copia[goal[0]][goal[1]] = 2 #objetivo é 2
image_copia[robo[0]][robo[1]] = 1 #robo é 1

menor_h = 1000
ponto = robo
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5
parar = False
coordenadas = list()
caminho_f = list ()

while(1):
    for l in range (-1,2):
        for c in range (-1,2):
            try:
<<<<<<< HEAD
                if(matrix_copia[ponto[0]+l][ponto[1]+c] == 1):
                    g = math.dist(inicio, (ponto[0]+l,ponto[1]+c))
                    h = math.dist((ponto[0]+l,ponto[1]+c), final)
                    f = g + h

                    matrix_copia[ponto[0]+ l][ponto[1]+c]= f
                    caminho_f.append(f)
                    coordenadas.append([ponto[0]+ l, ponto[1]+c])

                if(ponto[0]+l == final[0] and ponto[1]+c == final[1]):
=======
                if(image_copia[ponto[0]+l][ponto[1]+c] == 1):
                    g = math.dist(robo, (ponto[0]+l,ponto[1]+c))
                    h = math.dist((ponto[0]+l,ponto[1]+c), goal)
                    f = g + h

                    image_copia[ponto[0]+ l][ponto[1]+c]= f
                    caminho_f.append(f)
                    coordenadas.append([ponto[0]+ l, ponto[1]+c])

                if(ponto[0]+l == goal[0] and ponto[1]+c == goal[1]):
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5
                    parar = True
                    break
            except: 
                continue
        if(parar == True):
            break   
    if(parar == True):
           break   
    
    menor_ind = indice_menor_valor(caminho_f, coordenadas)
    if menor_ind is None:
        print("Erro: não foi encontrado um índice válido para continuar.")
        continue
    else:
        ponto = coordenadas.pop(menor_ind)
        caminho_f.pop(menor_ind)


<<<<<<< HEAD
#fig = plt.figure()
#fig.canvas.manager.set_window_title('Figura 2')

#norm = Normalize(vmin=371, vmax=373)
#cmap= plt.get_cmap('viridis')

#plt.imshow(matrix_copia, interpolation='nearest', cmap='viridis')  # Usando viridis para ver os valores
#plt.colorbar()
#plt.title('Imagem colorida de proximidade')
#plt.show()

#algoritmo de encontrar o caminho certo
ponto_inicial = inicio
caminho = [inicio]
menor = matrix_copia[inicio[0]][inicio[1]] + 2
menor_posicao = inicio
=======
fig = plt.figure()
fig.canvas.manager.set_window_title('Figura 2')

norm = Normalize(vmin=371, vmax=373)
cmap= plt.get_cmap('viridis')

plt.imshow(image_copia, interpolation='nearest', cmap='viridis', norm=norm)  # Usando viridis para ver os valores
plt.colorbar()
plt.title('Imagem colorida de proximidade')
plt.show()

#algoritmo de encontrar o caminho certo
ponto_inicial = robo
caminho = [robo]
menor = image_copia[robo[0]][robo[1]] + 2
menor_posicao = robo
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5
parar = False
listafechada = list()

while(1):
    for l in range (1,-2,-1):
        for c in range (1,-2,-1):
            try:          
<<<<<<< HEAD
                if(matrix_copia[ponto_inicial[0]+l][ponto_inicial[1]+c] > 1 and matrix_copia[ponto_inicial[0]+l][ponto_inicial[1]+c] < menor and ([ponto_inicial[0]+l],[ponto_inicial[1]+c]) not in listafechada and (([ponto_inicial[0]+l],[ponto_inicial[1]+c]) != ([ponto_inicial[0]], [ponto_inicial[1]]))):
                    menor = matrix_copia[ponto_inicial[0]+l][ponto_inicial[1]+c]
                    menor_posicao = (ponto_inicial[0]+l, ponto_inicial[1]+c)

                if(ponto_inicial[0]+l == final[0] and ponto_inicial[1]+c == final[1]):
=======
                if(image_copia[ponto_inicial[0]+l][ponto_inicial[1]+c] > 1 and image_copia[ponto_inicial[0]+l][ponto_inicial[1]+c] < menor and ([ponto_inicial[0]+l],[ponto_inicial[1]+c]) not in listafechada and (([ponto_inicial[0]+l],[ponto_inicial[1]+c]) != ([ponto_inicial[0]], [ponto_inicial[1]]))):
                    menor = image_copia[ponto_inicial[0]+l][ponto_inicial[1]+c]
                    menor_posicao = (ponto_inicial[0]+l, ponto_inicial[1]+c)

                if(ponto_inicial[0]+l == goal[0] and ponto_inicial[1]+c == goal[1]):
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5
                    parar = True
                    break

                listafechada.append(([ponto_inicial[0]+l],[ponto_inicial[1]+c]))
            except: 
                continue

        if(parar == True):
            break 

    ponto_inicial = menor_posicao
    caminho.append(menor_posicao)
    menor = menor + 2

    if(parar == True):
        break 
    
#colorindo caminho :)

<<<<<<< HEAD
imagem_caminho = matrix.copy()
imagem_caminho = cv2.cvtColor(imagem_caminho, cv2.COLOR_GRAY2RGB)

for i in caminho:

    imagem_caminho[i[0]][i[1]] = [254, 0, 0]

plt.imshow(imagem_caminho)
plt.title('Imagem com caminho')
plt.show()
=======
image_com_caminho = image.copy()
image_com_caminho = cv2.cvtColor(image_com_caminho, cv2.COLOR_GRAY2RGB)

for i in caminho:

    image_com_caminho[i[0]][i[1]] = [254, 0, 0]

plt.imshow(image_com_caminho)
plt.title('Imagem com caminho')
plt.show()
>>>>>>> 474bd5a4b63d940935f918e38fed7c017bfe2ad5
