# Quantum Full Adder

This repository contains a quantum full adder implemented using Qiskit. Quantum full adder is a quantum circuit that performs addition of binary numbers. In this implementation, the addition is performed using quantum gates on a quantum computer simulator.

## Overview

The quantum full adder takes two decimal numbers as input, converts them to binary, and then performs the addition using quantum circuits. The result is displayed in both binary and decimal forms. The implementation leverages the Qiskit SDK to create and manipulate quantum circuits and the AerSimulator for simulation.

## Features

- Converts decimal numbers to binary
- Constructs a quantum circuit to perform binary addition
- Measures and displays the result in both binary and decimal formats
- Optional visualization of the quantum circuit and histogram of results


## Installation

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook
- Qiskit (v1.1.1)
- Qiskit Aer (0.14.2)
- Matplotlib


### Install Jupyter Notebook, Qiskit, Qiskit Aer and Matplotlib

You can install the required libraries and software using pip:

```bash
pip install qiskit qiskit_aer matplotlib notebook
```

## Usage

To use the quantum full adder, you can either run the provided Python script directly or use the batch file (Windows only) for convenience.

### Running the Python Script
Run the script using Python:

```bash
python Addition.py
```

### Running with the Batch File (Windows only)

For simple usage, you can run the addition_app.bat file, which will execute the Addition.py script:

```bash
addition_app.bat
```

## Analyzing Specified Bit Additions
The repository also includes a file named "Specified addition" for explicitly analyzing 2-bit, 3-bit, and 4-bit additions. You can refer to this file to see specific examples and understand how the quantum full adder handles different bit lengths.

## Memory Requirements

- For inputs up to **511**, you need **16GB (16128M)** of RAM.
- For inputs between **512** and **1023**, you need exactly **16GB (16384MB)** of RAM.
- For inputs between **1024** and **2047**, you need **128GB** of RAM.
- For inputs over **2048**, you need **1TB** of RAM...



## Contact
For questions or support, please open an issue in the repository or contact the maintainer.




## Additional Information

This project demonstrates the application of quantum computing in performing arithmetic operations. For more information on quantum computing and Qiskit, check out the following resources:

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Platform](https://quantum.ibm.com/)


## Note on Qiskit Versions

This project uses Qiskit version 1.1.1. For new versions of Qiskit, the code and operations may vary. Ensure to check the relevant documentation and update the code accordingly if you are using a newer version of Qiskit.