import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x
z = x + y
# print(x)
# print(y)
# print(z)
plt.plot(x, y)
plt.show()
plt.plot(x, y, x, x)
plt.show()
plt.plot(x, x, x, y, y, x, x, z, z, x)
plt.show()
