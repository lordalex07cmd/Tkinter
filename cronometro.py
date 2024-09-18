###Ficha 4 exercício 15

## BIBLIOTECAS
from tkinter import *
from time import strftime

#### FUNÇÕES #####
def sair():
    janela.destroy()

def limpar():
    enome.delete(0,END)
    emorada.delete(0,END)
    enome.focus()
    label1["text"] = ""
    label2["text"] = ""

def ler():
    nome = enome.get().title()
    morada = emorada.get().title()
    label1["text"] = nome
    label2.configure(text=morada)

def relogio(minuto, segundo):
    from time import sleep
    #from time import sleep 
    #for m in range(0,-1,-1):
    #    for s in range(59,-1,-1):
    #        print(f"{m}:{s}")
    #        sleep(1)


   ##ERRO por causa de 1 segundo 
    print(minuto, segundo)

    lrelogio["text"]=f"00:{minuto}:{segundo}"
    segundo -= 1
    
    if (segundo==0 and minuto != 0):
        minuto -=1
        segundo = 59
    if (segundo==0 and minuto != 0):
        minuto -=1
        segundo = 00

    if segundo > -1:
        lrelogio.after(1000, lambda: relogio(minuto, segundo))


    
#####################################


##INERFACE
janela = Tk()
janela.title("Primeira janela em Tk")
janela.geometry("300x350+300+500")
#janela.iconbitmap("icon_python.ico")


#OBJECTOS
lnome=Label(janela,text="Nome:")
lmorada=Label(janela,text="Morada:")
enome = Entry(janela, width=25)
emorada = Entry(janela, width=25)
bler = Button(janela, text="Ler Dados",
              bd=4, width=11, command=ler)
blimpar = Button(janela, text="Limpar",
                 bd=4, width=11, command=limpar)
bsair = Button(janela, text="Sair",
               bd=4, bg="Red",fg="White",
               width=6, command=sair)
lmostrar = Label(janela,text="Os dados lidos são:")
label1 = Label(janela,text="")
label2 = Label(janela,text="")
lrelogio = Label(janela, text="")

#Posicionar objetos
lnome.place(x=30, y=30)
lmorada.place(x=30, y=50)
#medir tamanho da palavra morada pois é o mais comprido
janela.update() #forçar o cálculo do tamanhos dos objetos
medida = lmorada.winfo_width()#obter largura do objeto morada
enome.place(x=30+medida, y=30)
emorada.place(x=30+medida, y=50 )
bler.place(x=30, y=90)
janela.update() #forçar o cálculo do tamanhos dos objetos
medida = bler.winfo_width()#obter largura do objeto morada
blimpar.place(x=30+medida+10, y=90)
bsair.place(x=30+2*medida+10+10, y=90 )
lmostrar.place(x=30, y=130)
label1.place(x=30, y=150)
label2.place(x=30, y=170)
enome.focus()

#lrelogio["text"]="22:50:10"
lrelogio["font"]=("Comic Sans Ms", "16", "bold")
lrelogio.place(x=180,y=300)

relogio(1,5)

janela.mainloop()


