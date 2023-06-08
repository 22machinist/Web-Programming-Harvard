#In this python file we will create objects 

class Point() :
    #now we will define the def value with in-built function "__inint__"
    def __init__(self , input1 , input2) :
        self.x = input1      #Storing the value in x-property
        self.y = input2       #Storing the value in the y-property 


#Now we will check the object 
p = Point(8 , 9)

print(p.x)
print(p.y)