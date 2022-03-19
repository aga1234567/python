n=int(input("Podaj n"))
suma=0
for i in range(1,n+1):
    suma=suma+(i**3)
print(round(suma,2))