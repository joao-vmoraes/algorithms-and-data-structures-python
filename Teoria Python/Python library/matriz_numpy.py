import numpy as np

#Fazendo a inicialização de uma matriz com 2 linhas e 3 colunas.
matriz =  np.array([[3,4,1],
                    [3,1,5]])

# matriz.shape = mostra o formato da matriz: ( 2 , 3 )
#matriz[0] = vai mostrar apenas a primeira linha

soma  = 0
for i in range(matriz.shape[0]): 
    print(matriz[i])
    for j in range (matriz.shape[1]):
        soma += matriz[i][j]

print(soma)