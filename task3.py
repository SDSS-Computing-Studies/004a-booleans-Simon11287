#! python3 

# Have the user enter a number. 
# Use an if...elif statement to determine if the number is 
# a) larger than 1000 
# b) larger than 100 
# c) larger than 10 
# d) larger than 0 
# Output must match one of the valid output statements listed
# (2 points)

# Inputs:
# a number

# Output is a single number that represents a range of numbers:
# "3" : The number is equal to 1000 or is larger than 1000
# "2" : The number is 100 or a number up to 1000 
# "1" : The number is 10 or a number up to 100 
# "0" : The number is 0 or a number up to 100 


print("=============================")
print("Determine if a number is larger than 0, 10, 100, 1000")
print("=============================")
A = float(input("pick a number: "))
B = 0
C = 10
D = 100
E = 1000


Larger0 = True
Larger10 =  True
Larger100 = True
Larger1000 = True

if C > A > B or A == B :
  print("The number is larger than 0")

elif D > A > C or A == C:
  print("The number is larger than 10")

elif E > A > D or A == D :
    print("the number is larger then 100")

else :
  print("The number is over 1000")
  
print("=============================\n\n\n")
