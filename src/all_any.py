import numpy as np

# np.all and np.any
# np.all returns True if all elements of an array evaluate to True.
# np.any returns True if at least one element of an array evaluates to True.
# The behavior of these functions was changed for string arrays in NumPy 2.0.0.
# Previously, only non-empty strings were considered True.

arr = np.array(['a', '', 'c'])
try:
    print(np.all(arr))
    print(np.any(arr))
except TypeError as e:
    print(f"Error: {e}")