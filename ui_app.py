import context
from tkinter import *
from tkinter import ttk, font, messagebox, Listbox
from PIL import Image, ImageTk
import program._geral as geral
import program.main_class as whois
import threading


def ui_whois():
    # ------------------------------------------------------------------------ CONFIG UI
    janela = Tk()
    janela.title("Buscar Whois")
    # janela.geometry("350x210")  # Largura x Altura
    janela.iconphoto(False, PhotoImage(file="program/dance.gif"))
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
    asNumberVar = StringVar()
    # ------------------------------------------------------------------------ VARIABLES LIST
    # ------------------------------------------------------------------------ FUNCTIONS LIST
    def buscar():

        if validation(): return

        criar_cards()


    def criar_cards():
        sites = geral.sites_list()
        program = whois.whois(asNumberVar.get())

        # Criar cards
        for index, site in enumerate(sites):
            card = ttk.Frame(bodyFrame, padding="2 2", relief=GROOVE)
            card.grid(column=0, row=index, padx=10, pady=10)
            cardTitle = ttk.Label(card, style='FundoLAzul.TLabel', text=f"Fonte: {site}", anchor=CENTER)
            cardTitle.grid(column=0, row=0, sticky=NSEW)
            cardBody = ttk.Frame(card, padding="5 0 5 5")
            cardBody.grid(column=0, row=1)
            cardBodyContent = Listbox(cardBody, width=70, activestyle='none')
            cardBodyContent.grid(column=0, row=0)

            # Colher informações e preencher os cards
            match index:
                case 0:
                    info = program.bgpview()
                    cardBodyContent.insert(END, info[0] + " - " + info[1])
                    for i in info[2]: cardBodyContent.insert(END, i + f" {info[0][2:]}") 

                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                    

    def validation():
        tittle_text = "Não foi possível continuar"

        if asNumberVar.get() == "" or asNumberVar.get() == " ": 
            messagebox.showinfo(message="Preencha uma informação válida para buscar", title=tittle_text)
            return True
        
        if "AS" not in asNumberVar.get():
            messagebox.showinfo(message='Realize a busca do troço com o "AS" na frente', title=tittle_text)
            return True
        
        return False
        
    # ------------------------------------------------------------------------ FUNCTIONS LIST

    # ------------------------------------------------------------------------ FRAMES
    mainframe = ttk.Frame(janela, padding="5 5", style='FundoBranco.TFrame')
    mainframe.grid(column=0, row=0)

    headFrame = ttk.Frame(mainframe, padding="0 5 0 0", style='FundoBranco.TFrame') # Esquerda, cima, direita, baixo
    headFrame.grid(column=0, row=1, pady=5)
    contornoHeadFrame = ttk.Frame(headFrame, padding="10 10 10 10", relief=GROOVE)
    contornoHeadFrame.grid(column=0, row=0)
    buscarWhois = ttk.Entry(contornoHeadFrame, textvariable=asNumberVar)
    buscarWhois.grid(column=0, row=0, ipady=3)
    buttonbuscarWhois = ttk.Button(contornoHeadFrame, text="Buscar", command=buscar)
    buttonbuscarWhois.grid(column=1, row=0, ipady=2)
    
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

    # ------------------------------------------------------------------------ EVENTS

    # ------------------------------------------------------------------------ RUN WINDOWS
    janela.mainloop()
    # ------------------------------------------------------------------------ RUN WINDOWS

if __name__ == '__main__':
    ui_whois()