class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []  # Composition: House has Rooms

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        print(f"House at {self.address} has rooms:")
        for room in self.rooms:
            print(f"Room: {room.name}")

# Create instances of Room
room1 = Room("Living Room")
room2 = Room("Bedroom")

# Create an instance of House
house = House("123 Street Name")

# Add rooms to the house
house.add_room(room1)
house.add_room(room2)

# Demonstrate composition
house.show_rooms()
