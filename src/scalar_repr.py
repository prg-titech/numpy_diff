import numpy as np

# np.float64, np.int32, np.bool_, np.str_
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#representation-of-numpy-scalars-changed
# The representation of NumPy scalars has been updated to include type information.
# In NumPy 2.0.0, scalars are now printed as np.float64(3.0) rather than just 3.0.
# This change helps distinguish NumPy scalars from Python built-in types.


# Define various NumPy scalars
scalar_float = np.float64(3.0)
scalar_int = np.int32(42)
scalar_bool = np.bool_(True)
scalar_str = np.str_("hello")

# Print the scalars
# print(f"NumPy float scalar: {scalar_float}")
# print(f"NumPy int scalar: {scalar_int}")
# print(f"NumPy bool scalar: {scalar_bool}")
# print(f"NumPy string scalar: {scalar_str}")

# Print the representations of the scalars
print(f"Representation of NumPy float scalar: {repr(scalar_float)}")
print(f"Representation of NumPy int scalar: {repr(scalar_int)}")
print(f"Representation of NumPy bool scalar: {repr(scalar_bool)}")
print(f"Representation of NumPy string scalar: {repr(scalar_str)}")
