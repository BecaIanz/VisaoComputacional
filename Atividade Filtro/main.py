from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)


    linKernel = len(kernel)
    colKernel = len(kernel[0])

    coluna = []
    linha = []
    filtered = []
   
    quantc = colKernel // 2
    quantl = linKernel // 2

    for f in range(colKernel):
        coluna.append(quantc*(-1))
        quantc -= 1

    for g in range(linKernel):
        linha.append(quantl*(-1))
        quantl -= 1

    #aqui vamos percorrer a imagem
    for i in range(len(image)):
        new_lin = []
        for j in range(len(image[i])):
            soma = 0
            soma_kernel = 0 
            #aqui vamos percorrer o kernel e a 'matriz em volta do nosso querido e almejado pixel
            for k in range(linKernel):
                for l in range(colKernel):
                    soma_kernel += kernel[k][l]
                    if((i + linha[k] < 0) or (i + linha[k] > len(image)-1) or ( j + coluna[l] < 0) or (j + coluna[l] > len(image[i])-1)):
                        continue
                    soma += (image[i + linha[k]][j + coluna[l]] * kernel[k][l])


            if (soma_kernel != 0):
                soma = soma/soma_kernel

            if(soma > 255):
                soma = 255
            elif(soma < 0):
                soma = 0
                
            new_lin.append(soma)
        filtered.append(new_lin)
    return filtered

Kernel = Kernel("minion.png", filter_function)  


init()