
 # create a list of dictionary 
import pandas as pd
students_subjects = [
    {"Student": "Brijesh", "Python": "A", "Java": "A", "DSA": "A"},
    {"Student": "Akash", "Python": "B", "Java": "A", "DSA": "C"},
    {"Student": "Saurabh", "Python": "C", "Java": "B", "DSA": "B"},
    {"Student": "Manik", "Python": "A", "Java": "B", "DSA": "A"},
]
df = pd.DataFrame(students_subjects)
print(df)
