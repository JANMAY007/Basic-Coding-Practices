from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x
z = x + y
plt.subplot(3, 2, 1)
plt.plot(x, y)
plt.subplot(3, 2, 2)
plt.plot(x, z)
plt.subplot(3, 2, 3)
plt.plot(y, z)
plt.subplot(3, 2, 4)
plt.plot(z, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.subplot(3, 2, 5)
plt.subplot(3, 2, 6)
plt.plot(x, y, z, x)
plt.tight_layout()
plt.show()
