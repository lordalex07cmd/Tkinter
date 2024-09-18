from tkinter import *
from tkinter.ttk import *

def mostra(texto):
    print(texto)
    
###################################
janela = Tk()
janela.geometry("300x200")

lista = ['Ciano', 'Magenta', 'Preto', 'Amarelo']
numeros = []
for x in range(1,101):
    numeros.append(x)

combo1 = Combobox(janela,values=lista)
combo2 = Combobox(janela, values=numeros)
combo1.set("Escolha uma opção...")
combo1.pack()
combo2.pack()

botao= Button(janela, text="SIM",
              command=lambda:mostra("YES"))
                #opção lambda implica que o valor do parametro
                #só será passado quando houver evento via utilizador
                # caso contrario chama de imediato a função e executa 1 vez
botao.pack()


janela.mainloop()
