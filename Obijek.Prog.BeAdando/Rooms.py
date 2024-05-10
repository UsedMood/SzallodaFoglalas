from abc import ABC, abstractmethod
from datetime import date


class Rooms(ABC):
    def __init__(self, number, price, size, capacity, bed_type, amenities):
        self.number = number
        self.price = price
        self.size = size
        self.capacity = capacity
        self.bed_type = bed_type
        self.amenities = amenities
        self.is_booked = False
        self.booking_dates = []

    @abstractmethod
    def book_room(self, booking_date: date):
        pass

    @abstractmethod
    def unbook_room(self, unbooking_date: date):
        pass

    def get_booking_dates(self):
        return self.booking_dates

    def is_available(self, date: date):
        return date not in self.booking_dates

    def get_price_per_night(self):
        return self.price

    def get_price_for_stay(self, start_date: date, end_date: date):
        nights = (end_date - start_date).days
        return nights * self.price

