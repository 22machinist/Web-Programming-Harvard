#In this file we will use the decorators 
#Decorators are type of functions which modifies the other function and returns the other function

def announce(f):
    #Above we announced the decorator 
    #Inside the decorator now we will define another function
    def wrapper() :
        print("About to run the function...")
        f() 
        print("Execution completed !")
    #Now we will return the function 
    return wrapper 

#Now we will run the above decorator 
@announce                                        #Calling the decorator 
#Defining the hello function
def hello() : 
    print("Hello World !")


#Calling the hello function 
hello()