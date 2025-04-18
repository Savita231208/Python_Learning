#to add column into a dataframe
import pandas as pd
df['three']=pd.Series([6,7,8],index=['a','b','d'])
print(df)
#to add rows into a dataframe
df3 = pd.DataFrame([[5, 6], [7, 8]], index=['a','b'])
df = df._append(df3)
print(df)
#to drop rows
df.drop('a')