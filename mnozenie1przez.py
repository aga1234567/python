n=int(input("Podaj n"))
iloczyn=1
for i in range(1,n+1):
    iloczyn=iloczyn*(1/(i+1))
print(iloczyn)