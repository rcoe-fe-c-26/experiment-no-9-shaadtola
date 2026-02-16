# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Shaad Tola
# Date:

print("--- Factorial Finder ---\n")
a = int(input("Enter Number: "))
if a<0:
    print(f"Factorial of {a} is Not Defined")
fact = 1
for x in range(1,a+1):
    fact = fact*x 
print(f"Factorial of {a} is",fact)


