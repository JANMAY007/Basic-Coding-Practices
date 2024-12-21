import pandas as pd
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,0,1,2]
d=[3,4,5,6]
e=[7,8,9,0]
df=pd.DataFrame([a,b,c,d,e],['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df['W'])
print(df.loc['A'])#loc=location
print(df.iloc[1])
print(df.loc['B','X'])#accesing elements
#conditional accesings
print(df<=4)
print(df[df<5])
print(df[df['W']>3])#[['W','X']])