import numpy as np

a = np.array( [[1, 2], [3, 4], [5,6]])
b = np.array([[2, 4]])
c = a.copy()
k = a.shape
print(a[1][0])
print(k)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        n = a[i][j] + b[0][j]
        c[i][j] = n

print(c)

