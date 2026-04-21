import json
import csv
datne=open("uzd2.json",encoding="utf-8")
dati=json.load(datne)

pilsētas=[]
pensionāru_īpatsvars=[]
pilsētas.append("Rīga")
print(pilsētas)
procenti=[]
for vardnica in dati:
    procenti=(100/vardnica["iedzivotaji_kopā"])*vardnica["pensionari"]
    pensionāru_īpatsvars.append(procenti)
    print(f"{(procenti):.0f}%")
datne.close()
vardnica1={vardnica["nosaukums"]:procenti}

datne.close()

with open("rezultati.csv","w",encoding="utf-8")as d:
    i=csv.writer(d)
    i.writerow(vardnica1)




