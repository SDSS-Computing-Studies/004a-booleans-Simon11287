#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"


print("=============================")
print("Determine if a number is larger than 100 ")
print("=============================")
A = float(input("pick a number: "))
B = 100

Equal = True
Smaller=  True
Larger = True

if A > B :
  print("The number is larger than 100")

elif A < B :
  print("The number is smaller than 100")

else :
  print("The number is 100")
  
print("=============================\n\n\n")
