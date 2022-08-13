n=input("Podaj rok urodzenia")

dane = {"Ala Kowalska" : "03-04-2005", "Grzegorz Nowak" : "05-07-1999","Adam Serwus":"02-09-1960" }
for key, value in (dane).items() :
 if (n<value[-4:]):
     print(key)

