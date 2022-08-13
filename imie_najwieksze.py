import string
lista=["Adamm","Karolina","Mir  ka","LENA","Krys   tian","Krzysztof"]
max=len(lista[0])
min=len(lista[0])
lista2=[]
lista3=[]
for i in range (0,len(lista)):
    lista2.append((lista[i]).upper())
    lista3.append(lista[i].translate({ord(c): None for c in string.whitespace}))
for i in range(0, len(lista3)):
    if len(lista[i])>max:
        max=len(lista[i])
        a=lista[i]
    if len(lista[i])<min:
        min=len(lista[i])
        b=lista[i]
print(a)
print(b)
print(sorted(lista2,key=len))
print(lista3)



