import context
from tkinter import *
from tkinter import ttk, font, messagebox, Listbox
import program._geral as geral
import program.main_class as whois
import threading


def ui_whois():
    # ------------------------------------------------------------------------ CONFIG UI
    janela = Tk()
    janela.title("Buscar Whois")
    # janela.geometry("350x210")  # Largura x Altura
    # janela.iconphoto(False, PhotoImage(file=procurar_arquivos('SISVISA3.PNG')))
    janela.resizable(width=False, height=False)
    # ------------------------------------------------------------------------ CONFIG UI
    # ------------------------------------------------------------------------ COLOR LIST
    color_white = "#ffffff"
    color_blue_label = "#014654"
    # ------------------------------------------------------------------------ COLOR LIST
    # ------------------------------------------------------------------------ STYLE LIST
    tittle_Font = font.Font(name='sisvisatitle_Font', size=16, weight='bold')
    sub_tittle_Font = font.Font(name='subapptittle_Font', size=10, weight='bold')
    ttk.Style().configure('FundoBranco.TFrame', background=color_white)
    ttk.Style().configure('FundoAzul.TFrame', background='blue')
    ttk.Style().configure('FundoLAzul.TLabel', background='#017991')
    ttk.Style().configure('Fundo.TFrame', background='blue')
    ttk.Style().configure('FundoBranco.TSeparator', background=color_white)

    # ------------------------------------------------------------------------ STYLE LIST
    # ------------------------------------------------------------------------ VARIABLES LIST
    target_var = StringVar()
    choice_service_var = IntVar()
    choice_step_var = IntVar()
    spin_var = IntVar(value=1)
    config_corretor_var = BooleanVar()
    config_treinamento_var = BooleanVar()
    # ------------------------------------------------------------------------ VARIABLES LIST
    # ------------------------------------------------------------------------ FUNCTIONS LIST
    def buscar():

        program = whois.whois(target_var.get())
        program.primeiro_site()
        criar_cards()


    def criar_cards():
        sites = geral.sites_list()

        for index, site in enumerate(sites):
            card = ttk.Frame(bodyFrame, padding="2 2", relief=GROOVE)
            card.grid(column=index, row=0, padx=10, pady=10)
            cardTitle = ttk.Label(card, style='FundoLAzul.TLabel', text=f"Fonte: {site}", anchor=CENTER)
            cardTitle.grid(column=0, row=0, sticky=NSEW)
            cardBody = ttk.Frame(card, padding="5 0 5 5")
            cardBody.grid(column=0, row=1)
            cardBodyContent = Listbox(cardBody, width=35)
            cardBodyContent.grid(column=0, row=0)

        
    # ------------------------------------------------------------------------ FUNCTIONS LIST

    # ------------------------------------------------------------------------ FRAMES
    mainframe = ttk.Frame(janela, padding="5 5", style='FundoBranco.TFrame')
    mainframe.grid(column=0, row=0)

    headFrame = ttk.Frame(mainframe, padding="0 5 0 0", style='FundoBranco.TFrame') # Esquerda, cima, direita, baixo
    headFrame.grid(column=0, row=1, pady=5)
    contornoHeadFrame = ttk.Frame(headFrame, padding="10 10 10 10", relief=GROOVE)
    contornoHeadFrame.grid(column=0, row=0)
    buscarWhois = ttk.Entry(contornoHeadFrame, textvariable=target_var)
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