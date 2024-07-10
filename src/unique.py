import numpy as np

# np.unique
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#np-unique-return-inverse-shape-for-multi-dimensional-inputs
# Find the unique elements of an array.
# When multi-dimensional inputs are passed to np.unique with return_inverse=True,
# the unique_inverse output is now shaped such that the input can be reconstructed directly
# using np.take(unique, unique_inverse) when axis=None, and np.take_along_axis(unique, unique_inverse, axis=axis) otherwise.

a = np.array([[1, 2, 2], [3, 3, 3], [4, 4, 5]])

# Find the unique elements of the array and return the indices to reconstruct the input array
unique_result, unique_inverse = np.unique(a, return_inverse=True)
# print(f"Unique result: {unique_result}") # Same results
print(f"Unique inverse: {unique_inverse}")
print(f"Reconstructed array: {np.take(unique_result, unique_inverse)}")
