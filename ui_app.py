from tkinter import *
from tkinter import ttk, font, messagebox, Listbox
import threading
import os


def sisvisa():
    # ------------------------------------------------------------------------ CONFIG UI
    janela = Tk()
    janela.title("Buscar Whois")
    # janela.geometry("350x210")  # Largura x Altura
    # janela.iconphoto(False, PhotoImage(file=procurar_arquivos('SISVISA3.PNG')))
    janela.resizable(width=False, height=False)
    # janela.rowconfigure(0, weight=1)  # PESO DA LINHA (EXPANSÃO)
    # janela.columnconfigure(0)  # PESO DA COLUNA (EXPANSÃO)
    # ------------------------------------------------------------------------ CONFIG UI
    # ------------------------------------------------------------------------ COLOR LIST
    color_white = "#ffffff"
    color_blue_label = "#1f73b7"
    # ------------------------------------------------------------------------ COLOR LIST
    # ------------------------------------------------------------------------ STYLE LIST
    tittle_Font = font.Font(name='sisvisatitle_Font', size=16, weight='bold')
    sub_tittle_Font = font.Font(name='subapptittle_Font', size=10, weight='bold')
    ttk.Style().configure('FundoBranco.TFrame', background=color_white)
    ttk.Style().configure('FundoBranco.TRadiobutton', background=color_white)
    ttk.Style().configure('FundoBranco.TCheckbutton', background=color_white)
    ttk.Style().configure('FundoAzul.TFrame', background='blue')
    ttk.Style().configure('FundoBranco.TSeparator', foregroud=color_white)

    # ------------------------------------------------------------------------ STYLE LIST
    # ------------------------------------------------------------------------ VARIABLES LIST
    choice_service_var = IntVar()
    choice_step_var = IntVar()
    spin_var = IntVar(value=1)
    ambiente_var = StringVar()
    config_corretor_var = BooleanVar()
    config_treinamento_var = BooleanVar()
    # ------------------------------------------------------------------------ VARIABLES LIST
    # ------------------------------------------------------------------------ FUNCTIONS LIST
    def confirm_choice():
        choice = choice_service_var.get()
        ambiente = ambiente_var.get()
        spin = spin_var.get()
        corretor = config_corretor_var.get()

        try:
            step = choice_step_var.get()
            if choice < 6: 
                step = ''.join([f"1.{choice}.{step}"])
            else:
                step = ''.join([f"2.{choice}.{step}"])
        except:
            step = None
        
        # print("Escolha id:", choice, "\nStep id:", step, f"\nConfigs:\nCorretor={corretor}")
        if validation(choice=choice, step=step, ambiente=ambiente): return 

        return main_sisvisa.menu(ambiente=ambiente, choice=choice, step=step, switch_corretor=corretor)


    # ------------------------------------------------------------------------ FUNCTIONS LIST

    # ------------------------------------------------------------------------ FRAMES
    mainframe = ttk.Frame(janela, padding="0 0 0 0", style='FundoBranco.TFrame')
    mainframe.grid(column=0, row=0)

    headFrame = ttk.Frame(mainframe, padding="10 10 10 10") # Esquerda, cima, direita, baixo
    headFrame.grid(column=0, row=1)
    buscarWhois = ttk.Entry(headFrame)
    buscarWhois.grid(column=0, row=0, ipady=3)
    buttonbuscarWhois = ttk.Button(headFrame, text="Buscar")
    buttonbuscarWhois.grid(column=1, row=0, ipady=2)
    
    bodyFrame = ttk.Frame(mainframe, padding="14 1 14 10", relief=GROOVE)
    bodyFrame.grid(column=0, row=2, pady=10)
    card = ttk.Frame(bodyFrame)
    card.grid(column=0, row=0)
    cardTitle = ttk.Label(card, text="Fonte:")
    cardTitle.grid(column=0, row=0)
    card.grid(column=0, row=0)
    cardBody = ttk.Frame(card)
    cardBody.grid(column=0, row=1)
    cardBodyContent = Listbox(cardBody)
    cardBodyContent.grid(column=0, row=0)
    # ------------------------------------------------------------------------ FRAMES

    # ------------------------------------------------------------------------ LOGO + H1
    # div_h1 = ttk.Frame(mainframe, style='FundoAzul.TFrame')
    # div_h1.grid(column=0, row=0, columnspan=2, sticky=NSEW)
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
    sisvisa()