from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from winotify import Notification, audio
import random
import os
import time
import functools
from datetime import datetime



def abrir_navegador(is_navegador: bool) -> webdriver.Chrome:
        
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument("--log-level=3")
        if not is_navegador: options.add_argument("--headless=new")

        navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        navegador.implicitly_wait(3)

        return navegador


def fechar_navegador(navegador: webdriver.Chrome):
    try: navegador.quit()
    except: pass


def sites_list():
    """AS53013 - W I X N E T DO BRASIL
        177.67.X.X/22 53013
        2804:020:X:X/128 53013"""

    sites = ("https://bgpview.io/", "https://bgp.he.net/") # , "https://bgp.tools/", "https://www.peeringdb.com/"

    return sites



def criar_email_provisorio_moakt(nome=f"agente {random.randint(1,99999)}"):
    navegador_email = abrir_navegador(headless=True)
    navegador_email.get("https://moakt.com")
    navegador_email.refresh()
    navegador_email.find_element(By.NAME, "username").send_keys(str(f"{nome}"))
    navegador_email.find_element(By.NAME, "setemail").click()
    email = navegador_email.find_element(By.ID, "email-address").text
    print(f"E-mail {email} provisório criado.")
    return email, navegador_email


def win_notification(msg: str):
    notificacao = Notification(app_id="Cadastro Automatico",
                                title="Notificação da Automação",
                                msg=msg)
    # notificacao.add_actions(label="Abrir navegador", launch=navegador.maximize_window())
    notificacao.set_audio(audio.Reminder, loop=False)
    notificacao.show()


def stop(navegador: webdriver.Chrome, skip_stop: bool):
    '''skip_stop = True -> Pula em caso de coicidência\n
       skip_stop = False -> Pausa por 600 segundos'''

    if skip_stop: return

    win_notification("Automação concluida. A tela ficará aberta por 10 minutos antes de fechar sozinha.")
    print("######################## Em pausa ########################")
    time.sleep(600)
    fechar_navegador(navegador)



# Decorador de log no terminal e erros
def log_terminal_automacao(mensagem: str):

    def dale(funcao):

        @functools.wraps(funcao)
        def wrapper(*args, **kwargs):
            erros = 5
            navegador = args[0].navegador
            print(f"{mensagem}", end="\r")

            while True:

                try:
                    result = funcao(*args, **kwargs)
                    print(f"{mensagem} ... \033[32mConcluído.\033[0m")
                    break

                except StaleElementReferenceException:
                    if 'PGLS_site.criar_empresa.<locals>._preencher_segunda_pagina_do_cadastro' in funcao.__qualname__: continue

                except ElementClickInterceptedException: # ESSA POCA QUANDO ESTOU REMOVENDO UMA EMPRESA E TENTO MUDAR O USUÁRIO
                    if 'PGLS_admin._alterar_usuario_CNPJ' in funcao.__qualname__: 
                        navegador.refresh()
                        continue
                    
                except Exception as e:
                    erros -= 1
                    if erros > 0:
                        print(f"{mensagem} ... \033[31mErro. Tentando novamente... \033[0m")
                        navegador.refresh()

                    else:
                        try: 
                            navegador.execute_script("alert('Deu erro aqui viu');")
                            time.sleep(300)
                            navegador.quit()
                            print("Finalizando o programa...", end="\r")

                        except ConnectionRefusedError:
                            print("Conexão encerrada com o programa")
                            break

                        except NoSuchElementException:
                            print("Não encontrou o elemento html", e)
                            break

            return result
        
        return wrapper
    
    return dale


def procurar_arquivos(nome_arquivo) -> str:
    caminho_atual = os.path.realpath(__file__)
    diretorio_raiz = os.path.dirname(os.path.dirname(caminho_atual))
    
    # Caminha recursivamente pelo diretório raiz e subdiretórios
    for dirpath, dirnames, filenames in os.walk(diretorio_raiz):
        for filename in filenames:
            if nome_arquivo in filename:
                # Adiciona o caminho completo do arquivo encontrado
                return os.path.join(dirpath, filename)
    
    return nome_arquivo


def procurar_pasta(nome_pasta):
    caminho_atual = os.path.realpath(__file__)
    diretorio_raiz = os.path.dirname(os.path.dirname(caminho_atual))
    
    # Caminha recursivamente pelo diretório raiz e subdiretórios
    for dirpath, dirnames in os.walk(diretorio_raiz):
        for dirname in dirnames:
            if nome_pasta in dirname:
                # Adiciona o caminho completo da pasta encontrado
                return os.path.join(dirpath, dirname)
        return 
    
