# Import itertools to generate combinations
import itertools

# Function to generate 3-bit binary strings
def generate_3_bit_strings():
    return [''.join(seq) for seq in itertools.product('01', repeat=3)]

# Function to add two binary strings and return the result as a binary string
def add_binary_strings(bin_str1, bin_str2):
    # Convert binary strings to integers, add them, and convert back to binary string
    result = bin(int(bin_str1, 2) + int(bin_str2, 2))[2:]
    return result

# Generate the 3-bit binary strings
binary_strings = generate_3_bit_strings()

# Store all possible outcomes
outcomes = set()

# Iterate over all pairs of binary strings
for x in binary_strings:
    for y in binary_strings:
        result = add_binary_strings(x, y)
        outcomes.add(result)
        print(f"x: {x}, y: {y}, result: {result}")

# Output all possible outcomes
print("All possible outcomes:", sorted(outcomes))
