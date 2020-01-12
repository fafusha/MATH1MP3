f = open("numbers.txt", "r")
maxn  = 0
runsum = 0

for l in f:
    n = int(l)
    print(n > maxn)
    if n > maxn:
        maxn = n
        runsum += n

print(runsum)
