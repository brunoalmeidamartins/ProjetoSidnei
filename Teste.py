import os
import json
path_home = os.getenv("HOME") #Captura o caminho da pasta HOME

arq = open(path_home+'/ProjetoSidnei/Avon_Folheto_Cosmeticos_3_2019.txt', 'r')

texto = arq.read()

arq.close()

print(texto)

produtos = texto.split(',')
print('Tamanho da Lista = '+str(len(produtos)))

produtos2 = []

for i in produtos:
    if i[0] == ' ':
        texto = ''
        for j in range(len(i)):
            if j > 0:
                texto = texto + i[j]
        i = texto
    produtos2.append(i)
produtos2.remove('')
codigos_produtos = []

for i in produtos2:
    vet = i.split(' ')
    codigos_produtos.append(vet[0])

produtos = []
for i in produtos2:
    texto = ''
    for j in range(len(i)):
        if j > 6:
            texto = texto + i[j]
    produtos.append(texto)

# Tenho dois vetores: 1 de codigo e outro de nome do produto
lista_produtos = []

for i in range(len(codigos_produtos)):
    lista_produtos.append({'codigo':codigos_produtos[i],'nome_produto':produtos[i]})
print(lista_produtos)

#Leitura
#produtos = open('produtos.json','r')
#json.load(produtos)

#Escrita
#arq = open('produtos.json', 'w')
#jsom.dump('lista','arq')

'''
#Escrita no arquivo
arq = open('produtos.json','w')
json.dump(lista_produtos,arq)
arq.close()
'''

#Abertura do arquivo
arq = open('produtos.json','r')
produtos = json.load(arq)
arq.close()

for i in produtos:
    print(i['codigo'])


print('FIM')

