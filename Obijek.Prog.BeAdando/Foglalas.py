class Reservation:
    def __init__(self, room, reservation_date):
        self.room = room
        self.reservation_date = reservation_date

class HotelRoom:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price
        self.booking_dates = []

    @staticmethod
    def create_room(room_type, room_number):
        if room_type == 1:
            return HotelRoom("Single Room", room_number, 100)
        elif room_type == 2:
            return HotelRoom("Double Room", room_number, 150)
        elif room_type == 3:
            return HotelRoom("Deluxe Room", room_number, 200)
        else:
            raise ValueError("Invalid room type")

    @staticmethod
    def create_single_room(room_number):
        return HotelRoom.create_room(1, room_number)

    @staticmethod
    def create_double_room(room_number):
        return HotelRoom.create_room(2, room_number)

    @staticmethod
    def create_deluxe_room(room_number):
        return HotelRoom.create_room(3, room_number)
