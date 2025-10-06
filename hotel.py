import sys

class Room:
    def _init_(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = "Available"  # Available or Occupied
        self.guest = None  # Will store guest name during booking

    def _str_(self):
        return f"Room {self.room_number} ({self.room_type}) - Price: ${self.price} - Status: {self.status} - Guest: {self.guest or 'None'}"

class Guest:
    def _init_(self, name, contact):
        self.name = name
        self.contact = contact

class Booking:
    def _init_(self, guest, room, check_in_date="Today"):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = None  # Set during check-out

class Hotel:
    def _init_(self):
        self.rooms = []
        self.bookings = []  # List of active bookings
        self._initialize_rooms()

    def _initialize_rooms(self):
        # Predefined rooms (you can add more)
        room_types = [
            (101, "Single", 100),
            (102, "Double", 150),
            (103, "Single", 100),
            (104, "Suite", 250),
            (201, "Double", 150),
            (202, "Single", 100),
            (203, "Double", 150),
            (204, "Suite", 250),
            (301, "Single", 100),
            (302, "Double", 150)
        ]
        for room_num, room_type, price in room_types:
            self.rooms.append(Room(room_num, room_type, price))

    def view_all_rooms(self):
        print("\n=== All Rooms ===")
        for room in self.rooms:
            print(room)
        print()

    def view_available_rooms(self):
        print("\n=== Available Rooms ===")
        available = [room for room in self.rooms if room.status == "Available"]
        if not available:
            print("No rooms available!")
        else:
            for room in available:
                print(room)
        print()

    def book_room(self):
        self.view_available_rooms()
        try:
            room_num = int(input("Enter room number to book: "))
            room = next((r for r in self.rooms if r.room_number == room_num), None)
            if not room or room.status != "Available":
                print("Invalid room number or room not available!")
                return

            guest_name = input("Enter guest name: ")
            guest_contact = input("Enter guest contact (phone/email): ")
            guest = Guest(guest_name, guest_contact)

            room.status = "Occupied"
            room.guest = guest_name
            booking = Booking(guest, room)
            self.bookings.append(booking)

            print(f"Room {room_num} booked successfully for {guest_name}!")
        except ValueError:
            print("Invalid input! Please enter a valid room number.")
        print()

    def check_out(self):
        self.view_all_rooms()
        try:
            room_num = int(input("Enter room number to check out: "))
            room = next((r for r in self.rooms if r.room_number == room_num), None)
            if not room or room.status != "Occupied":
                print("Invalid room number or room not occupied!")
                return

            # Find and update booking
            booking = next((b for b in self.bookings if b.room == room), None)
            if booking:
                booking.check_out_date = "Today"  # In real app, use actual date
                self.bookings.remove(booking)  # Remove from active bookings (or mark as completed)

            room.status = "Available"
            room.guest = None
            print(f"Check-out successful for Room {room_num}!")
        except ValueError:
            print("Invalid input! Please enter a valid room number.")
        print()

    def view_bookings(self):
        print("\n=== Active Bookings ===")
        if not self.bookings:
            print("No active bookings!")
        else:
            for booking in self.bookings:
                print(f"Guest: {booking.guest.name} ({booking.guest.contact}) | "
                      f"Room: {booking.room.room_number} | "
                      f"Check-in: {booking.check_in_date} | "
                      f"Check-out: {booking.check_out_date or 'Ongoing'}")
        print()

def main():
    hotel = Hotel()
    print("Welcome to the Hotel Management System!")

    while True:
        print("\n=== Main Menu ===")
        print("1. View All Rooms")
        print("2. View Available Rooms")
        print("3. Book a Room")
        print("4. Check Out")
        print("5. View Active Bookings")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            hotel.view_all_rooms()
        elif choice == '2':
            hotel.view_available_rooms()
        elif choice == '3':
            hotel.book_room()
        elif choice == '4':
            hotel.check_out()
        elif choice == '5':
            hotel.view_bookings()
        elif choice == '6':
            print("Thank you for using the Hotel Management System!")
            sys.exit(0)
        else:
            print("Invalid choice! Please try again.")

if _name_ == "_main_":
    main()
