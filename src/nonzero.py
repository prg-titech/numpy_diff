import numpy as np

# np.nonzero
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#truthiness-of-numpy-strings-changed
# Returns the indices of the elements that are non-zero.
# For string arrays, the behavior was changed in NumPy 2.0.0
# so that whitespace is now considered True.

arr = np.array([' ', 'a', ''])
print(np.nonzero(arr))
