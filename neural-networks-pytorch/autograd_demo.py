


import torch 

# requires_grad = True -> "is tensor ka gradient track karo"
m = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

# data - same jo gradient descent me tha 

hours = torch.tensor([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0])
scores = torch.tensor([52.0, 58.0, 65.0, 70.0, 75.0, 82.0, 99.0, 92.0])

# 1000 rounds of training 
for epoch in range(1000):
    predictions = m * hours + b 
    loss = ((predictions - scores) ** 2).mean()
    
    loss.backward()     # pytorch khud gradient calculate karta hai

    with torch.no_grad():    # gradient tracking temporary off
        m -= 0.01 * m.grad 
        b -= 0.01 * b.grad
    
    m.grad.zero_()      # gradient reset for next round 
    b.grad.zero_()

    if epoch % 200 == 0:
        print(f'''Epoch {epoch:4d} -> loss: {loss.item():.1f}, m: {m.item():.3f}, b: {b.item():.3f}''')
    
print(f"\nFinal: m={m.item():.3f}, b={b.item():.3f}")
print(f"9 hours → {m.item()*9 + b.item():.1f} marks")