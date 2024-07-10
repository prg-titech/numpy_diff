import numpy as np

# np.linalg.solve
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#removed-ambiguity-when-broadcasting-in-np-solve
# - https://github.com/numpy/numpy/blob/e8f93a9803d15fa15aa7f68cf46999c470d8c920/numpy/linalg/_linalg.py#L320
# Solves the linear equation system a * x = b for x.
# Given a square matrix a and a right-hand side matrix b,
# this function computes the solution matrix x.
# In NumPy 2.0.0, the broadcasting rules for np.linalg.solve(a, b)
# were changed, which may lead to different results compared to version 1.26.4.


# 形状 (2, 2, 2)
a = np.array(
  [ [[3, 1], [1, 2]]
  , [[2, 1], [1, 3]] ]) 
# 形状 (2, 2)
b = np.array(
  [ [9, 8]
  , [7, 10] ])

x = np.linalg.solve(a, b)
print(x)
