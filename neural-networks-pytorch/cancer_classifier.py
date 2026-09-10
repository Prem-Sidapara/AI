


import torch
import torch.nn as nn 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# data load karo 

data = load_breast_cancer()
X = data.data
y = data.target     

# split + scale 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# pytorch tensor me convert karo
X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)
y_train = torch.FloatTensor(y_train).unsqueeze(1)
y_test = torch.FloatTensor(y_test).unsqueeze(1)

# neural network 
class CancerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(30, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()    # 0 to 1 probability 
        )
    def forward(self, x):
        return self.layers(x)


model = CancerNet()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
loss_fn = nn.BCELoss()    # binary cross entropy for yes/no problems 

# train 
for epoch in range(1000):
    pred = model(X_train)
    loss = loss_fn(pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f"Epoch {epoch:4d} -> loss: {loss.item():.4f}")

# Accuracy 
with torch.no_grad():
    test_pred = model(X_test)
    predicted = (test_pred > 0.5).float()
    accuracy = (predicted == y_test).float().mean()
    print(f"\nTest Accuracy: {accuracy.item()*100:.1f}")