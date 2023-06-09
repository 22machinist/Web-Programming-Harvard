#In this file we will deal with expeted error 

#Importing file which contains exit function
import sys

#taking input from user 

try :
    x = int(input("x: "))
    y = int(input("y: ")) 
except ValueError :
    print("Error ! Invalid Input")               #When a character is added on the place of int
    sys.exit(1)
try :
    result = x / y 
except ZeroDivisionError :
    print("Error can't divide with 0!")
    sys.exit(1) 

print(f"Quotient is : {result}")
