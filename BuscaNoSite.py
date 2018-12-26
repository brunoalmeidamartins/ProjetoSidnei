import time
import os
import json
from selenium import webdriver


path_home = os.getenv("HOME") #Captura

def acesso():
    arq = open(path_home+'/LojaSidnei/Avon.txt','r')
    texto = arq.read()
    arq.close()
    vet = texto.split(',')
    user = vet[0]
    pwd = vet[1]
    return user, pwd



user, pwd = acesso()



driverpath = path_home+'/ProjetoSidnei/chromedriver'
driver = webdriver.Chrome(driverpath)

driver.get('http://www.google.com.br')

time.sleep(2)

#Buscando alguma coisa
elem = driver.find_element_by_name('q').send_keys("Bruno Almeida")
#bt_pesquisa = driver.find_element_by_name('btnK')
#bt_pesquisa.click()
bt_pesquisa = driver.find_element_by_xpath('//div[@class="FPdoLc VlcLAe"]//input[@value="Pesquisa Google"]')
print(bt_pesquisa.get_attribute('value'))
bt_pesquisa.click()

time.sleep(5)
driver.close()
