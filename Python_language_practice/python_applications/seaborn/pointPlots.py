import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
diamond=sns.load_dataset('diamonds')
#print(diamond)
sns.distplot(diamond['price'])
plt.show()
sns.rugplot(diamond['x'])
plt.show()
sns.kdeplot(diamond['depth'])
plt.show()