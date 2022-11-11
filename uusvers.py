import os
from datetime import datetime

failinimi = "andmed.txt"
#true või false
eksisteerib = os.path.exists(failinimi)

with open(failinimi, "a" if eksisteerib else "w") as f:
	while True:
		sisestus = input("Sisesta ülesanne: ")
		kuupaev = input("Sisesta kuupäev(MM-PP-YY): ")
		kellaaeg = input("Sisesta kellaaeg(00:00): ")
		f.write(f"Ülesanne: {sisestus}, Kuupäev: {kuupaev}, Kellaaeg: {kellaaeg}\n")
		jatkuvus = input("Tahad veel ülesandeid lisada(y - jah, n - ei)? ")
		if jatkuvus == "n":
			break
		else:
			continue

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