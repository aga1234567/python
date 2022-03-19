n=int(input("Podaj n"))
licznik=0
for i in range(1,n+1):
    if(i%7==0) and (i%2==1) and (i%3==1) and (i%4==1) and (i%5==1) and (i%6==1):
     licznik+=1
     print(i)
print(licznik)