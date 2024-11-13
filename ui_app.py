import context
from tkinter import *
from tkinter import ttk, font, messagebox, Listbox
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
    # ------------------------------------------------------------------------ COLOR LIST
    color_white = "#ffffff"
    color_blue_label = "#014654"
    # ------------------------------------------------------------------------ COLOR LIST
    # ------------------------------------------------------------------------ STYLE LIST
    tittle_Font = font.Font(name='sisvisatitle_Font', size=16, weight='bold')
    ttk.Style().configure('FundoBranco.TFrame', background=color_white)
    ttk.Style().configure('FundoAzul.TFrame', background='blue')
    ttk.Style().configure('FundoLAzul.TLabel', background='#017991')
    ttk.Style().configure('Fundo.TFrame', background='blue')
    ttk.Style().configure('FundoBranco.TSeparator', background=color_white)

    # ------------------------------------------------------------------------ STYLE LIST
    # ------------------------------------------------------------------------ VARIABLES LIST
    asBuscado = StringVar(value="AS53182")
    columVar = IntVar(value=0)
    cardList = []
    sitedeBuscaVar = StringVar(value=f"{geral.sites_list()[0]}")
    # ------------------------------------------------------------------------ VARIABLES LIST
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
                card, style='FundoLAzul.TLabel',
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
    mainframe = ttk.Frame(janela, padding="5 5", style='FundoBranco.TFrame')
    mainframe.grid(column=0, row=0)

    headFrame = ttk.Frame(mainframe, padding="0 5 0 0", style='FundoBranco.TFrame') # Esquerda, cima, direita, baixo
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
    configFrameTitle = ttk.Label(configFrame, text="Configurações", style='FundoLAzul.TLabel', anchor=CENTER)
    configFrameTitle.grid(column=0, row=0, columnspan=3, sticky=EW)

    configSubTitleUm = ttk.Label(configFrame, text="Realizar a busca em:")
    configSubTitleUm.grid(column=0, row=1)
    buscarEntry = ttk.Combobox(configFrame, values=geral.sites_list(), textvariable=sitedeBuscaVar)
    buscarEntry.grid(column=0, row=2)

    bodyFrame = ttk.Frame(mainframe, style='FundoBranco.TFrame')
    bodyFrame.grid(column=0, row=2)
    

    # ------------------------------------------------------------------------ FRAMES

    # ------------------------------------------------------------------------ LOGO + H1
    ttk.Label(mainframe, text="Salve salve familia:", font=tittle_Font,
            padding=(0, 10), anchor='center', foreground=color_white,
            background=color_blue_label).grid(column=0, row=0, sticky=EW)
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