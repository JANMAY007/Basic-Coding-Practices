from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x
z = x + y
plt.plot(x, y)
plt.show()
fig = plt.figure()
print(fig)
axes = fig.add_axes([0.1, 0.1, 1, 1])  # controlling the axes
axes.plot(x, y)
plt.show()
