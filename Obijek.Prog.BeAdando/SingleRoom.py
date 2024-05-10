from Rooms import Rooms

class SingleRoom(Rooms):
    def __init__(self, number, price, size, amenities):
        if not 1 <= number <= 35:
            raise ValueError("Single room number must be between 1 and 35")
        super().__init__("", "2500 peso", size, 1, "King Size", "Safe")
