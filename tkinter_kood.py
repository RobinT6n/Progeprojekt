#PROGRAMM: Ajaplaneerimise abiline
#AUTORID:
#	KRISTJAN NOORMETS
#	ROBIN TÕNISTE


import uusvers as uv
import tkinter as tki

#MUUTUJAD:
obj_jrjnd=uv.obj_jrjnd


# NUPPUDE FUNKTSIOONID




# FUNKTSIOONID JA KLASSID
def lisaylesanne():
	def lisalisti():
		ylnimi = nimi.get()
		ylpaev = paev.get()
		ylkuu = kuu.get()
		ylaasta = aasta.get()
		yltund = tund.get()
		ylminut = minut.get()
		if uv.kontrollikp(ylpaev, ylkuu, ylaasta):
			if uv.kontrollikell(yltund, ylminut):
				uv.loojalisaobjekt(ylnimi, ylpaev, ylkuu, ylaasta, yltund, ylminut, jrjnd=obj_jrjnd)
				uv.kirjutafaili(jrjnd=obj_jrjnd)
				root.destroy()
			else:
				def kellboom():
					valekell.destroy()
				valekell = tki.Tk()
				valekell.title("Kellaaeg on vale!")
				valekell.geometry("120x50")
				sisukell = tki.Label(valekell, text="Kellaaeg on vale!")
				sisukell.pack()
				kellokei = tki.Button(valekell, text="Okei!", command=kellboom)
				kellokei.pack()
				valekell.mainloop()
		else:
				def kpboom():
					valekp.destroy()
				valekp = tki.Tk()
				valekp.title("Kuupäev on vale!")
				valekp.geometry("120x50")
				sisukp = tki.Label(valekp, text="Kuupäev on vale!")
				sisukp.pack()
				kpokei = tki.Button(valekp, text="Okei!", command=kpboom)
				kpokei.pack()
				valekp.mainloop()

	root = tki.Tk()
	root.title("Uus Ülesanne")
	root.geometry("300x130")
	n = tki.Label(root, text="Ülesande nimi:")
	n.place(x=0,y=0)
	nimi = tki.Entry(root, width=45)
	nimi.place(x=10,y=20)
	kp= tki.Label(root,text="Kuupäev (DD-MM-YYYY):") #Kuupäev
	kp.place(x=0,y=40)
	paev = tki.Entry(root,width=2)
	paev.place(x=10,y=60)
	kuu = tki.Entry(root,width=2)
	kuu.place(x=30,y=60)
	aasta = tki.Entry(root,width=4)
	aasta.place(x=50,y=60)
	ka = tki.Label(root, text="Kellaaeg (HH:MM):") #Kellaaeg
	ka.place(x=0,y=80)
	tund = tki.Entry(root, width=2)
	tund.place(x=10,y=100)
	minut = tki.Entry(root, width=2)
	minut.place(x=30,y=100)
	lisa = tki.Button(root, text="Lisa", width=10, command=lisalisti)
	lisa.place(x=210,y=95)
	root.mainloop()






#MAIN PROGRAMMI OSA
obj_jrjnd = uv.loefailist()

lisaylesanne()

# andmed = []
# jarjestatud_andmed = []
# while True: 
# 	sisu = []
# 	vaartus = []
# 	root = Tk()
# 	root.title("Ülesande sisestus")
# 	sisestus = tkinter.Entry(root, width=50)
# 	sisestus.pack()
# 	nupp = tkinter.Button(root, text="Lisa ülesande nimi", width=48, command=nupu_vajutus_ulesanne)
# 	nupp.pack()
# 	root.mainloop()

# 	root2 = Tk()
# 	root2.title("kuupaeva sisestus") 
# 	sisestus2 = tkinter.Entry(root2, width=50) #See võiks olla kohe eraldi lahtritena - Päev, kuu, aasta
# 	sisestus2.pack()
# 	nupp2 = tkinter.Button(root2, text="Lisa kuupäev (MM-PP-YY)", width=48, command=nupu_vajutus_kuupaev)
# 	nupp2.pack()
# 	root2.mainloop()

# 	root3 = Tk()
# 	root3.title("kellaaja sisestus")
# 	sisestus3 = tkinter.Entry(root3, width=50) #See võiks ka olla kaks lahtrit - Tund, minut
# 	sisestus3.pack()
# 	nupp3 = tkinter.Button(root3, text="Lisa kellaaeg (00:00)", width=48, command=nupu_vajutus_kellaaeg)
# 	nupp3.pack()
# 	root3.mainloop()

# 	andmed.append(sisu)

# 	root4 = Tk()
# 	root4.title("Jätkuvus")
# 	nuppjah = tkinter.Button(root4, text="Jätka", width=48, command=nupu_vajutus_jah)
# 	nuppjah.pack()
# 	nuppei = tkinter.Button(root4, text="katkesta", width=48, command=nupu_vajutus_ei)
# 	nuppei.pack()
# 	root4.mainloop()
# 	if len(vaartus) == 1:
# 		#siia peaks nt lisama selle, et kui fail olemas, ss lisab faili ("a"), muidu kui pole faili olemas, siis kirjutab uue faili("w")
# 		with open("andmete_fail.txt", "w", encoding="utf8") as f:
# 			for i in andmed:
# 				ulesanne = i[0]
# 				dates = i[1].split("-")
# 				paev = dates[1]
# 				kuu = dates[0]
# 				aasta = dates[2]
# 				ajad = i[2].split(":")
# 				tund = ajad[0]
# 				minut = ajad[1]
# 				f.write(f"Ülesanne: {ulesanne}, päev: {paev}, kuu: {kuu}, aasta: {aasta}, tund:{tund}, minutid: {minut}\n")
# 		break


#HUNNIK FUNKTSIOONE - X klõpsamine

