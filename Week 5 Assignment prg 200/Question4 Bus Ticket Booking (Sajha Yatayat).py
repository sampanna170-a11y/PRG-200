class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = {}

    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked_seats:
            print("Seat already booked")
        elif seat_number > self.total_seats or seat_number < 1:
            print("Invalid seat number")
        else:
            self.booked_seats[seat_number] = passenger_name
            print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked_seats)

    def passenger_list(self):
        print("\nPassenger List:")
        for seat, passenger in sorted(self.booked_seats.items()):
            print(f"Seat {seat}: {passenger}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang")
]

for seat, passenger in bookings:
    bus.book_seat(seat, passenger)

print(f"\nAvailable Seats: {bus.available_seats()}")

bus.passenger_list()
