import easygui
from easygui import *
from urllib.request import urlopen

tervitus = msgbox("Tere tulemast!")
nupud = ["Ei","Ja"]
vastus = buttonbox("Kas sa soovid jätkata?", choices = nupud)

if vastus == "Ja":
    nimi = enterbox("Palun sisesta oma nimi: ")
    vanus = integerbox("Palun sisesta oma vanus: ", lowerbound = 1, upperbound = 120)
    aadress = enterbox("Palun sisesta oma aadress: ")
    
failinimi = filesavebox()
f = open(failinimi, "w")
f.write(nimi + "\n")
f.write(str(vanus) + "\n")
f.write(aadress + "\n")
f.close()

failinimi = fileopenbox()
f = open(failinimi)

nimi = f.readline().strip()
vanus = f.readline().strip()
aadress = f.readline().strip()

f.close()

tagastus = "Sisestatud nimi on: " + nimi + "\n" + "Sisestatud vanus on: " + vanus + " a. " + "\n" + "Sisestatud aadress on: " + aadress
msgbox(tagastus)
easygui.msgbox("Korras")
failveebis = urlopen("https://courses.cs.washington.edu/courses/cse163/20wi/files/lectures/L04/bee-movie.txt")
veeb = failveebis.read()
tekst = veeb.decode()
failveebis.close()
msgbox(tekst)


