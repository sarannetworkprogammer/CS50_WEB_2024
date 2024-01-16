class Flight():

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []


    def add_passengers(self,name):

        if self.open_seats() <= 0:
            return False
        self.passengers.append(name)

        return True
    
    def open_seats(self):

        return self.capacity -len(self.passengers)
    

# creating a flight capacity of 3
flight = Flight(3)



people = ["harry","Ron", "Hermione", "Ginny"]


for person in people:
    if flight.add_passengers(person):
        print(f"added {person} to filght sucessfully")


    else:
        print(f" No available seats for {person}")