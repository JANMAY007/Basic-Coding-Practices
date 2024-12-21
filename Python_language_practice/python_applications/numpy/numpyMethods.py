import numpy as np

w = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = np.array(w)
print(y)
z = np.array(x)
print(z)
print(np.zeros((3, 3)))
print(np.ones((3, 3)))
print(np.eye(30))
print(np.arange(50).reshape(2, 25))
print(np.linspace(0, 100, 11))
print(z.transpose())
print(z.flatten())
print(np.concatenate(x, axis=1))
a = np.array([1, 2, 3], int)
b = np.array([4, 5, 6], int)
print(a >= b)
print(b < 7)
print(any(a))
print(all(b))
print(np.where(a != 0, 1 / a, a))
