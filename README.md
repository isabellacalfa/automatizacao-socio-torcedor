# Projeto para automatização de ações no site sociotorcedor.com.br

**Projeto em desenvolvimento.**

## 1. Pré-Requisitos:
O projeto foi realizado utilizando o navegador Google Chrome, mas pode ser aplicado em outros navegadores após ajustes no driver utilizado e funções.

## 2. Preparação:
### 2.1 Bibliotecas:
Antes de executar o código, é necessário garantir que as bibliotecas necessárias estejam instaladas (*! pip install*) e é preciso que o *chromedriver.exe* (da bib **webdriver**) esteja incluído no PATH do sistema (no PC: Editar Variáveis de Ambiente > Variáveis de Ambiente ... > Path > Editar).

### 2.2 Arquivo auth.ini:
O arquivo auth.ini deve ser no seguinte formato:

[login]
user=your username<br/>
password=your password<br/>
executable_path=pasta do chromedriver.exe

## 3. Ações disponíveis:
### 3.1 Login
A ação pode ser executada através do *login_st.py* e consiste em passar usuário e senha disponibilizados no arquivo *auth.ini* para realizar login no site.