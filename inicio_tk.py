from tkinter import *







def dizok():
    print("bye-bye mundo")
    janela.destroy()




janela = Tk()
janela.title('Formulário de inscrição')
janela.geometry('600x400+450+300')
janela.iconbitmap('dragon.ico')
janela.resizable(True, True)

x=janela.winfo_screenwidth()
y=janela.winfo_screenheight()
print(f"Resolução: {x}x{y}")

janela['bg']="#d97661"

janela.minsize(50,50)
janela.maxsize(x-200,y-200)

#janela.state('zoomed')
fonte = "Arial 26 overstrike"
##Criação da interface
texto = Label(janela,fg="Blue", relief=SUNKEN,bd=4,
              bg="Yellow",
              text="O meu 1º texto", width=20,
              font="Arial 26 bold")

cxtexto = Entry(janela, width=40,
                bg="Gray",show="",
                font=fonte,
                fg="White")
cxtexto.focus()
botao = Button(janela, text="DIZ OK", command=dizok,bd=18,
               background="Lightgreen", foreground="Green")

#Colocar Objetos
#botao.pack(side=LEFT, fill=BOTH)
#texto.pack(side=RIGHT,fill=Y)
#cxtexto.pack(side=BOTTOM)
texto

texto.grid(row=0, column=0, sticky="WE")
botao.grid(row=0, column=1, sticky="WE")
cxtexto.grid(row=1, column=0,columnspan=2,sticky="WE")

#texto.place(x=20,y=30)
#janela.update() #recalcular internamente dimensões dos objetos
#comp = texto.winfo_width()
#print(f"Comprimento do rotulo: {comp}")
#botao.place(x=comp+25,y=30)

janela.mainloop()
