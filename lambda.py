#this file's first section contains how to compare a dict inside a list 

persons = [ 
    {"name" : "Harry" , "house" : "England"} , 
    {"name" : "Jack" , "house" : "UK"} , 
    {"name" : "Tyrone" , "house" : "Phyladelphia"} ,
    {"name" : "Glen" , "house" : "Las vegas"}
]

#defining the function to tell which key is going to be used 
def f(person) :
    return person["name"]

#Declaring the sort-out function 
persons.sort(key=f)

#printing out the sorted data 
print(persons)

#To define the above function we can do the same in different way 
#Defining the list 

World = [
    {"name" : "Russia" , "capital" : "Moscow"},
    {"name" : "USA" , "capital" : "Washington DC"},
    {"name" : "Germany" , "capital" : "Berlin"},
    {"name" : "India" , "capital" : "Delhi"},
    {"name" : "France" , "capital" : "Paris"},
    {"name" : "UK" , "capital" : "London"}
]

World.sort(key=lambda World: World["name"])

print(World)