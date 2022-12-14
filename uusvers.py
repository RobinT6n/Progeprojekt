#PROGRAMM: Ajaplaneerimise abiline
#AUTORID:
#	KRISTJAN NOORMETS
#	ROBIN TÕNISTE


import os
from datetime import datetime
from tkinter import *
from math import floor

#MUUTUJAD:
failinimi = "andmed.txt"
obj_jrjnd = []





#FUNKTSIOONID JA KLASSID
class Ylesanne:
	def __init__(self, nimi, paev, kuu, aasta, tund, minut):
		self.nimi = nimi
		self.kuu = int(kuu)
		self.paev = int(paev)
		self.aasta = int(aasta)
		self.tund = int(tund)
		self.minut = int(minut)
	def aegkuni(self):
		aegkuni = datetime(self.aasta,self.kuu,self.paev,self.tund,self.minut).timestamp() - datetime.now().timestamp()
		return aegkuni


def loefailist(failinimi=failinimi, yljrjnd=obj_jrjnd): #Loeb failist järjendi ja teeb Ylessanne objektid, mille hoiustab yljrjnd ja siis tagastab selle
	try:
		objekt = 0
		fail = open(failinimi, 'r', encoding='UTF-8')
		for rida in fail:
			infojrjnd = rida.strip("\n").split(";")
			print(infojrjnd)
			objekt = Ylesanne(str(infojrjnd[0]),int(infojrjnd[1]),int(infojrjnd[2]),int(infojrjnd[3]),int(infojrjnd[4]),int(infojrjnd[5]))
			yljrjnd.append(objekt)
		yljrjnd.sort(key=lambda x: x.aegkuni())
		fail.close()
		return yljrjnd
	except:
		return []

def kirjutafaili(failinimi=failinimi,jrjnd=obj_jrjnd): # Kirjutab faili formaadis [[nimi, paev, kuu, aasta, tund, minut],[objekt2]...]
	jrjnd.sort(key=lambda x: x.aegkuni())
	i = 0
	fail = open(failinimi, 'w', encoding='UTF-8')
	for yl in jrjnd:
		if i > 0:
			fail.write['\n']
		fail.writelines(f'{str(yl.nimi)}";{yl.paev};{yl.kuu};{yl.aasta};{yl.tund};{yl.minut}')
		i+=1
	fail.close()
	return

def kontrollikp(paev, kuu, aasta):
	try:
		paev=int(paev)
		kuu=int(kuu)
		aasta=int(aasta)
		if int(kuu) in [1,3,5,7,8,10,12]:
			if int(paev) > 0 and int(paev) <=31:
				return True
			else:
				return False
		elif int(kuu) in [4,6,9,11]:
			if paev > 0 and paev <=30:
				return True
			else:
				return False
		elif int(kuu) == 2:
			if (aasta % 400 == 0):
				if paev > 0 and paev <= 29:
					return True
				else:
					return False
			elif (aasta % 100 != 0) and (aasta % 4 == 0):
				if paev > 0 and paev <= 29:
					return True
				else:
					return False
			else:
				if paev > 0 and paev <= 28:
					return True
				else:
					return False
		else:
			return False
	except:
		return False

def kontrollikell(tund, minut):
	try:
		tund=int(tund)
		minut=int(minut)
		if tund < 0 or tund >= 24:
			return False
		if minut < 0 or minut >= 60:
			return False
		return True
	except:
		return False


def loojalisaobjekt(nimi, paev, kuu, aasta, tund, minut, jrjnd=obj_jrjnd):
	lisaobjekt = Ylesanne(nimi, paev, kuu, aasta, tund, minut)
	jrjnd.append(lisaobjekt)
	return jrjnd

# IDEED
#
#print(datetime(2022,12,14,19,45).timestamp() - datetime.now().timestamp()) # See kuidas pärast saame "Aegkuni" kätte. Lihtsalt vaja teha formatimist veits (Päev, tund, minut)
# Sort(key=lambda x: x.aegkuni(), ) #Imeline viis sorteerida kogu classi Ylesanne objektide järjend - done
#

#MAIN PROGRAMMI OSA?



#ALGNE KOOD

# # Pigem pole vaja
# #true või false
# eksisteerib = os.path.exists(failinimi)

