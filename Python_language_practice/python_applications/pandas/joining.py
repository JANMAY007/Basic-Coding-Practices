import numpy as np
import pandas as pd
x1={'a':[1,2,3],'b':[4,5,6]}
y1={'c':[7,8,9],'d':[0,1,2]}
x=pd.DataFrame(x1,index=['p','q','r'])
y=pd.DataFrame(y1,index=['P','v','w'])
#print(x1)
#print(y1)
#print(x)
#print(y)
print(x.join(y))
print(y.join(x,how='right'))