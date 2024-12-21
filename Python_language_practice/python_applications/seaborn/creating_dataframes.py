import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df1=sns.load_dataset('tips')
#df2=pd.read_csv("ece.csv")
x1=np.random.rand(100,5)
x2=np.random.rand(10,5)
df3=pd.DataFrame(x1,columns=['a','b','c','d','e'])
df4=pd.DataFrame(x2,columns=['a','b','c','d','e'])
sns.distplot(x1)
plt.show()
sns.pointplot(df1['tip'])
plt.show()
df4['a'].plot.line()
#sns.lineplot(x=2,y=5)
plt.show()