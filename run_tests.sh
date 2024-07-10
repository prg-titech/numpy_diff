#!/bin/bash

# Declare an array of test files and their descriptions
test_files=(
  "linalg_solve.py"
  "gradient.py"
  "all_any.py"
  "nonzero.py"
  "linalg_lstsq.py"
  "dtype_init.py"
  "loadtxt_genfromtxt.py"
  "can_cast.py"
  "unique.py"
  "scalar_repr.py"
)
descriptions=(
  "Incompatibility: Broadcasting rules for np.linalg.solve(a, b) were changed in NumPy 2.0.0."
  "Incompatibility: Return value of np.gradient was changed from a list to a tuple in NumPy 2.0.0."
  "Incompatibility: Behavior of np.all and np.any was changed for string arrays in NumPy 2.0.0."
  "Incompatibility: np.nonzero behavior was changed to consider whitespace True in string arrays in NumPy 2.0.0."
  "Incompatibility: Default value of rcond parameter in np.linalg.lstsq was changed in NumPy 2.0.0."
  "Incompatibility: Interpretation of strings with commas to initialize dtype was changed in NumPy 2.0.0."
  "Incompatibility: Default encoding for np.loadtxt and np.genfromtxt was changed in NumPy 2.0.0."
  "Incompatibility: np.can_cast cannot be called for Python int, float, and complex in NumPy 2.0.0."
  "Incompatibility: Behavior of np.unique was changed in NumPy 2.0.0."
  "Incompatibility: The representation of NumPy scalars has been updated to include type information in NymPy 2.0.0."
)

echo "---------------------------------------------"
for i in "${!test_files[@]}"; do
  test_file="${test_files[$i]}"
  description="${descriptions[$i]}"
  
  echo "$description"
  echo "@ Running $test_file with numpy 1.26.4"
  source venv1/bin/activate
  python3 "src/$test_file"
  deactivate

  echo "@ Running $test_file with numpy 2.0.0"
  source venv2/bin/activate
  python3 "src/$test_file"
  deactivate

  echo "---------------------------------------------"
done
