from _geral import *



class whois():
    def __init__(self, asNumber) -> None:
        
        self.navegador = abrir_navegador(is_navegador=True)
        self.asNumber = asNumber
        self.asNumber2 = ""
        self.asName = ""
        self.whois = []


    def bgpview(self):
        navegador = self.navegador

        def _acessar_site():
            navegador.get("https://bgpview.io/")
            navegador.find_element(By.NAME, "query_term").send_keys(self.asNumber)
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
                    

        def scrap_bgpview():
            _acessar_site()
            _pegar_whois()
            
            fechar_navegador()

            return self.asNumber2, self.asName, self.whois


        return scrap_bgpview()
    
    
    def coming_soon(self):
        pass
    