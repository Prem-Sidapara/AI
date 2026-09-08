

import torch

# tensor banao - numpy jaisa hai
t = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print("Tensor: ", t)
print("Shape: ", t.shape)
print("Dtype: ", t.dtype)

# Math - ekdum numpy jevu
print("\n t * 2 = ", t * 2)
print("t + 10 = ", t + 10)
print("t mean = ", t.mean())

# 2D tensor (matrix)
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.9]])
print("\nMatrix shape: ", matrix.shape) 
print(matrix)