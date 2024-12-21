import numpy as np
import plotly as pl
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as po
import cufflinks as cf
po.init_notebook_mode(connected=True)
cf.go_offline()
df1=pd.DataFrame(np.random.rand(100,5),columns=['a','b','c','d','e'])
#print(df1)
df2=pd.DataFrame({'x':['a','b','c','d','e'],'y':[1,2,3,4,5],'z':[6,7,8,9,0]})
#print(df2)
df1.iplot(kind='surface',x='a',y='b',mode='markers')
plt.show()