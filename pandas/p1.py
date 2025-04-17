# making a dataframe with a dictionary of series 

import pandas as pd
s1=pd.Series(['a','b','c','d'],index=['r1','r2','r3','r4'])
s2=pd.Series(['e','f','g','h'],index=['r1','r2','r3','r4'])
s3=pd.Series(['i','j','k','l'],index=['r1','r2','r3','r4'])
print(s1,s2,s3)
dic1={"a1":s1,'a2':s2,'a3':s3}
print(dic1)