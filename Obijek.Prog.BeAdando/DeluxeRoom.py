from Rooms import Rooms

class DeluxeRoom(Rooms):
    def __init__(self, number, price, size, amenities):
        if not 50 <= number <= 55:
            raise ValueError("Deluxe room number must be between 50 and 55")
        super().__init__("", price, size, 2, "double", "Safe, FREE Mini fridge, Free Bar")
