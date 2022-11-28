import os
from datetime import datetime

failinimi = "andmed.txt"
#true või false
eksisteerib = os.path.exists(failinimi)

with open(failinimi, "a" if eksisteerib else "w", encoding="UTF-8") as f:
	while True:
		sisestus = input("Sisesta ülesanne: ")
		try:
			# Mõtlesin äkki võtta see kuupäev tükkideks lahti, siis äkki kergem sorteerida neid 
			# Põhimõtteliselt saab selle 'kuu,paev,aasta' osa muuta tagasi MM-DD-YY formaati faili kirjutamisel.
			# Selle asjaga saab lihtsalt checkida kas kuupäev on normaalne.
			# 
			# kuu,paev,aasta = input("Sisesta kuupäev(MM-PP-YY): ").split("-")
			# kuu,paev,aasta = int(kuu),int(paev),int(aasta)
			# aasta = int("20"+str(aasta))
			# if int(kuu) in [1,3,5,7,8,10,12]:
			# 	if int(paev) > 0 and int(paev) <=31:
			# 		continue
			# 	else:
			# 		raise ValueError(f"Teie sisestatud kuupäev {(str(kuu).zfill(2))}-{paev}-{(str(aasta)[-2:])} ei ole korrektne")
			# elif int(kuu) in [4,6,9,11]:
			# 	if paev > 0 and paev <=30:
			# 		continue
			# 	else:
			# 		raise ValueError(f"Teie sisestatud kuupäev {str(kuu).zfill(2)}-{paev}-{(str(aasta)[-2:])} ei ole korrektne")
			# elif int(kuu) == 2:
			# 	if (aasta % 400 == 0):
			# 		if paev > 0 and paev <= 29:
			# 			continue
			# 		else:
			# 			raise ValueError(f"Teie sisestatud kuupäev {str(kuu).zfill(2)}-{paev}-{(str(aasta)[-2:])} ei ole korrektne")
			# 	elif (aasta % 100 != 0) and (aasta % 4 == 0):
			# 		if paev > 0 and paev <= 29:
			# 			continue
			# 		else:
			# 			raise ValueError(f"Teie sisestatud kuupäev {(str(kuu).zfill(2))}-{paev}-{(str(aasta)[-2:])} ei ole korrektne")
			# 	else:
			# 		if paev > 0 and paev <= 28:
			# 			continue
			# 		else:
			# 			raise ValueError(f"Teie sisestatud kuupäev {(str(kuu).zfill(2))}-{paev}-{(str(aasta)[-2:])} ei ole korrektne")
			# else:
			# 	raise ValueError(f"Teie sisestatud kuupäev {(str(kuu).zfill(2))}-{paev}-{(str(aasta)[-2:])} ei ole korrektne")
			# aasta = int(str(aasta)[-2:])
			#
			kuupaev = input("Sisesta kuupäev(MM-PP-YY): ") #Algne
			kellaaeg = input("Sisesta kellaaeg(00:00): ")
			f.write(f"Ülesanne: {sisestus}, Kuupäev: {kuupaev}, Kellaaeg: {kellaaeg}\n")  #Algne
			# f.write(f"Ülesanne: {sisestus}, Kuupäev: {(str(kuu).zfill(2))}-{paev}-{aasta}, Kellaaeg: {kellaaeg}\n") #Tagasi MM-DD-YY formaati
			jatkuvus = input("Tahad veel ülesandeid lisada(y - jah, n - ei)? ")
			if jatkuvus == "n":
				break
			else:
				continue
		except ValueError as v:
			print(f"Tekkis viga: {v}.\nKontrolli sisestatud tekst üle!")

jarjend = []
jarjend2 = []
kuu = []
kellad = []
ulesanded = []

f = open(failinimi, "r")
for rida in f:
	jarjend.append(rida.strip("\n"))
f.close()

for i in jarjend:
	jarjend2.append(i.strip(" ").split(","))

for i in jarjend2:
	for j in i:
		j.split()
		if j[1:8] == "Kuupäev":
			kuupv = j[9:18]
			kuu.append(kuupv.strip(" "))
		if j[1:9] == "Kellaaeg":
			kellaa = j[10:16]
			kellad.append(kellaa.strip(" "))
		if j[0:8] == "Ülesanne":
			ül = j[9:]
			ulesanded.append(ül.strip(" "))

#üritan teha sorteerimist, et näitaks failis ülesandeid enne, mille kuupäevad on kõige varasemad
kuu_indeksid = kuu[:]
kellade_indeksid = kellad[:]

#def sorteeri_kuupaev(kuupaevade_listid):
#	eraldi = kuupaevade_listid.split("-")
#	print(eraldi)
#	return eraldi[1], eraldi[0]
#kuu.sort(key=sorteeri_kuupaev)
#
#def sorteeri_kellad(kellade_listid):
#	eraldi = kellade_listid.split(":")
#	return eraldi[0], eraldi[1]
#kellad.sort(key=sorteeri_kellad)