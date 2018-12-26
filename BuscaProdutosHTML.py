import time
import os
import json
from bs4 import BeautifulSoup

def lista_inputs_produto(inicio, fim, lista_inputs):
    lista_retorno = []
    for i in range(len(lista_input)):
        if i >= inicio and i < fim:
            lista_retorno.append(lista_input[i])
    return lista_retorno


path_home = os.getenv("HOME") #Captura

for j in range(0,24):

    with open(path_home+'/LojaSidnei/HTML/pagina'+str(j+1)+'.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    #print(soup.div)
    #print(soup.get_text())

    #print(len(soup.div))

    #lista_div = soup.find_all(class_=['product'])

    #print(len(lista_div))

    #print(lista_div)




    lista_input = soup.find_all('input',type='hidden') #Busca por todas as Tags INPUT

    print(len(lista_input))

    lista_indices = []
    for i in range(len(lista_input)):
        if i > 1:
            vet = str(lista_input[i]).split(' ')
            if vet[len(vet)-1] == 'value="Pague"/>':
                lista_indices.append(i) #Pego o indice onde comeca o produto

    print(lista_indices)

    lista_produtos = []

    for i in range(len(lista_indices)):
        if i < (len(lista_indices)-1):
            lista_produtos.append(lista_inputs_produto(lista_indices[i],lista_indices[i+1],lista_input))
        else:
            lista_produtos.append(lista_inputs_produto(lista_indices[i], len(lista_input), lista_input))

    print('/ProjetoSidnei/Dados_html/produtos_pag'+str(j+1)+'.txt')

    arq = open(path_home+'/ProjetoSidnei/Dados_html/produtos_pag'+str(j+1)+'.txt', 'w')
    for i in lista_produtos:
        arq.write(str(i)+'\n')
        #time.sleep(1)

    arq.close()
    #time.sleep(2)


    #for i in lista_produtos:
        #print(i)

    #print(len(lista_produtos))


