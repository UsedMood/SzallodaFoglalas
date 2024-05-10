from Hotel import HotelRoom
from datetime import date, timedelta
from Foglalas import Reservation

bookings = [
    Reservation(HotelRoom.create_single_room(1), date.today() + timedelta(days=2)),
    Reservation(HotelRoom.create_single_room(5), date.today() + timedelta(days=3)),
    Reservation(HotelRoom.create_double_room(36), date.today() + timedelta(days=4)),
    Reservation(HotelRoom.create_double_room(40), date.today() + timedelta(days=5)),
    Reservation(HotelRoom.create_deluxe_room(50), date.today() + timedelta(days=6)),
    Reservation(HotelRoom.create_deluxe_room(55), date.today() + timedelta(days=7)),
]

def list_available_rooms():
    for room in HotelRoom.create_single_room(35), HotelRoom.create_double_room(49), HotelRoom.create_deluxe_room(55):
        print(f"{room.name} {room.number} ({room.price}): {', '.join(str(x) for x in range(1, 36)) if room.name == 'Single Room' else ', '.join(str(x) for x in range(36, 50)) if room.name == 'Double Room' else ', '.join(str(x) for x in range(50, 56))}")

def book_room():
    print("Choose a room type (1: Single, 2: Double, 3: Deluxe):")
    room_type = int(input())
    if room_type == 1:
        room_numbers = range(1, 36)
        price = "2500 peso"
        size = "35m2"
        amenities = "Safe"
    elif room_type == 2:
        room_numbers = range(36, 50)
        price = "7500 peso"
        size = "45 m2"
        amenities = "Safe, Mini Fridge"
    elif room_type == 3:
        room_numbers = range(50, 56)
        price = "15000 peso"
        size = "100 m2"
        amenities = "Safe, FREE Mini fridge, Free Bar"
    else:
        print("Invalid room type. Please choose a valid room type.")
        return
    print(f"Available {room_type} room numbers: {', '.join(str(x) for x in room_numbers)}")
    room_number = int(input())
    if room_number not in room_numbers:
        print("Invalid room number. Please enter a valid room number.")
        return
    checkin_date = date.fromisoformat(input("Enter check-in date (YYYY-MM-DD): "))
    checkout_date = date.fromisoformat(input("Enter checkout date (YYYY-MM-DD): "))
    for booking in bookings:
        if booking.room.number == room_number and booking.reservation_date == checkin_date:
            print("Room is already booked on this date. Please choose a different date.")
            return
    bookings.append(Reservation(HotelRoom.create_room(room_type, room_number, price, size, amenities), checkin_date))
    print("Room booked successfully.")

def unbook_room():
    room_number = int(input("Enter room number: "))
    checkin_date = date.fromisoformat(input("Enter check-in date (YYYY-MM-DD): "))
    for booking in bookings:
        if booking.room.number == room_number and booking.reservation_date == checkin_date:
            bookings.remove(booking)
            print("Room unbooked successfully")
            return
    else:
        print("Room not found ornot booked on this date")

def list_booked_rooms():
    for booking in bookings:
        print(f"{booking.room.name} {booking.room.number} ({booking.room.price}): {booking.reservation_date} - {booking.reservation_date + timedelta(days=1)}")

while True:
    print("\n1. Book a room")
    print("2. List available rooms")
    print("3. Unbook a room")
    print("4. List booked rooms")
    print("5. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        book_room()
    elif option == 2:
        list_available_rooms()
    elif option == 3:
        unbook_room()
    elif option == 4:
        list_booked_rooms()
    elif option == 5:
        break
    else:
        print("Invalid option")