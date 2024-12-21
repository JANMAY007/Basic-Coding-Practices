import numpy as np
import pandas as pd
p={'items':['apples', 'apples', 'oranges', 'oranges', 'guns', 'guns'],'days':['monday','tuesday','wednesday','thursday','friday','saturday'],'sales':[100,80,200,100,5,10]}
print(p)
df=pd.DataFrame(p,index=[1,2,3,4,5,6])
print(df)
dfg=df.groupby('items')
#print(dfg)
print(dfg.mean())