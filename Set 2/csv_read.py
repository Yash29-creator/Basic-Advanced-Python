import pandas as pd
df = pd.read_csv('C:/Users/Yash/Desktop/P_L/Python/Set 2/Salary_Data.csv')
df=df.drop('YearsExperience', axis=1)
print(df.sum())