# Sidney Levine
# This program converts a decimal to binary, octal and hexadecimal
# input for decimal
number = int(input("Enter a decimal number: "))

# Print functions with built in functions for computation
print()
print(number,'\n')
# Prefix for binary is 0b
print("Prefix for binary is 0b")
print("Binary: ", bin(number), '\n')
# Prefix for Octal is 0o
print("Prefix for Octal is 0o")
print("Octal: ", oct(number), "\n")
# Prefix for Hexadecimal is 0x
print("Prefix for Hexadecimal is 0x")
print("Hexadecimal: ", hex(number))