# coding: utf-8
#! / usr / bin / python

# Projeto de login automático em site

## Bibliotecas:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from configparser import RawConfigParser
from datetime import datetime
from random import random

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
passw=params['password']
#Pasta com o executável do chromedriver.exe:
executable_path=params['executable_path'] 

## Intervalo de tempo para a abertura do navegador:
n = random()
time.sleep(n*100)

## Abertura do navegador:
inicio=datetime.now()
print(f'Iniciando o processo de abertura do navegador...')
### Tratamento de Erros:
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
### Acesso ao navegador:
try:
    browser = webdriver.Chrome(options=options)
except:
    browser = webdriver.Chrome(options=options,executable_path=executable_path)
fim=datetime.now()
print(f'Navegador aberto. Tempo de Execução: {fim-inicio}.')

## Acesso ao site de login:
browser.get(site) 
inicio=datetime.now()
print(f'Iniciando processo de abertura do site {site}...')
fim=datetime.now()
print(f'{site} acessado com sucesso. Tempo de Execução: {fim-inicio}.')
time.sleep(5) 

## Login:
inicio=datetime.now()
### Abertura da tela de login:
try:
    browser.find_element_by_link_text('LOGIN').click()
except:
    print(f'ERRO! Botão de login não pressionado.')    
print(f'Definição dos parâmetros de login...')
### Pausa para atualização dos dados:
time.sleep(5)
### Definição de usuário:
browser.find_element_by_id('mat-input-0').send_keys(user)
### Definição de senha:
browser.find_element_by_id('mat-input-1').send_keys(passw)
### Selecionando o botão de login:
try:
    browser.find_element_by_xpath("//button[text()=' ENTRAR ']").click()
    fim=datetime.now()
    print(f'Login efetuado com sucesso. Tempo de Execução: {fim-inicio}.')
except:
    print(f'ERRO! Botão "Logar-se" não pressionado.')  

## Intervalo de tempo para fechar o navegador:
n = random()
time.sleep(n*100)

## Fechamento do navegador:
browser.close()
