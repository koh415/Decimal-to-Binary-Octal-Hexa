# Sidney Levine
# This program converts a decimal to binary, octal and hexadecimal
# input for decimal
number = int(input("Enter a decimal number: "))

# Print functions with built in functions for computation
print(number)
# Prefix for binary is 0b
print("Binary: ", bin(number))
# Prefix for Octal is 0o
print("Octal: ", oct(number))
# Prefix for Hexadecimal is 0x
print("Hexadecimal: ", hex(number))