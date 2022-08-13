"""lista = [i for i in range(0,10)]

newlist = sum(lista)
print(newlist)"""


"""lista = [i for i in range(0,10)]
max=lista[0]
for i in range(0,10):
 if (i>max):
     max=i
print(max)"""
"""suma=0
for i in range(0,10):
 suma=suma+i
print(suma)"""
lista=["kot","pies","kura","krokodyl"]
n=input("Wpisz wyraz")
k=input("Wpisz wyraz 2")
newlist=[]
for i in range(len(lista)):
 if len(n)<len(lista[i]) and len(k)>len(lista[i]):
    newlist.append(lista[i])

print(newlist)
