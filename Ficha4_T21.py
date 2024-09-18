###Ficha 4
#### FUNÇÕES #####
def bazar():
    janela.destroy()


#####################################
from tkinter import *

##INERFACE
janela = Tk()
janela.title("Primeira janela em Tk")
janela["background"]="Orange"
janela.geometry("400x330+300+500")
janela.resizable(False,0)
fonte = ("Comic Sans MS", "14", "bold")
janela.iconbitmap("imagens\dragon.ico")


#OBJECTOS
label1 = Label(janela,text="Olá Python",
               bg="Orange")
#label1.pack(side="bottom")
#label1.configure(font=fonte)
label1["font"] = fonte
cxtexto = Entry(janela, fg="Blue")
cxtexto["font"]=fonte
botao = Button(janela, text="Sair",
               command=bazar, bd=5,
               bg="Lightgreen", fg="Green")
#janela.wm_attributes('-transparentcolor','orange')


#### POSICIONAR OBJETOS
label1.place(x=30, y=50)
cxtexto.pack()
botao.pack()
