imiona = ["Kasia", "Tomek", "Jacek"]
lista =[ (x, x[0]) for x in imiona if x[-1]=="a"]
print (lista)