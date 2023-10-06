class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.passengers = []

    def display_flight_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Available Seats: {self.capacity - len(self.passengers)}")

    def book_seat(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            print(f"Reservation for {passenger_name} on Flight {self.flight_number} confirmed.")
        else:
            print("Sorry, the flight is fully booked.")

class ReservationSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_available_flights(self):
        print("Available Flights:")
        for flight in self.flights:
            flight.display_flight_info()

    def make_reservation(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight.book_seat(passenger_name)
                return
        print(f"Flight {flight_number} not found.")

def main():
    system = ReservationSystem()

    # Sample flights
    flight1 = Flight("F001", "New York", "Los Angeles", "08:00 AM", 100)
    flight2 = Flight("F002", "Chicago", "Miami", "10:30 AM", 120)
    flight3 = Flight("F003", "San Francisco", "Seattle", "12:45 PM", 80)

    system.add_flight(flight1)
    system.add_flight(flight2)
    system.add_flight(flight3)

    while True:
        print("\nFlight Reservation System")
        print("1. Display Available Flights")
        print("2. Make a Reservation")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.display_available_flights()
        elif choice == "2":
            flight_number = input("Enter the flight number: ")
            passenger_name = input("Enter passenger name: ")
            system.make_reservation(flight_number, passenger_name)
        elif choice == "3":
            print("Exiting the Flight Reservation System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
