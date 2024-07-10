import numpy as np

# np.gradient (gh-23861)
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#changes
# Calculates the gradient of an N-dimensional array.
# The gradient is calculated using central differences in the interior
# and first differences at the boundaries.
# The return value was changed from a list to a tuple in NumPy 2.0.0.

arr = np.array([[1, 2, 4], [7, 11, 16]])
grad = np.gradient(arr)
print(f"Type of gradient result: {type(grad)}")
print(grad)