import re
with open ("klienti.txt","r",encoding="utf-8")as datne:
    dati=datne.read()

epasti=re.findall(r"\w+@\w+\.\w+",dati)
print(epasti)
print(len(epasti))
telefoni=re.findall(r"\d{8}",dati)
print(telefoni)


aizvietots=re.sub(r"\d{8}","📱",dati)
print(aizvietots)

datne=open("klienti_anon.txt","w",encoding="utf-8")
datne.write(aizvietots)
datne.close()
