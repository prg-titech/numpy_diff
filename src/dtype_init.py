import numpy as np

# np.dtype
# The interpretation of strings with commas to initialize dtype has been changed.
# A trailing comma now always creates a structured dtype.

# In NumPy 2.0.0, a trailing comma creates a structured dtype with a single field.
dt = np.dtype("i,")
print(dt)
