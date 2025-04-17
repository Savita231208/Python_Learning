# create a dataframe dictionary of list
import pandas as pd
data = {
"Student": ["Brijesh", "Akash", "Saurabh", "Manik"],
    "Python": ["A", "B", "C", "A"],
    "Java": ["A", "A", "B", "B"],
    "DSA": ["A", "C", "B", "A"]
}
df = pd.DataFrame(data)
print(df)