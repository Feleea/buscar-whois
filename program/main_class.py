from _geral import *



class whois():
    def __init__(self) -> None:
        
        self.navegador = abrir_navegador(is_navegador=True)


    def primeiro_site(self):
        self.navegador.get("https://bgpview.io/")