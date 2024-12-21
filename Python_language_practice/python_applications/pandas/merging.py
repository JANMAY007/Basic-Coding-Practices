import numpy as np
import pandas as pd
df1=pd.DataFrame({'key1':[1,2,3],'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'key2':[9,5,6]})
df2=pd.DataFrame({'key1':[1,2,3],'d':[1,2,3],'e':[2,2,3],'f':[4,3,8],'key2':[9,5,6]})
print(pd.merge(df1,df2,how='right',on=['key1','key2']))#try with only one key also