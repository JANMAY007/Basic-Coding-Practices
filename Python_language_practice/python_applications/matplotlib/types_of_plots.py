from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x
z = x + y
plt.plot(3, 2, 1)
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
plt.show()
plt.hist(x, y, label='medians')
plt.legend(loc=10)
plt.show()
