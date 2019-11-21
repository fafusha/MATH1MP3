d = open("data.txt", "r")
dp = open("dataplus.txt", "w")
dm = open("dataminus.txt", "w")
for l in d:
    n = int(l)
    if n < 0:
        dm.write(l)
    elif n > 0:
        dp.write(l)
