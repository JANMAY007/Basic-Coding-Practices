import numpy as np

x = np.arange(1, 26).reshape(5, 5)
print(x)
print(x[2:5, 1:4])
print(x < 12)
print(np.full((3, 3), True))
