import numpy as np

# np.dtype
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#cleanup-of-initialization-of-numpy-dtype-with-strings-with-commas
# The interpretation of strings with commas to initialize dtype has been changed.
# A trailing comma now always creates a structured dtype.

# In NumPy 2.0.0, a trailing comma creates a structured dtype with a single field.
dt = np.dtype("i,")
print(dt)
