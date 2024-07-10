import numpy as np
import io

# np.loadtxt and np.genfromtxt
# - https://numpy.org/doc/stable/release/2.0.0-notes.html#loadtxt-and-genfromtxt-default-encoding-changed
# Default encoding was changed from 'bytes' to 'utf-8'.

def custom_converter(byte_string):
    # Assume byte_string is a byte, decode it to a string and then convert to float
    return float(byte_string.decode('utf-8'))

# Sample data to be loaded, saved as a text file
data = b"1.1\n2.2\n3.3\n"
with open('data.txt', 'wb') as f:
    f.write(data)

# Load the data using loadtxt with the custom converter
try:
    data = np.loadtxt('data.txt', converters={0: custom_converter})
    print(f"Data loaded successfully: {data}")
except Exception as e:
    print(f"An error occurred: {e}")