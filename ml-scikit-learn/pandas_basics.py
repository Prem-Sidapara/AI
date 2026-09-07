


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





import matplotlib.pyplot as plt 

plt.figure(figsize=(10,4))

# Graph 1 - Experience vs salary
plt.subplot(1, 2, 1)
plt.scatter(df["years_experience"], df["salary_lakhs"] , color="steelblue")
plt.xlabel("YEars of experience")
plt.ylabel("Salary (lakhs)")
plt.title("Experience vs salary")

# Graph 2 - Avg salary vs education
plt.subplot(1, 2, 2)
labels = ["Bachelore", "Master", "phd"]
values = [5.06, 7.04, 10.55]
plt.bar(labels, values, color=["#ff0000", "#00ff00", "#000000"])
plt.ylabel("Avg Salary (Lakhs)")
plt.title("Salary by Education")
plt.tight_layout()
plt.savefig("salary_charts.png")
plt.show()
print("Chart saved!")