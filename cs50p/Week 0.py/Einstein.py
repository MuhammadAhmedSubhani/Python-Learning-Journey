""" 
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer 
(in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input 
an integer.
"""

m = int(input("Enter Mass in kg: "))
c = 300000000
E =m * c**2 
print("E =",E)

# Samples of input and expected output 
# Run your program with python einstein.py. Type 1 and press Enter. Your program should output:
# 90000000000000000
# Run your program with python einstein.py. Type 14 and press Enter. Your program should output:
# 1260000000000000000
# Run your program with python einstein.py. Type 50 and press Enter. Your program should output
# 4500000000000000000

