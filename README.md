<h1 align="center">Teste técnico QA - TOTVS</h1>

> ***Este repositório tem por objetivo disponibilizar o teste técnico de QA para a avaliação do mesmo pela empresa.***

1. <a href="#ExecAuto">Execução da Automação (Front-end)</a> </br>
  1.2  <a href="ReqExec">Requisitos para a execução</a> 
    1. <a href="Linux">Linux</a> 
    2. <a href="Windows">Windows</a>
  1.3 <a href="Exec">Execução dos s</a> </br>
2. <a href="#ExecAutoBack">Execução da Automação (Back-end)</a> </br>
  
<div id="ExecAuto"></div>

# Execução da automação de funcionalidades Front-end
A automação por si, foi feita em python (em sua versão 3.8+) sendo utilizado juntamente com o Selenium WebDriver.

<div id="ReqExec"></div>

## Requisitos para a execução dos s:

<div id="Linux"></div>

### Linux:
  - Python 3.8+ (Nativo nas versões mais recentes);
  - pip3 (gerenciador de pacotes do Python3)
    ```console
    foo@bar:~$ sudo apt install python3-pip
    ```
  - Importação da biblioteca dentro da pasta do projeto:
    ```console
    foo@bar:~$ pip3 install selenium
    ```
    
<div id="Windows"></div>

### Windows:
  - Instalação do gerenciador de pacotes [Chocolatey](https://chocolatey.org/install):
  - Via `PowerShell` (como Administrador)
    - Instalação do Python 3.8:
     ```console
     foo@bar:~$ choco install python --version=3.8.0
     ```
    - Instalação do pip3:
     ```console
     foo@bar:~$ choco install pip3
     ```
    - Importação da biblioteca dentro da pasta do projeto:
     ```console
     foo@bar:~$ pip3 install selenium
     ```

<div id="Exec"></div>

## Execução dos scripts:
  - Abrir o terminal (Linux) ou `PowerShell` (Windows) e executar:
   ```console
   foo@bar:~$ python3 test1.py
   ```
  - Após executado este e fechado o navegador, executar o segundo :
   ```console
   foo@bar:~$ python3 test2.py
   ```
   
---

<div id="ExecAutoBack"></div>

# Execução da automação de funcionalidade Back-end
Teste realizados via Postman e exportados deste, apenas importar o arquivo `qa-challenge-backend.postman_collection` e executar internamente.
