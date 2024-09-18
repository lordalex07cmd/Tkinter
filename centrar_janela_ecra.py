#Import the tkinter libraryfrom tkinter import *#Create an instance of tkinter frame

from tkinter import *

win = Tk()#Set the geometry

larg = 801 #largura da janela
alt = 601  #altura da janela

larg_ecra = win.winfo_screenwidth() ##largura da resolução do ecrã
alt_ecra = win.winfo_screenheight() ##altura da resolução do ecrã
#print(larg_ecra,alt_ecra)

#determina o ponto (x,y) onde inicia a janela (
# metade_larg_ecra - metadade_larg_janela, metade_alt_ecra - metade_alt_janela)
posx = (larg_ecra / 2) - (larg / 2) # 1920/2 - 800/2 = 960-400=560
posy = (alt_ecra / 2) - (alt / 2)

win.geometry("%dx%d+%d+%d" % (larg,alt,posx,posy))


##Bibiloteca para posicionar o ponto (x,y) da janela no centro do ecra
#win.eval('tk::PlaceWindow . center')

win.mainloop()
