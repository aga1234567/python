n=int(input("Podaj n"))
m=int(input("Podaj najwieksza liczbe ktora chcesz"))
z=int(input("wpisz 0 najmiejsza , 1 jak max to 0"))
flaga=0
if (z==1):
  a = n
  b = 0
  c = -1
else:
  a = 0
  b = n
  c = 1
for i in range(a,b,c):
   if(i%7==0) and (i%2==1) and (i%3==1) and (i%4==1) and (i%5==1) and (i%6==1):
       flaga+=1
       if(flaga==m):
        break
print(i)