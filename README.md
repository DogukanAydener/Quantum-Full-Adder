# Quantum Full Adder

This repository contains a Jupyter notebook demonstrating a quantum full adder implemented using Qiskit. A full adder is a digital circuit that performs addition of three binary bits, outputting a sum and a carry bit. This quantum full adder extends the classical full adder concept to quantum computing, leveraging the principles of superposition and entanglement.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Restrictions](#restrictions)
- [License](#license)

## Introduction

A full adder is a fundamental component in digital circuits, used for binary addition. In classical computing, it adds three input bits (two significant bits and a carry bit) to produce a sum and a carry output. This notebook demonstrates how to implement a full adder using quantum gates with Qiskit, a Python library for quantum computing.

## Installation

To run the notebook, you'll need to have Python and Jupyter Notebook installed, along with Qiskit. You can install the required packages using pip:

```bash
pip install qiskit
pip install jupyter
```

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/DogukanAydener/Quantum-Full-Adder.git
cd Quantum-Full-Adder
```

## Usage

1. Open the Jupyter notebook:

    ```bash
    jupyter notebook Addition_combined.ipynb
    ```

2. Follow the instructions in the notebook to execute the cells. The notebook will prompt you to input two decimal numbers to be added. These numbers will be converted to binary, padded to equal length, and processed by the quantum full adder circuit.

3. The resulting sum and carry will be displayed as both binary and decimal values.

### Example

When prompted, input two decimal numbers:

```
Enter the first decimal value: 5
Enter the second decimal value: 3
```

The notebook will output the binary representations and the result of the addition:

```
Binary representation of 5: 0101
Binary representation of 3: 0011
Result: 8
```

## Restrictions

- The notebook uses basic quantum gates and is intended for educational purposes. It may not be optimized for performance on large-scale quantum computers.
- The input numbers must be non-negative integers.
- Ensure that you have a working installation of Qiskit and access to a quantum simulator or quantum hardware if running on actual quantum devices.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
