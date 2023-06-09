#In this python file we will create python algorithm to give out no. of passengers can be added 


#Main code begins 
#defining class 

class Flight():
    def __init__(self , capacity) :
        self.capacity = capacity 
        self.passengers = [] 

    def add_passenger(self , name) :
        if not self.open_seats() :
            return False
        self.passengers.append(name)
        return True

    def open_seats(self) :
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["Harry" , "Rone" , "Tyrone" , "Jack"]
for person in people :
    success = flight.add_passenger(person)
    if success :
        print(f"Added {person} to the flight Successfully!")
    else :
        print(F"No seats are available for the {person}")