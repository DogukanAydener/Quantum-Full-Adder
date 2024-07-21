# Quantum Full Adder

This repository contains a quantum full adder implemented using Qiskit. A full adder is a digital circuit that performs addition of binary numbers. In this implementation, the addition is performed using quantum gates on a quantum computer simulator.

## Overview

The quantum full adder takes two decimal numbers as input, converts them to binary, and then performs the addition using quantum circuits. The result is displayed in both binary and decimal forms. The implementation leverages the Qiskit library to create and manipulate quantum circuits and the AerSimulator for simulation.

## Features

- Converts decimal numbers to binary
- Constructs a quantum circuit to perform binary addition
- Measures and displays the result in both binary and decimal formats
- Optional visualization of the quantum circuit and histogram of results
- Supports explicit analysis of 2-bit, 3-bit, and 4-bit additions

## Installation
!!!! May added later !!!

### Prerequisites

- Python 3.7 or higher
- Qiskit (v.1.1.1)
- Matplotlib

### Install Qiskit and Matplotlib

You can install the required libraries using pip:

```bash
pip install qiskit matplotlib
```

## Usage

To use the quantum full adder, you can either run the provided Python script directly or use the batch file for convenience.

### Running the Python Script
Run the script using Python:

```bash
python Addition.py
```

### Running with the Batch File

For simple usage, you can run the addition_app.bat file, which will execute the Addition.py script:

```bash
addition_app.bat
```

 ### Analyzing Specified Bit Additions
The repository also includes a file named Specified addition for explicitly analyzing 2-bit, 3-bit, and 4-bit additions. You can refer to this file to see specific examples and understand how the quantum full adder handles different bit lengths.

## Contact
For questions or support, please open an issue in the repository or contact the maintainer.




## Additional Information

This project demonstrates the application of quantum computing in performing arithmetic operations. For more information on quantum computing and Qiskit, check out the following resources:

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Quantum Computing: An Introduction](https://quantum-computing.ibm.com/)


## Note on Qiskit Versions

This project uses Qiskit version 1.1.1. For new versions of Qiskit, the code and operations may vary. Ensure to check the relevant documentation and update the code accordingly if you are using a newer version of Qiskit.