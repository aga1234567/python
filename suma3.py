n=int(input("Podaj n"))
suma=0
for i in range(1,n+1):
    suma=suma+1/(i*(i+1))
print(round(suma,2))