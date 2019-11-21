import numpy as np
import random as r

for i in range(20):
    print(r.randrange(1,11))
x = np.arange(28).reshape((7,4))
#print(x)
#print(x[0,3])
#print(x[1:3,1:3])
#print(x[1:3,-1:])
#print(x[:,-1])

x = x[:np.newaxis]

#print(x)
#for i in range(x.shape[1]):
#    print(x[:,i].sum())

k = "hello there 123"

print(k.replace(" ", "!"))


a = np.uint8(-1)
print(a)
