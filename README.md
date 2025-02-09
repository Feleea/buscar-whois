# Buscar Whois
 
# Objetivo:
 Esse programa tem como objetivo facilitar a consulta de Whois dos ASNubers das operadoras de redes de internet

# utilização:
 Ao abrir o programa é só informar o ASNunber que deseja encontrar o Whois
 * Você pode buscar por vários ASN's separados por virgula
    * Ex.: AS123,AS124,AS125, AS126, AS127
 * Também é possível consultar em sites diferentes ao selecionar nas configurações
 * Você pode exportar toda busca em um arquivo .txt ao selecionar nas configurações

 ![2024-12-08-21-44-20](https://github.com/user-attachments/assets/6a03ae4e-1a77-45ad-bb8d-0130712db4bd)


# Como instalar:

 ### 1. Criar ambiente virtual no VScode
 * ctrl + shifit + P > Python: Create Environment

 ### 2. Ativar o ambiente virtual
 ```bash
 .venv\Scripts\Activate.ps1
 ```

 ### 3. Instalar as bibliotecas
 * Durante a criação do ambiente virtual o VS code também pergunta se você deseja instalar as dependencias e deixa esse arquivo como sugestão, é só selecionar ele e continuar com a criação do ambiente virtual. Caso isso não ocorra, instale as bibliotecas com a linha abaixo no terminal.
 ```bash
 pip install -r requirements.txt
 ```

 # Executar:

 ```bash
 python ui_app.py
 ```
