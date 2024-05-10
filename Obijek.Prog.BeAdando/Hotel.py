from datetime import date

class HotelRoom:
    def __init__(self, name, number, price, size, amenities):
        self.name = name
        self.number = number
        self.price = price
        self.size = size
        self.amenities = amenities
        self.booking_dates = []

    @staticmethod
    def create_room(room_type, room_number, price, size, amenities):
        if room_type == 1:
            return HotelRoom("Single Room", room_number, price, size, amenities)
        elif room_type == 2:
            return HotelRoom("Double Room", room_number, price, size, amenities)
        elif room_type == 3:
            return HotelRoom("Deluxe Room", room_number, price, size, amenities)
        else:
            raise ValueError("Invalid room type")

    @staticmethod
    def create_single_room(room_number):
        return HotelRoom.create_room(1, room_number, "2500 peso", "35m2", "Safe")

    @staticmethod
    def create_double_room(room_number):
        return HotelRoom.create_room(2, room_number, "7500 peso", "45 m2", "Safe, Mini Fridge")

    @staticmethod
    def create_deluxe_room(room_number):
        return HotelRoom.create_room(3, room_number, "15000 peso", "100 m2", "Safe, FREE Mini fridge, Free Bar")