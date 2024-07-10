import numpy as np

# np.linalg.lstsq
# Solves the equation a * x = b by computing a vector x that minimizes the Euclidean 2-norm || b - a * x ||.
# In NumPy 2.0.0, the default value of the rcond parameter was changed.

# 100x2 matrix a
m = 10**2
a = np.zeros((m, 2))
a[0, 0] = 1          # Singular value of the first row is 1
a[m-1, 1] = 2.22e-16 # Singular value of the second row is machine precision

# Vector b with 100 elements
b = np.zeros(m)
b[m-1] = 1

# In 1.26.4, if the value is smaller than max singular value * machine precision, it is cut off. 
# In 2.0.0, if the value is smaller than max singular value * machine precision * max(M, N), it is cut off.
try:
    x_default, res_default, rank_default, s_default = np.linalg.lstsq(a, b)
    print(f"Solution with default rcond: {x_default}")
    print(f"Residuals: {res_default}")
    print(f"Rank: {rank_default}")
    print(f"Singular values: {s_default}")
except FutureWarning as e:
    print(f"FutureWarning: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
