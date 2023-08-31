import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

average_age = df['Age'].mean()
print("Average Age:", average_age)
