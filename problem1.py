#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

number = float(input("pick a number"))

print("=============================")
print("Determine if the number is an even number.")
print("=============================")
a = number
b = 22
value = a==b
print(value)
if value:
  print("The if statement is executed because")
  print("the condition is true")
print("=============================\n\n\n")
