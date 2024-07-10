# NumPy Compatibility Testing

This repository contains scripts to test the compatibility and behavior differences between NumPy versions 1.26.4 and 2.0.0. The scripts cover various NumPy functions that have different behaviors or outputs in these versions.

[NumPy 2.0.0 Release Notes#Changes](https://numpy.org/doc/stable/release/2.0.0-notes.html#changes)

## Prerequisites

- Python 3.x
- Virtual environment tool (e.g., `venv`)

## Setup

1. Clone this repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Run the setup script to create virtual environments and install the required NumPy versions:
    ```sh
    chmod +x setup.sh (only when the first run)
    ./setup.sh
    ```

## Running the Tests

To run the tests for both NumPy versions, execute the `run_tests.sh` script:

```sh
chmod +x run_tests.sh (only when the first run)
./run_tests.sh
```
