# Teste técnico QA - TOTVS
Este repositório tem por objetivo disponibilizar o teste técnico de QA para a avaliação do mesmo pela empresa.

# Execução da automação de funcionalidades Front-end
A automação por si, fora feita em python (em sua versão 3.8+) sendo utilizado juntamente com o Selenium WebDriver.

## Requisitos para a execução dos scripts:
### Linux:
  - Python 3.8+ (Nativo nas versões mais recentes);
  - pip3 (gerenciador de pacotes do Python3)
    - `sudo apt install python3-pip`
  - Importação da biblioteca dentro da pasta do projeto:
    - `pip3 install selenium`
### Windows:
  - Instalação do gerenciador de pacotes Chocolatey:
    - https://chocolatey.org/install
  - Via PowerShell (como Administrador)
    - Instalação do Python 3.8:
      - `choco install python --version=3.8.0`
    - Instalação do pip3:
      - `choco install pip3`
    - Importação da biblioteca dentro da pasta do projeto:
      - `pip3 install selenium`

## Execução dos scripts:
  - Abrir o terminal (linux) ou PowerShell (Windows) e executar:
    - `python3 test1.py`
    - Após executado este e fechado o navegador, executar o segundo script;
    - `python3 test2.py`
    
# Execução da automação de funcionalidade Back-end
Teste realizados via Postman e exportados deste, apenas importar o arquivo `qa-challenge-backend.postman_collection` e executar internamente.
