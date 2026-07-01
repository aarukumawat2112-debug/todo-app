#simple calculator using if else 
x=int(input("enter the value of x"))
z=input("enter the operator:")
y=int(input("enter the value of y"))
if (z == "+"):  # Addition
 print(x + y)

elif (z == "-"): # Subtraction
 print(x - y)

elif (z == "*"):  # Multiplication
 print(x * y)

elif (z == "/"):  # Division (returns float)
 print(x / y)

elif (z == "//"): # Floor Division (returns integer quotient)
 print(x // y)

else:
 # Executes when the entered operator is not supported
 print("Invalid operator.")