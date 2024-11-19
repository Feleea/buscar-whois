from _geral import *
from bs4 import BeautifulSoup
import requests



class whois():
    def __init__(self, asNumber="", requisicao=True) -> None:
        
        self.asNumber = asNumber
        self.asNumber2 = ""
        self.asName = ""
        self.whois = []

        if requisicao == 0: self.navegador = False
        else: self.navegador = abrir_navegador()


    def bgpview(self):
        navegador = self.navegador

        def _acessar_site():
            navegador.get("https://bgpview.io/")
            navegador.find_element(By.NAME, "query_term").send_keys(self.asNumber)
            try: navegador.find_element(By.ID, "hs-eu-confirmation-button").click()
            except: pass
            navegador.find_element(By.CLASS_NAME, "btn.btn-default").click()
            WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "resource-content")))

        def _pegar_whois():

            navegador.find_element(By.ID, "nav-whois").click()
            texto = navegador.find_element(By.ID, "content-whois").text
            lista_itens = [item.split(": ") for item in texto.split("\n")]
            for  coisa in lista_itens:
                if 'aut-num' in coisa: 
                    self.asNumber2 = coisa[1].strip()
                    continue
                if 'owner' in coisa:
                    self.asName = coisa[1].strip()
                    continue
                if 'inetnum' in coisa:
                    self.whois.append(coisa[1].strip())
                    continue
                    
        def _request_whois():
            html = requests.get(f"https://bgpview.io/asn/{self.asNumber[2:]}#whois").text
            soup = BeautifulSoup(html,'html.parser').find_all("pre")

            lista_itens = [item.split(": ") for item in soup[0].get_text().split("\n")] 
            for coisa in lista_itens:
                if 'aut-num' in coisa: 
                    self.asNumber2 = coisa[1].strip()
                    continue
                if 'owner' in coisa:
                    self.asName = coisa[1].strip()
                    continue
                if 'inetnum' in coisa:
                    self.whois.append(coisa[1].strip())
                    continue

        def scrap_bgpview():
            if navegador:
                _acessar_site()
                _pegar_whois()

            else: _request_whois()
            
            return self.asNumber2, self.asName, self.whois


        return scrap_bgpview()
    
    
    def bgp(self):
        navegador = self.navegador

        def _acessar_site():
            navegador.get(f"https://bgp.he.net/{self.asNumber}#_whois")
            WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, "whois")))

        def _pegar_whois():
            textInfo = navegador.find_element(By.ID, "whois").text
            if "unavailable" in textInfo: 
                self.asNumber2 = "Não foi possível localizar o AS number"
                self.asName = "Não foi possível localizar o nome da empresa"
                return

            texto = navegador.find_element(By.ID, "whois").text
            lista_itens = [item.split(": ") for item in texto.split("\n")]
            for  coisa in lista_itens:
                if 'aut-num' in coisa: 
                    self.asNumber2 = coisa[1].strip()
                    continue
                if 'owner' in coisa:
                    self.asName = coisa[1].strip()
                    continue
                if 'inetnum' in coisa:
                    self.whois.append(coisa[1].strip())
                    continue

        def _request_whois():
            html = requests.get(f"https://bgp.he.net/{self.asNumber}#_whois").text
            soup = BeautifulSoup(html,'html.parser').find_all("pre")

            lista_itens = [item.split(": ") for item in soup[0].get_text().split("\n")] 
            for coisa in lista_itens:
                if 'aut-num' in coisa: 
                    self.asNumber2 = coisa[1].strip()
                    continue
                if 'owner' in coisa:
                    self.asName = coisa[1].strip()
                    continue
                if 'inetnum' in coisa:
                    self.whois.append(coisa[1].strip())
                    continue


        def scrap_bgp():
            if navegador:
                _acessar_site()
                _pegar_whois()

            else: _request_whois()

            return self.asNumber2, self.asName, self.whois
        
        return scrap_bgp()