# with open(failinimi, "a" if eksisteerib else "w", encoding="UTF-8") as f: # Seda ka pigem pole vaja
# 	while True:
# 		sisestus = input("Sisesta ülesanne: ")
# 		try:
# 			# Mõtlesin äkki võtta see kuupäev tükkideks lahti, siis äkki kergem sorteerida neid 
# 			# Põhimõtteliselt saab selle 'kuu,paev,aasta' osa muuta tagasi MM-DD-YYYY formaati faili kirjutamisel.
# 			# Selle asjaga saab lihtsalt checkida kas kuupäev on normaalne.
# 			#
# 			kuupaev = input("Sisesta kuupäev(MM-PP-YYYY): ") #Algne
# 			kuu,paev,aasta = kuupaev.split("-") #Üldiselt jääb suht sarnaseks
# 			kuu,paev,aasta = int(kuu),int(paev),int(aasta)
# 			aasta = int("20"+str(aasta).zfill(2))
# 			# if int(kuu) in [1,3,5,7,8,10,12]: #Kogu see osa on nüüd funktsioon kontrollikp(), mis korrektse kuupäeva korral returnib True
# 			# 	if int(paev) > 0 and int(paev) <=31:
# 			# 		continue
# 			# 	else:
# 			# 		raise ValueError(f"Teie sisestatud kuupäev {kuupaev} ei ole korrektne")
# 			# elif int(kuu) in [4,6,9,11]:
# 			# 	if paev > 0 and paev <=30:
# 			# 		continue
# 			# 	else:
# 			# 		raise ValueError(f"Teie sisestatud kuupäev {kuupaev} ei ole korrektne")
# 			# elif int(kuu) == 2:
# 			# 	if (aasta % 400 == 0):
# 			# 		if paev > 0 and paev <= 29:
# 			# 			continue
# 			# 		else:
# 			# 			raise ValueError(f"Teie sisestatud kuupäev {kuupaev} ei ole korrektne")
# 			# 	elif (aasta % 100 != 0) and (aasta % 4 == 0):
# 			# 		if paev > 0 and paev <= 29:
# 			# 			continue
# 			# 		else:
# 			# 			raise ValueError(f"Teie sisestatud kuupäev {kuupaev} ei ole korrektne")
# 			# 	else:
# 			# 		if paev > 0 and paev <= 28:
# 			# 			continue
# 			# 		else:
# 			# 			raise ValueError(f"Teie sisestatud kuupäev {kuupaev} ei ole korrektne")
# 			# else:
# 			# 	raise ValueError(f"Teie sisestatud kuupäev {kuupaev} ei ole korrektne") #Kuni siiani siis kontrollikp()
# 			aasta = int(str(aasta)[-2:])
			
# 			# kuupaev = input("Sisesta kuupäev(MM-PP-YY): ") #Algne
# 			kellaaeg = input("Sisesta kellaaeg(00:00): ")
# 			tund, minut = kellaaeg.split(":")
# 			f.write(f"Ülesanne: {sisestus}, Kuupäev: {kuupaev}, Kellaaeg: {kellaaeg}\n")  #Algne
# 			# f.write(f"Ülesanne: {sisestus}, Kuupäev: {(str(kuu).zfill(2))}-{paev}-{aasta}, Kellaaeg: {kellaaeg}\n") #Tagasi MM-DD-YY formaati. Pole vaja, tuli parem idee
# 			jatkuvus = input("Tahad veel ülesandeid lisada(y - jah, n - ei)? ")
# 			if jatkuvus.lower() == "n":
# 				break
# 		except ValueError as v:
# 			print(f"Tekkis viga: {v}.\nKontrolli sisestatud tekst üle!")
# 			jatkuvus = input("Tahad veel ülesandeid lisada(y - jah, n - ei)? ")
# 			if jatkuvus.lower() == "n":
# 				break






# jarjend = []
# jarjend2 = []
# kuu = []
# kellad = []
# ulesanded = []

# f = open(failinimi, "r")
# for rida in f:
# 	jarjend.append(rida.strip("\n"))
# f.close()

# for i in jarjend:
# 	jarjend2.append(i.strip(" ").split(","))

# for i in jarjend2:
# 	for j in i:
# 		j.split()
# 		if j[1:8] == "Kuupäev":
# 			kuupv = j[9:18]
# 			kuu.append(kuupv.strip(" "))
# 		if j[1:9] == "Kellaaeg":
# 			kellaa = j[10:16]
# 			kellad.append(kellaa.strip(" "))
# 		if j[0:8] == "Ülesanne":
# 			ül = j[9:]
# 			ulesanded.append(ül.strip(" "))

# # POLE VAJA #üritan teha sorteerimist, et näitaks failis ülesandeid enne, mille kuupäevad on kõige varasemad
# # kuu_indeksid = kuu[:]
# # kellade_indeksid = kellad[:]

# #def sorteeri_kuupaev(kuupaevade_listid):
# #	eraldi = kuupaevade_listid.split("-")
# #	print(eraldi)
# #	return eraldi[1], eraldi[0]
# #kuu.sort(key=sorteeri_kuupaev)
# #
# #def sorteeri_kellad(kellade_listid):
# #	eraldi = kellade_listid.split(":")
# #	return eraldi[0], eraldi[1]
# #kellad.sort(key=sorteeri_kellad)

