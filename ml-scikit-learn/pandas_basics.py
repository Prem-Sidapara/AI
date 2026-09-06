


import pandas as pd 

df = pd.read_csv("salary_data.csv")

# print("Shape:", df.shape)
# print("\nFirst 3 rows:")
# print(df.head(3))
# print("\nStats:")
# print(df.describe())
# print("\nMissing values:")
# print(df.isnull().sum())



#Filter: sirf Masters/PHD waale (education >= 1)
high_edu = df[df["education"] >= 1]
print(f"\nHigh education employees: {len(high_edu)}")

# New column add karo 
df["salary_lakhs"] = df["salary"] / 100000
print("\nSalary in lakhs (first 5):")
print(df[["years_experience", "salary_lakhs"]].head())

# Group by: education level ke hisaab se average salary
avy_by_edu = df.groupby("education")["salary"].mean()
print("\nAverage salary by education:")
print(avy_by_edu)