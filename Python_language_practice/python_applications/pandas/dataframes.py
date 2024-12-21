import numpy as np
import pandas as pd
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,0,1,2]
d=[3,4,5,6]
e=[7,8,9,0]
df=pd.DataFrame([a,b,c,d,e],['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
df['T']=df['W']+df['X']+df['Y']+df['Z']
print(df)
df=df.drop('E')
print(df)
#df=df.drop('D', inplace=True)
#print(df)
df=df.drop('T',axis=1)
print(df)