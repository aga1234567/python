fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
przykład = [x for x in range(0,100) if x%2==0]
print(przykład)
przykład = [100*i for i in range(0,100) if i%2==0]
print(przykład)
przykład = [x for x in range(0,200) if x%3==0]
print(przykład)

przestepny = [x for x in range(0,2022) if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)]
print(przestepny)
print("ok")
a=0
szesciany = [x for x in range(10,100) if (x**3)]
print(szesciany)



