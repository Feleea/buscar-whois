from _geral import *



class whois():
    def __init__(self, target) -> None:
        
        self.navegador = abrir_navegador(is_navegador=True)
        self.target = target


    def primeiro_site(self):
        navegador = self.navegador

        def acessar_site():
            navegador.get("https://bgpview.io/")
            navegador.find_element(By.NAME, "query_term").send_keys(self.target)
            navegador.find_element(By.CLASS_NAME, "btn.btn-default").click()
            WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "resource-content")))
            print(sleep(300))

        def pegar_whois():
            pass
