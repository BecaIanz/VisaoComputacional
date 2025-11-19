from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)

    linha = [[-1, -1, -1] , [0, 0, 0],[ 1, 1, 1]]
    coluna = [[-1, 0, 1] , [-1, 0, 1] ,[-1, 0, 1] ]
    filtered = image[:]
    soma_kernel = 0 
    #aqui vamos percorrer a imagem
    for i in range(len(image)):
        for j in range(len(image[i])):
            soma = 0
            #aqui vamos ercorrer o kernel e a 'matriz em volta do nosso querido e almejado pixel
            for k in range(3):
                for l in range(3):
                    if((i + linha[k][l] < 0) or (i + linha[k][l] > len(image)-1) or ( j + coluna[k][l] < 0) or (j + coluna[k][l] > len(image[i])-1)):
                        continue
                    soma += (image[i + linha[k][l]][j + coluna[k][l]] * kernel[k][l])
                    soma_kernel += kernel[k][l]

            if (soma_kernel <= 0):
                soma_kernel = 1
            
            soma = soma/soma_kernel

            if(soma > 255):
                soma = 255
            elif(soma < 0):
                soma = 0
                
            filtered[i][j] = soma
    return filtered

Kernel = Kernel("minion.png", filter_function)  

init()