import numpy as np

# np.can_cast
# The behavior of np.can_cast was changed for Python int, float, and complex.
# The result must not depend on the value passed in.

try:
    print(f"np.can_cast(127, np.int8): {np.can_cast(127, np.int8)}")
except TypeError as e:
    print(f"Error: {e}")

try:
    print(f"np.can_cast(127, np.float16): {np.can_cast(127, np.float16)}")
except TypeError as e:
    print(f"Error: {e}")

try:
    print(f"np.can_cast(127, np.complex64): {np.can_cast(127, np.complex64)}")
except TypeError as e:
    print(f"Error: {e}")