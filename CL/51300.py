d1 = {2:3, 8:19, 6:4, 5:12}
d2 = {2:5, 4:3, 3:9}
d3 = {}
for k1 in d1.keys():
    if not k1 in d2.keys():
        d3[k1]  = d1[k1]

for k2 in d2.keys():
    if not k2 in d1.keys():
        d3[k2]  = d2[k2]

print(d3)
