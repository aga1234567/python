lista_a=[1,2,3,4,5,3,4]
lista_b=[5,4,3,2,1]
listac=[]
for i in range(len(lista_a)):
    if i>=len(lista_b):
     listac.append(lista_a[i])
    else:
     listac.append(lista_a[i]-lista_b[i])
print(listac)

#k(t)
#Zad. domow: program który bierze listę znaków i łączy w napis
#z ["k","o","t"] zrobi "kot"
#z=["k","o","t",9]
#k=""
#for i in range(len(z)):
 #   k+=str(z[i])
#print(k)

#z=["kot"]
#k=""

#for i in range(len(z)):
 #   for j in range(len(z[i])):
 #    k=z[i][j]
 #    print(k)

z="kot"
k=""
for i in range(len(z)):
 k=z[i]
 print(k)
 #"\w\d"
#"a90"
#"b3000"
#"ba1"
#"^[a-z][0-9]*"

