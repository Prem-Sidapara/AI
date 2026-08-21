

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np 


hours = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1, 1)
scores = np.array([52,58,65,70,75,82,88,92,95,98])

# Train/Test split = 80% train , 20% test
X_train , X_test , Y_train , Y_test = train_test_split(
    hours, scores, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Model banao aur train kario 
model = LinearRegression()
model.fit(X_train, Y_train) # gradient descent iske andar ho raha hai 

# Results 
print(f"\n m (slope):   {model.coef_[0]:.3f}")
print(f" b (intercept): {model.intercept_:.3f}")

# Predict 
predictions = model.predict(X_test)
for actual, pred in zip(Y_test, predictions):
    print(f"Actual: {actual}, predicted: {pred:.1f}")


from sklearn.metrics import r2_score, mean_absolute_error

r2 = r2_score(Y_test, predictions)
mae = mean_absolute_error(Y_test, predictions)

print(f"\n R² score: {r2:.3f}") # 1.0 = perfect, 0 = random 
print(f"MAE:    {mae:.3f}") # average error in marks