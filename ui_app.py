import context
from tkinter import *
from tkinter import ttk, font, messagebox
import program._geral as geral
import program.main_class as whois
from threading import Thread


def ui_whois():
    # ------------------------------------------------------------------------ CONFIG UI
    janela = Tk()
    janela.title("Buscar Whois")
    # janela.geometry("350x210")  # Largura x Altura
    janela.iconphoto(False, PhotoImage(file=geral.procurar_arquivos("dance.gif")))
    janela.resizable(width=False, height=False)
    # ------------------------------------------------------------------------ CONFIG UI
    # ------------------------------------------------------------------------ VARIABLES LIST
    asBuscado = StringVar(value="AS53182")
    columVar = IntVar(value=0)
    cardList = []
    sitedeBuscaVar = StringVar(value=f"{geral.sites_list()[0]}")
    temaVar = StringVar()
    verNavegador = IntVar(value=0)
    # ------------------------------------------------------------------------ VARIABLES LIST
    # ------------------------------------------------------------------------ COLOR LIST
    def temas(event):
        
        if "Claro" in event:
            corFundoPadrao = "#ffffff"
            corFundoTitulo = "#014654"
            corFonteTitulo = "#ffffff"
            corFundoSubTitulo = "#017991"
            corFonteSubTitulo = "#000000"

        else:
            corFundoPadrao = "#2e2e2e"
            corFundoTitulo = "#111"
            corFonteTitulo = "#ffffff"
            corFundoSubTitulo = "#bbc7c9"
            corFonteSubTitulo = "#ffffff"
        
        # ------------------------------------------------------------------------ STYLE LIST
        ttk.Style().configure('FundoTelaPrincipal.TFrame', background=corFundoPadrao)
        ttk.Style().configure('Titulo.TLabel', background=corFundoTitulo, foreground=corFonteTitulo)
        ttk.Style().configure('FundoCardTitulo.TLabel', background=corFundoSubTitulo)
        ttk.Style().configure('FundoBranco.TSeparator', background=corFundoPadrao)

        # ------------------------------------------------------------------------ STYLE LIST
    # ------------------------------------------------------------------------ COLOR LIST

    temas("Claro")
    # ------------------------------------------------------------------------ FUNCTIONS LIST
    def buscar():

        if validation(): return
        criar_cards()

    def criar_cards():

        asNumberString = asBuscado.get()

        def _criar_cards(asNumber: str, index=0):

            program.asNumber = asNumber.strip()

            if len(cardList) // 3 == 1: 
                columCont = columVar.set(columVar.get()+1)
                index -= 3
            if len(cardList) // 3 == 2: 
                columCont = columVar.set(columVar.get()+2)
                index -= 3
            else: columCont = columVar.get()

            card = ttk.Frame(bodyFrame, padding="2 2", relief=GROOVE)
            card.grid(column=columCont, row=index, padx=10, pady=10)
            cardTitle = ttk.Label(
                card, style='FundoCardTitulo.TLabel',
                text=f"Busca realizada às {geral.datetime.today().strftime("%H:%M:%S")} - Fonte: {sitedeBuscaVar.get()}", anchor=CENTER)
            cardTitle.grid(column=0, row=0, sticky=NSEW)
            cardBody = ttk.Frame(card, padding="5 0 5 5")
            cardBody.grid(column=0, row=1)
            cardBodyContent = Text(cardBody, width=45, height=9)
            cardBodyContent.grid(column=0, row=0)
            cardList.append(card)

            if geral.sites_list()[0] in sitedeBuscaVar.get(): info = program.bgpview()
            if geral.sites_list()[1] in sitedeBuscaVar.get(): info = program.bgp()

            cardBodyContent.insert(END, info[0] + " - " + info[1] + "\n")
            for i in info[2]:
                cardBodyContent.insert(END, i + f" {info[0][2:]}\n")
                program.asNumber2 = ""
                program.asName = ""
                program.whois = []


        program = whois.whois()
        apagarCards()
        if "," in asNumberString:
            asNumberList = asNumberString.split(",")
            for index, asNumber in enumerate(asNumberList): _criar_cards(asNumber, index)
        else:
            _criar_cards(asNumber=asNumberString)

        geral.fechar_navegador(program.navegador)


    def validation():
        tittle_text = "Não foi possível continuar"

        if asBuscado.get() == "" or asBuscado.get() == " ": 
            messagebox.showinfo(message="Preencha uma informação válida para buscar", title=tittle_text)
            return True
        
        if "AS" not in asBuscado.get():
            messagebox.showinfo(message='Realize a busca do troço com o "AS" na frente', title=tittle_text)
            return True
        
        return False
    
    def limpar_entry_email(event):
        buscarWhois.delete(0, END)
        buscarWhois.configure(foreground="black")

    def apagarCards():
            for i in cardList: i.destroy()
            cardList.clear()


    # ------------------------------------------------------------------------ FUNCTIONS LIST

    # ------------------------------------------------------------------------ FRAMES
    mainframe = ttk.Frame(janela, padding="5 5", style='FundoTelaPrincipal.TFrame')
    mainframe.grid(column=0, row=0)

    headFrame = ttk.Frame(mainframe, padding="0 5 0 0", style='FundoTelaPrincipal.TFrame') # Esquerda, cima, direita, baixo
    headFrame.grid(column=0, row=1, pady=5)

    contornoHeadFrame = ttk.Frame(headFrame, padding="10 10 10 10", relief=GROOVE)
    contornoHeadFrame.grid(column=0, row=0)
    buscarWhois = ttk.Entry(contornoHeadFrame, textvariable=asBuscado, foreground="gray", width=25)
    buscarWhois.grid(column=0, row=0, ipady=3)
    buttonbuscarWhois = ttk.Button(
        contornoHeadFrame, text="Buscar", command=lambda: Thread(target=buscar).start())
    buttonbuscarWhois.grid(column=1, row=0, ipady=2)
    
    separinhoBusca = ttk.Separator(contornoHeadFrame, orient="vertical")
    separinhoBusca.grid(column=2, row=0, sticky=NS, padx=10)

    configFrame = ttk.Frame(contornoHeadFrame)
    configFrame.grid(column=3, row=0)
    configFrameTitle = ttk.Label(configFrame, text="Configurações", style='FundoCardTitulo.TLabel', anchor=CENTER)
    configFrameTitle.grid(column=0, row=0, columnspan=4, sticky=EW)

    configSubTitleUm = ttk.Label(configFrame, text="Realizar a busca em:")
    configSubTitleUm.grid(column=0, row=1)
    sitesList = geral.sites_list()
    buscarEntry = ttk.OptionMenu(configFrame, sitedeBuscaVar, geral.sites_list()[0], *sitesList)
    buscarEntry.grid(column=0, row=2)

    separinhoConfigUm = ttk.Separator(configFrame, orient="vertical")
    separinhoConfigUm.grid(column=1, row=1, rowspan=2, sticky=NS, padx=10)

    configSubTitleDois = ttk.Label(configFrame, text="Aparência:")
    configSubTitleDois.grid(column=2, row=1)
    temasList = ["Tema Claro", "Tema Escuro"]
    aparenciaScale = ttk.OptionMenu(configFrame, temaVar, temasList[0], *temasList, command=temas)
    aparenciaScale.grid(column=2, row=2)

    bodyFrame = ttk.Frame(mainframe, style='FundoTelaPrincipal.TFrame')
    bodyFrame.grid(column=0, row=2)
    
    # ------------------------------------------------------------------------ FRAMES

    # ------------------------------------------------------------------------ LOGO + H1
    fonteTitulo = font.Font(name='Maintitle.Font', size=16, weight='bold')
    ttk.Label(mainframe, text=f"{geral.frases()}:", font=fonteTitulo, padding=(0, 10),
              style='Titulo.TLabel', anchor=CENTER).grid(column=0, row=0, sticky=EW)
    # ------------------------------------------------------------------------ LOGO + H1

    # ------------------------------------------------------------------------ CHOICES
    

    # ------------------------------------------------------------------------ CHOICES

    # ------------------------------------------------------------------------ FOOT
    
    
    # ------------------------------------------------------------------------ FOOT

    # ------------------------------------------------------------------------ EVENTS
    buscarWhois.bind('<Button-1>', limpar_entry_email) # Limpar Entry de usuário e senha
    # ------------------------------------------------------------------------ EVENTS

    # ------------------------------------------------------------------------ RUN WINDOWS
    janela.mainloop()
    # ------------------------------------------------------------------------ RUN WINDOWS

if __name__ == '__main__':
    ui_whois()