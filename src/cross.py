import numpy as np

# np.cross
# Returns the cross product of two (arrays of) vectors.
# In NumPy 2.0.0, the function only accepts three-dimensional vectors,
# whereas in previous versions, two-dimensional vectors were also accepted.

vec1 = np.array([1, 2])
vec2 = np.array([3, 4])

cross_product = np.cross(vec1, vec2)
print(cross_product)