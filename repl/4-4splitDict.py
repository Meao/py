d = {"key1": 100, "key2": -100}
d1 = {}
d2 = {}
for el in d.items():
    
    if(el[1]>0):
        d1[el[0]] = el[1]
    else:
        d2[el[0]] = el[1]

print(d1,d2)
