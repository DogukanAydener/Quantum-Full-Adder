#import required libarries

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display
import matplotlib.pyplot as plt
import os
import msvcrt




while True:
    print("##########  Quantum Full Adder  ##########")
    print("")
    print("")
    print("Enter the decimal values you want to add;")

    # Function to convert a decimal number to binary
    def decimal_to_binary(decimal_value):
        return bin(decimal_value)[2:]

    # Decimal values wanted to add
    decimal1 = int(input("Enter the first decimal value: "))
    decimal2 = int(input("Enter the second decimal value: "))

    # Converting decimal values to binary
    x = decimal_to_binary(decimal1)
    y = decimal_to_binary(decimal2)

    # Padding the shorter binary number with leading zeros
    max_length = max(len(x), len(y))
    x = x.zfill(max_length)
    y = y.zfill(max_length)

    print("")
    print(f"Binary representation of first decimal ({decimal1}) is {x}")
    print(f"Binary representation of second decimal ({decimal2}) is {y}")
    print("")


    print(f"Calculation: \n {decimal1} + {decimal2}")
    print(f"Binary calculation: \n {x} + {y} ")

    print("")
    print("")

    # Qubit number(n) selection

    if len(x)>len(y):
        n = len(x)
    else:
        n = len(y)


    #A is first number's register and B is second number's register.

    A = QuantumRegister(n, 'A')
    B = QuantumRegister(n , 'B')

    C = QuantumRegister(n , 'Carry')

    Ans = ClassicalRegister(n+1 ,'Answer')

    qc = QuantumCircuit(A,B,C,Ans)






    #installation of input numbers to the quantum circuit

    for i, bit in enumerate(x):
        if bit == '1':
            qc.x(A[i])

    for i, bit in enumerate(y):
        if bit == '1':
            qc.x(B[i])


    #checks if both A[n] and B[n] are '1' and copy result on C[n] (carry) register

    for i in range(n):
        qc.ccx(A[i],B[i],C[i])


    qc.barrier()



    for i in range(n):
        qc.cx(A[i],B[i])


    qc.barrier()

    for i in range(n-1):
        qc.ccx(C[n-1-i],B[n-2-i],C[n-2-i])


    for i in range(n-1):
        qc.cx(C[n-1-i],B[n-2-i])

    qc.barrier()


    qc.measure(C[0],Ans[n])

    for i in range(n):
        qc.measure(B[i],Ans[n-1-i])


    d = input("Show circuit (y/n): ")

    if d == "y":
        fig, ax = plt.subplots(figsize=(10, 5)) 
        qc.draw("mpl", ax=ax , fold=-1)
        plt.show()

        
    else:
        pass



    result = AerSimulator().run(qc).result()
    stats = result.get_counts()



    p = input("Show histogram (y/n): ")

    if p == "y":
        fig, ax = plt.subplots(figsize=(5, 5)) 
        plot_histogram(stats, ax=ax)
        plt.show()
        
    else:
        pass



    # Function to convert a binary number to decimal
    def binary_to_decimal(binary_value):
        return int(binary_value, 2)

    # Extract the binary number from stats
    binary_number = list(stats.keys())[0]

    # Convert the binary number to a decimal value
    decimal_value = binary_to_decimal(binary_number)

    print("")
    print("")

    print(f"Result in terms of binary;\n {x} + {y} = {binary_number}")
    print("")
    print(f"Result in decimal; \n {decimal1} + {decimal2} = {decimal_value}")
    print("Press any key to continue...")
    msvcrt.getch()
    os.system('cls')