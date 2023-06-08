# In this file we will add the functions 


#First we will create the square function 
def square(x) :
    output = x * x 
    return output 

#Now we will define the function for addition of two numbers 
def add(x , y) :
    output = x + y 
    return output

#Now we will define the function for Subtraction 
def sub(x , y) :
    output = x - y 
    return output

#Now we will define the function for multiplication 
def mul(x , y) :
    output = x * y 
    return output

#Now we will define the function for division 
def div(x , y) :
    output = x / y 
    return output 

#Now we will create the function to greet the user 
def greet() :
    print("Good Day , Sir !")

#Now we will begin the code 
#First we will ask the user what kind of Operations they wanna perform 
greet() 

print("A & a = Addition")
print("S & s = Subtraction")
print("M & m = Multiplication")
print("D & d = Division")
print("Q & q = Squaring")
a = input("Operation : ")

if (a == "Q" or a == 'q') :
    b = int(input("Number : "))
    out = square(b)
    print(f"The Square of {b} is : {out}")
elif ( a == 'A' or a == 'a') :
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))

    out = add(b , c)
    print(f"Sum of {b} & {c} is : {out}")
elif (a == 'S' or a == 's') :
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    out = b - c 
    print(f"The difference between {b} & {c} is : {out}")
elif (a == 'M' & a == 'm'):
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    out = b * c 
    print(f"The Product of numbers {b} & {c} is : {out}")
elif (a == 'D' & a == 'd'):
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    if ( c == 0 ):
        print("Error!!!!")
    else :
        out = b / c 
        print(f"The Quotient of {b} & {c} is : {out}")
else : 
    print("Unrecognised Command !! Abort")
    