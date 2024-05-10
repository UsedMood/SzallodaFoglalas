from Rooms import Rooms

class DoubleRoom(Rooms):
    def __init__(self, number, price, size, amenities):
        if not 36 <= number <= 49:
            raise ValueError("Double room number must be between 36 and 49")
        super().__init__("", "7500 peso", size, 2, "double", "Safe, Mini Fridge")