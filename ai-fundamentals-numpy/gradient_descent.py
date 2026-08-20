




import numpy as np 

hours = np.array([1,2,3,4,5,6,7,8], dtype=float)
scores = np.array([52, 58, 65, 70, 75, 82, 99, 92], dtype=float)

m = 0.0 
b = 0.0
learning_rate = 0.01
n = len(hours)

for epoch in range(1000):
    predictions = m * hours + b  
    loss = np.mean((predictions - scores) ** 2 )
    gradient_m = (2/n) * np.sum((predictions - scores ) * hours)
    gradient_b = (2/n) * np.sum(predictions - scores)
    m = m - learning_rate * gradient_m 
    b = b - learning_rate * gradient_b 


    # ye formulas real me nahi likhte 
    # bas samajhne ke liye 
    # ki andar kya ho raha hai
    # real world me ham Pytorch ,Tensorflow, scikit-learn use karenge 
    # loss.backward()
    # optimizer.sleep() is tarike se 

    if epoch % 200 == 0:
        print(f"Epoch {epoch:4d} -> loss: {loss:.1f}, m: {m:.3f}")

print(f"\nFinal m = {m:.3f}, b = {b:.3f}")
print(f"9 hours padha -> predicted score : {m * 9 + b:.1f}")



# m sirf ek single number nahi hai 
# puri ek matrix hoti hai 
