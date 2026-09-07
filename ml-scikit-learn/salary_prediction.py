



from pandas import col
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error


# Load data

df = pd.read_csv("salary_data.csv")
df["salary_lakhs"] = df["salary"] / 100000

# Features and target

x = df[["years_experience", "education", "age"]]
y = df["salary_lakhs"]

# split + train 

X_train, X_test, Y_train, Y_test = train_test_split(x,y, random_state=42, test_size=0.2)
model = LinearRegression()
model.fit(X_train, Y_train)

# Evaluate

preds = model.predict(X_test)
print(f"R2 score: {r2_score(Y_test, preds):.3f}")
print(f"MAE: {mean_absolute_error(Y_test, preds):.2f} lakhs rupeess")

# Actual vs predicted graph 

plt.figure(figsize=(7,5))
plt.scatter(Y_test, preds, color="steelblue")
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()],"r--")
plt.xlabel("Actual salary (lakhs)")
plt.ylabel("Predicted salary (lakhs)")


# predict for new person 
new = pd.DataFrame([[6,1,30]], columns=["years_experience", "education", "age"])
print(f"\n 6 yers exp, masters, 30 years -> {model.predict(new)[0]:.2f} lakhs/year")