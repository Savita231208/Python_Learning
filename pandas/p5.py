#creating data frame with row labels and column label
import pandas as pd
df=pd.DataFrame([1,2,3,4],['a','b','c','d'],['Marks'])
print(df)

data = [['A',10],['B',12],['C',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df.loc[0])