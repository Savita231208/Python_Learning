#Concatenating data frame
import pandas as pd
df1=pd.DataFrame([[1,'brijesh',3],[4,5,6]],index=['first','second'])
df2=pd.DataFrame([[7,8,9],[10,11,12]],index=['first','second'])
df3=pd.concat([df1,df2])
print(df3)
df4=pd.concat([df1,df2],keys=(['x','y']))
print(df4)
df5=pd.concat([df1,df2],ignore_index=True)
print(df5)