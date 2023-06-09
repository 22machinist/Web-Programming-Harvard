#In this file we will deal with expeted error 

#Importing file which contains exit function
import sys

#taking input from user 

x = int(input("x: "))
y = int(input("y: ")) 

try :
    result = x / y 
except ZeroDivisionError :
    print("Error can't divide with 0!")
    sys.exit(1) 

print(f"Quotient is : {result}")
