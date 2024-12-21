import numpy as np
import pandas as pd
f={'a':[1,2,3,4,5],'b':[6,7,8,9,np.nan],'c':[0,1,2,np.nan,np.nan],'d':[3,4,np.nan,np.nan,np.nan],'e':[5,np.nan,np.nan,np.nan,np.nan]}
df=pd.DataFrame(f)
#df=pd.DataFrame(f,index=[1,2,3,4,5])
print(f)
print(df)
print(df.dropna(axis=1))#default axis=0
print(df.dropna(thresh=3))
print(df['b'].fillna(1))
print(df['c'].fillna(value=df['b'].mean()))