n=int(input("Podaj n"))
for i in range(n,0,-1):
   if(i%7==0) and (i%2==1) and (i%3==1) and (i%4==1) and (i%5==1) and (i%6==1):
    break
print(i)