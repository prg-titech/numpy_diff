import numpy as np

# np.linalg.pinv
# Compute the (Moore-Penrose) pseudo-inverse of a matrix.
# In NumPy 2.0.0, the behavior of np.linalg.pinv was changed.

a = np.array([[1, 2], [3, 4], [5, 6]])

# Compute the pseudo-inverse of the matrix
pinv_result = np.linalg.pinv(a)
print(f"Result of np.linalg.pinv:\n{pinv_result}")
