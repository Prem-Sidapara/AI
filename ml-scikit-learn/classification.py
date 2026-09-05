


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Features: [hours_studied, sleep_hours]
X = np.array([
    [2, 5], [3, 6], [1, 4], [5, 7], [6, 8],
    [4, 6], [7, 9], [1, 3], [8, 8], [2, 4],
    [6, 7], [3, 5], [9, 8], [1, 2], [5, 6],
])

# Labels: 1 = Pass, 0 = Fail
y = np.array([0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
print(classification_report(y_test, predictions, target_names=["Fail", "Pass"], labels=[0, 1]))
