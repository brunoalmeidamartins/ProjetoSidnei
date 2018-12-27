import time
import os
import json
from bs4 import BeautifulSoup

#Variaveis globais
path_home = os.getenv("HOME") #Captura a HOME do Usuario

def lista_inputs_produto(inicio, fim, lista_inputs):
    lista_retorno = []
    for i in range(len(lista_input)):
        if i >= inicio and i < fim:
            lista_retorno.append(lista_input[i])
    return lista_retorno

def lista_argumentos_produto(inicio, fim, lista_argumentos):
    lista_retorno = []
    for i in range(len(lista_argumentos)):
        if i>=inicio and i < fim:
            lista_retorno.append((lista_argumentos[i]))
    return lista_retorno

def montaArquivosProdutosInput():
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

def Lista_Produtos_Brutos():
    lista_produtos_bruto = []
    for t in range(24):
        with open(path_home+'/ProjetoSidnei/Dados_html/produtos_pag'+str(t+1)+'.txt','r') as f: #Abre o arquivo
            soup = BeautifulSoup(f,'html.parser') #Faz a leitura do arquivo
        lista_inputs = soup.find_all('input') #Gera a lista de inputs gravados no arquivo
        lista_arg = []
        for i in lista_inputs:
            lista_arg.append(i.get('value')) #Gera a lista com todos os values


        lista_indices = [] #Cria uma lista de indice onde comeca o produto
        for i in range(len(lista_arg)):
            if lista_arg[i] == 'Pague':
                lista_indices.append(i)

        #lista_produtos_bruto = [] #Guarda uma lista de values com informacoes do produto
        for i in range(len(lista_indices)):
            if i < (len(lista_indices) - 1):
                lista_produtos_bruto.append(lista_argumentos_produto(lista_indices[i], lista_indices[i + 1], lista_arg))
            else:
                lista_produtos_bruto.append(lista_argumentos_produto(lista_indices[i], len(lista_arg), lista_arg))

        '''
        for i in lista_produtos:
            #print(i[8]+' '+i[3].replace(' ',''))
            print(i)
        '''
    return lista_produtos_bruto

def retiraPosicoesInuteisDaLista(lista_produtos):
    lista_retorno = []
    for i in lista_produtos:
        lista_produto = []
        for j in range(len(i)):
            if j > 2:
                if i[j] != '' and j < (len(i)-2):
                    lista_produto.append(i[j])
        lista_retorno.append(lista_produto)
    #print(lista_retorno)
    return lista_retorno

def separaVetorDeProdutos(listas_indices, lista_separar):
    lista_retorno = []
    for i in range(len(lista_indices)):
        if i == 0:
            lista_retorno.append(separaVetorDeProdutos2(0,lista_indices[i],lista_separar))
        elif i < len(lista_indices)-1:
            lista_retorno.append(separaVetorDeProdutos2(lista_indices[i]+1,lista_indices[i+1],lista_separar))
        else:
            lista_retorno.append(separaVetorDeProdutos2(lista_indices[i] + 1, len(lista_separar)-1, lista_separar))
    #Tratamento!! Alguns listas tem uma ultima posicao vazia
    lista_aux = []
    for i in range(len(lista_retorno)):
        if len(lista_retorno[i]) != 0:
            lista_aux.append(lista_retorno[i])
    lista_retorno = lista_aux
    return lista_retorno

def separaVetorDeProdutos2(inicio,fim,lista_separar):
    lista_retorno = []
    for i in range(len(lista_separar)):
        if i >= inicio and i <=fim:
            lista_retorno.append((lista_separar[i]))
    return lista_retorno



lista_produtos = Lista_Produtos_Brutos()
'''
print(len(lista_produtos))
for i in lista_produtos:
    print(i)
'''


lista_produtos = retiraPosicoesInuteisDaLista(lista_produtos)
#print(len(lista_produtos))

'''
Cada posicao lista pode representar um produto ou um conjunto. Entao eh necessario separalos
'''
lista_produtos2 = []
for i in lista_produtos:
    lista_indices = []
    for j in range(len(i)):
        if len(i[j]) == 19: #ex:3074457345616693119
            lista_indices.append(j) #lista de indices para separacao
    #print(lista_indices)
    lista_produtos2.append(separaVetorDeProdutos(lista_indices,i))

lista_produtos_verdadeira = []
for i in lista_produtos2:
    for j in i:
        if len(j) == 5:
            lista_produtos_verdadeira.append({'codigo':j[3],'cod_internet':j[2],'custo':j[1],'dados':j})
        elif len(j) == 6:
            lista_produtos_verdadeira.append({'codigo':j[4],'cod_internet':j[3],'custo':j[2],'dados': j})
        elif len(j) == 7:
            lista_produtos_verdadeira.append({'codigo':j[5],'cod_internet':j[4],'custo':j[2],'dados': j})
        else:
            pass
'''
with open(path_home+'/ProjetoSidnei/Dados_html/Lista_Produtos_Site.json', 'w') as f:
    json.dump(lista_produtos_verdadeira,f)
'''
with open(path_home+'/ProjetoSidnei/produtos.json', 'r') as f:
    produtos = json.load(f)
'''
for i in lista_produtos_verdadeira:
    print(i['codigo'])

for i in produtos:
    print(i)
'''

def buscaCodigoProdutoLista(codigo, lista_produtos_site):
    preco = 'ERRO'
    for i in lista_produtos_site:
        if i['codigo'] == codigo:
            preco = i['custo']
            break
    return preco


print(len(produtos))
produtos2 = []

for i in produtos:
    produtos2.append({'codigo':i['codigo'],'nome_produto':i['nome_produto'],'custo':buscaCodigoProdutoLista(i['codigo'],lista_produtos_verdadeira)})

'''
with open(path_home+'/ProjetoSidnei/Produtos2.json', 'w') as f:
    json.dump(produtos2,f)

t = 0
for i in produtos2:
    if i['custo'] == 'ERRO':
        t = t+1
    if i['custo'] != 'ERRO':
        print(i)
print('\n\n\n\n\n')
for i in produtos2:
    if i['custo'] == 'ERRO':
        print(i)
print('Total de ERROS: '+str(t))
print('Diferenca: '+str(len(produtos2)-t))
'''



#print('\n\n')
#print(lista_produtos[1])



'''

with open(path_home+'/ProjetoSidnei/Dados_html/Teste.txt','w') as f:
    for i in lista_produtos:
        #f.write(i[8]+' '+i[5].replace(' ','')+'\n') #Um dos codigos e o preco da revista
        f.write(str(i)+'\n')
'''
for i in produtos2:
    print(i)

