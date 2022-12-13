#sellega on võimalik saada väärtused ning siis saab ka neid väärtusi veel edasi kuskile asetada või kasutada
import uusvers
from tkinter import *
import tkinter

def nupu_vajutus_ulesanne():
	ulesanne = sisestus.get()
	sisu.append(ulesanne)
	root.destroy()

def nupu_vajutus_kuupaev():
	kuupaev = sisestus2.get()
	sisu.append(kuupaev)
	root2.destroy()

def nupu_vajutus_kellaaeg():
	kellaaeg = sisestus3.get()
	sisu.append(kellaaeg)
	root3.destroy()

def nupu_vajutus_jah():
	root4.destroy()

def nupu_vajutus_ei():
	root4.destroy()
	vaartus.append(1)

while True: 
	sisu = []
	vaartus = []
	root = Tk()
	root.title("Ülesande sisestus")
	sisestus = tkinter.Entry(root, width=50)
	sisestus.pack()
	nupp = tkinter.Button(root, text="Lisa ulesanne", width=48, command=nupu_vajutus_ulesanne)
	nupp.pack()
	root.mainloop()

	root2 = Tk()
	root2.title("kuupaeva sisestus") 
	sisestus2 = tkinter.Entry(root2, width=50) #See võiks olla kohe eraldi lahtritena - Päev, kuu, aasta
	sisestus2.pack()
	nupp2 = tkinter.Button(root2, text="Lisa kuupäev", width=48, command=nupu_vajutus_kuupaev)
	nupp2.pack()
	root2.mainloop()

	root3 = Tk()
	root3.title("kellaaja sisestus")
	sisestus3 = tkinter.Entry(root3, width=50) #See võiks ka olla kaks lahtrit - Tund, minut
	sisestus3.pack()
	nupp3 = tkinter.Button(root3, text="Lisa kellaaeg", width=48, command=nupu_vajutus_kellaaeg)
	nupp3.pack()
	root3.mainloop()

	print(sisu)

	root4 = Tk()
	root4.title("Jätkuvus")
	user_password = Label(root4, text = "Password")
	nuppjah = tkinter.Button(root4, text="Jätka", width=48, command=nupu_vajutus_jah)
	nuppjah.pack()
	nuppei = tkinter.Button(root4, text="katkesta", width=48, command=nupu_vajutus_ei)
	nuppei.pack()
	root4.mainloop()
	if len(vaartus) == 1:
		break