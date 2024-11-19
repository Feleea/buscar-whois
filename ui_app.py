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
    columContVar = IntVar(value=0)
    rowContVar = IntVar(value=0)
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

        apagarCards()
        if validation(): return
        criarProgressBar()
        criar_cards()
        apagarProgressBar()
        rowContVar.set(0)
        columContVar.set(0)


    def criar_cards():

        def _criar_cards(asNumber: str):

            program.asNumber = asNumber.strip()

            card = ttk.Frame(bodyFrame, padding="2 2", relief=GROOVE)
            card.grid(column=columContVar.get(), row=rowContVar.get(), padx=10, pady=10)
            cardTitle = ttk.Label(
                card, style='FundoCardTitulo.TLabel',
                text=f"Busca realizada às {geral.datetime.today().strftime("%H:%M:%S")} - Fonte: {sitedeBuscaVar.get()}", anchor=CENTER)
            cardTitle.grid(column=0, row=0, sticky=NSEW)
            cardBody = ttk.Frame(card, padding="5 0 5 5")
            cardBody.grid(column=0, row=1)
            cardBodyContent = Text(cardBody, width=45, height=9)
            cardBodyContent.grid(column=0, row=0)

            calcularLinhaColuna()

            if geral.sites_list()[0] in sitedeBuscaVar.get(): info = program.bgpview()
            if geral.sites_list()[1] in sitedeBuscaVar.get(): info = program.bgp()

            cardBodyContent.insert(END, info[0] + " - " + info[1] + "\n")
            for i in info[2]:
                cardBodyContent.insert(END, i + f" {info[0][2:]}\n")
                program.asNumber2 = ""
                program.asName = ""
                program.whois = []


        program = whois.whois(requisicao=verNavegador.get())
        asNumberString = asBuscado.get()

        if "," in asNumberString:
            asNumberList = asNumberString.split(",")
            for asNumber in asNumberList: _criar_cards(asNumber)
        else:
            _criar_cards(asNumber=asNumberString)

        geral.fechar_navegador(program.navegador)


    def calcularLinhaColuna():
        rowContVar.set(rowContVar.get()+1)
        if rowContVar.get() == 3 or rowContVar.get() == 6:
            columContVar.set(columContVar.get()+1)
            rowContVar.set(0)

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
        for filho in bodyFrame.winfo_children(): filho.destroy()

    def criarProgressBar():
        barraProgressoFrame.grid(column=0, row=2)
        ttk.Label(barraProgressoFrame, text="Buscando informações",
                  style='FundoCardTitulo.TLabel', anchor="center").grid(column=0, row=0, sticky=EW)
        pb_hd = ttk.Progressbar(barraProgressoFrame, mode='indeterminate', length=250)
        pb_hd.grid(column=0, row=1, pady=5)
        pb_hd.start()

    def apagarProgressBar():
        barraProgressoFrame.grid_remove()
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
    ttk.Separator(contornoHeadFrame, orient="vertical").grid(column=2, row=0, sticky=NS, padx=10)

    configFrame = ttk.Frame(contornoHeadFrame)
    configFrame.grid(column=3, row=0)
    configFrameTitle = ttk.Label(configFrame, text="Configurações", style='FundoCardTitulo.TLabel', anchor=CENTER)
    configFrameTitle.grid(column=0, row=0, columnspan=4, sticky=EW)

    usarNavegador = ttk.Checkbutton(configFrame, text="Visualizar navegador", variable=verNavegador)
    usarNavegador.grid(column=0, row=1, ipady=5)
    ttk.Separator(configFrame).grid(column=0, row=2, columnspan=3, sticky=EW)

    configSubTitleUm = ttk.Label(configFrame, text="Realizar a busca em:")
    configSubTitleUm.grid(column=0, row=3)
    sitesList = geral.sites_list()
    buscarOptions = ttk.OptionMenu(configFrame, sitedeBuscaVar, sitesList[0], *sitesList)
    buscarOptions.grid(column=1, row=3, ipady=5)
    ttk.Separator(configFrame).grid(column=0, row=4, columnspan=3, sticky=EW)

    configSubTitleDois = ttk.Label(configFrame, text="Aparência:")
    configSubTitleDois.grid(column=0, row=5)
    temasList = ["Tema Claro", "Tema Escuro"]
    aparenciaScale = ttk.OptionMenu(configFrame, temaVar, temasList[0], *temasList, command=temas)
    aparenciaScale.grid(column=1, row=5)

    barraProgressoFrame = ttk.Frame(mainframe, padding="10 10 10 10", relief=GROOVE)
    

    bodyFrame = ttk.Frame(mainframe, style='FundoTelaPrincipal.TFrame')
    bodyFrame.grid(column=0, row=4)
    
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