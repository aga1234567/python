n = int((input("Podaj ilo cyfrowe liczby mam wyswietlic n")))
m = int((input("Podaj podzielne przez m")))
i=n
"""while i<1000000:
    if len(str(i))==n and i%m==0:
        print (i)
    i=i+1"""
for i in range(1,1000000):
    if len(str(i))==n and i%m==0:
        print(i)