#  create a list of dictionary
import pandas as pd
students_subjects = [
    {"Student": "Brijesh", "Python": 65, "Java": 56, "DSA": 98},
    {"Student": "Akash", "Python": 85, "Java": 45, "DSA": 90},
    {"Student": "Saurabh", "Python": 62, "Java": 70, "DSA": 75},
    {"Student": "Manik", "Python": 69, "Java": 45, "DSA": 85},
    {"Student": "Ashish", "Python": 89, "Java": 87, "DSA": 86},
]
df = pd.DataFrame(students_subjects)
print(df)
df.head()
df.tail()
df.describe()
df['Python'].max()
