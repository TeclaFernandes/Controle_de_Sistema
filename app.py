from tkinter import *
import os

def desligar():
    return os.system("shutdown /s /t 1")

def reiniciar():
    return os.system("shutdown /r /t 1")

def sair():
    return os.system("shutdown -l")

janela = Tk()
janela.title("Gerenciador de Energia")
janela.configure(bg='#975701')

largura_janela = 200
altura_janela = 200

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

Button(janela, text='Desligar', command=desligar, padx=10, pady=5, bg='#fdbd67').place(x=65, y=20)
Button(janela, text='Reiniciar', command=reiniciar, padx=10, pady=5, bg='#fdbd67').place(x=64, y=65)
Button(janela, text='Sair', command=sair, padx=10, pady=5, bg='#fdbd67').place(x=77, y=110)

janela.mainloop()
