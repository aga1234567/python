imiona = ["Kasia", "Tomek", "Jacek"]
nazwisko=["Nowak","Kowalski","Maj"]
lista =[ (imiona[i][0], nazwisko[i][0]) for i in range(len(imiona))]
print(lista)