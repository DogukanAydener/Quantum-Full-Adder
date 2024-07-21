#import required libarries

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from IPython.display import display
import matplotlib.pyplot as plt






print("##########  Addition Calculator  ##########")
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



# Qubit number(n) selection

if len(x)>len(y):
    n = len(x)
else:
    n = len(y)


#A is first number's register and B is second number's register.

A = QuantumRegister(n, 'A')
B = QuantumRegister(n , 'B')

S = QuantumRegister(n , 'Sum')
C = QuantumRegister(n , 'Carry')
R = QuantumRegister(n+1 , 'Result')

Ans = ClassicalRegister(n+1 ,'Answer')

qc = QuantumCircuit(A,B,S,C,R,Ans)






#installation of input numbers to the quantum circuit

for i, bit in enumerate(x):
    if bit == '1':
        qc.x(A[i])

for i, bit in enumerate(y):
    if bit == '1':
        qc.x(B[i])





qc.barrier()

#Add A[n] and B[n] values and copy them in S[n] (Sum) register

for i in range(n):
    qc.cx(A[i],S[i])
    qc.cx(B[i],S[i])


qc.barrier()

#checks if both A[n] and B[n] are '1' and copy result on C[n] (carry) register


for i in range(n):
    qc.ccx(A[i],B[i],C[i])



qc.barrier()

#apply sum to result
for i in range(n):
    qc.cx(S[i],R[i+1])


#carry modification
for i in range(n-1):
    qc.ccx(R[n-1-i],C[n-1-i],C[n-2-i])

#modified carry to result
for i in range(n):
    qc.cx(C[i],R[i])



qc.barrier()


for i in range(n+1):
    qc.measure(R[n-i],Ans[i])



d = input("Show circuit (y/n)")

if d == "y":
    fig, ax = plt.subplots(figsize=(10, 5)) 
    qc.draw("mpl", ax=ax)
    plt.show()

    
else:
    pass



from qiskit_aer import AerSimulator


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

# Print the decimal value
#print(f"Decimal value of binary {binary_number} is: {decimal_value}")

print("")
print("")

print(f"Result in terms of binary;\n {x} + {y} = {binary_number}")
print("")
print(f"Result in decimal; \n {decimal1} + {decimal2} = {decimal_value}")




