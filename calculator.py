#This file is created to calculate some basic operations 
print("Welcome to Pheonix basic Calculator Prototype")
a = int(input("Enter Number 1 :"))
b = int (input("Enter Number 2 : ")) 

#Now we will ask for the input about operations what operations user wish to make
print("For Addition : A/a")
print("For Subtraction : S/s")
print("For Multiplication : M/m")
print("For Division : D/d")

#getting operation input from the user
c = input("Operation: ")

#Defining the condtion statements 
if (c == 'A' or c == 'a') :
    print("You defined for Addition .")
    sum = a + b 
    print("Output of your defined operation is : " , sum)
elif (c == 'S' or c == 's') :
    print("You defined for Subtraction")
    sum = a - b 
    print("OUtput for your defined operation is : " , sum)
elif (c == 'D' or c == 'd'):
    print("You defined for Division") 
    if (b == 0):
        print("Error ! Can't divide any number by 0")
    else :
        sum = a / b
        print("Output for your defined operation is : " , sum)
elif (c == 'M' or c == 'm') :
    print("You defined for Multiplication")
    sum = a * b 
    print("Output for your defined opertion is :" , sum)
else :
    print("Invalid Operation defined")
