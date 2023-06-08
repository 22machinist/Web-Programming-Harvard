#Created the list
names = ["Harry" , "Hermoine" , "Jenny" , "Wales"]
print(names) 

#Now we will use pyton built-in append function to add element to the list 

names.append("Brock")

#Now we will use built-in sort() python function to sort the list 
names.sort()

print("After Adding" , names)

#Now we will create empty set 
s = set() 

#Now we will add the elements to the set defined above 
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)


#Now we will remove the element from the set by using .remove() Built in function 
s.remove(3) 

# Now we will find the length of set using len() function
print(f"Length of the given set is {len(s)}")


#Now we will see the use of python Dictionaries 
#Defining the Python Dictionary 

Capitals = {"U.S.A" : "Washington DC" , "India" : "Delhi" , "Russia" : "Moscow" , "UK" : "London" , "France" : "Paris" , "Germany" : "Berlin"}

#Now we will add the new value to the Capitols 
Capitals["Australia"] = "Canbera"


#printing out all the keys of dictionary 
print(Capitals.keys())
#printing out all the values of dictionary 
print(Capitals.values())

#looping in the dictionary 

for info in Capitals :
    print(Capitals[info])
