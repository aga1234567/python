slo = {"pierwszy" : 876543223453, "drugi" : 2 }
slo["trzeci"]=3
del slo["pierwszy"]

val = 2
for key, value in dict(slo).items():
        if value == val:
            del slo[key]

print(slo)
print(slo.items())

