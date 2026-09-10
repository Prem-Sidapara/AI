


import torch 
import torch.nn as nn 

# neural network define karo 
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(1, 8),    # 1 input -> 8 neurons
            nn.ReLU(),          # activation
            nn.Linear(8, 1)     # 8 neurons -> 1 output
        )
    
    def forward(self, x):
        return self.layers(x)

# data

hours  = torch.tensor([[1.],[2.],[3.],[4.],[5.],[6.],[7.],[8.]])
scores = torch.tensor([[52.],[58.],[65.],[70.],[75.],[82.],[88.],[92.]])

model = SimpleNN()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.01)
loss_fn = nn.MSELoss()

# training loop
for epoch in range(1000):
    pred = model(hours)
    loss = loss_fn(pred, scores)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f"Epoch {epoch:4d} -> loss: {loss.item():.2f}")

# predict 
test = torch.tensor([9.0])
print(f"\n 9 hours -> {model(test).item():.1f} marks")