import pandas as pd
df=pd.DataFrame(dic1)
print(df)
df['a4']=["m",'n','o','p']#insert new column
print(df)
df['a3']=["m",'n','o','p']#update column
df.loc['r5']=['q','r','s','t']
print(df)