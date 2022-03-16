# coding: utf-8
#! / usr / bin / python

# Projeto de login automático em site

## Bibliotecas:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from configparser import RawConfigParser

## Funções:
def config(filename, section): 
    parser = RawConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db [param [0]] = param [1]
    else:
        raise Exception ('Seção {0} não encontrada no {1} arquivo'.format (section, filename))
    return db

## Variáveis Globais:
site='https://sociotorcedor.com.br/'
params=config('auth.ini','login')
user=params['user']
password=params['password']

## Abetura do navegador:
print(f'Iniciando o processo de abertura do navegador...')
options = webdriver.ChromeOptions() # Tratamento de erro
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Tratamento de erro
browser = webdriver.Chrome(options=options) # Tratamento de erro
print(f'Navegador aberto.')

## Acesso ao site de login:
browser.get(site) 
print(f'Iniciando processo de abertura do site {site}...')
print(f'{site} acessado com sucesso.')
time.sleep(10) 

## Login:
browser.find_element_by_name("mat-input-2/mat-input-element mat-form-field-autofill-control ng-tns-c60-8 ng-pristine ng-valid cdk-text-field-autofill-monitored ng-touched/name of username").send_keys(user)
time.sleep(30)
#username = browser.find_element_by_id("matinput")
#password = browser.find_element_by_id("password")
#username.send_keys(user)
#password.send_keys(password)
#login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#login_attempt.submit()
#ids = browser.find_elements_by_xpath('//*[@class]')
#for ii in ids:
    #print ii.tag_name
    #print(ii.get_attribute('class'))    # id name as string


## Fechamento do navegador:
print('Navegador fechado.')
#browser.close()
