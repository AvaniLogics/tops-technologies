class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai-Pune": 500,
            "Delhi-Jaipur": 600,
            "Bangalore-Mysore": 450,
            "Ahmedabad-Surat": 350
        }
        self.tickets = {}
        self.seats_booked = {route: [] for route in self.routes}
        self.max_seats = 40
        self.next_ticket = 1

    def show_routes(self):
        print("\nAvailable Routes & Prices:")
        for r, p in self.routes.items():
            print(f"  {r} - ₹{p}")

    def book_ticket(self, name, age, mobile, route):
        if route not in self.routes:
            return "Invalid route."
        if len(self.seats_booked[route]) >= self.max_seats:
            return "All seats are booked for this route."
        seat_no = len(self.seats_booked[route]) + 1
        ticket_id = str(self.next_ticket).zfill(4)
        self.next_ticket += 1
        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_no,
            "price": self.routes[route]
        }
        self.seats_booked[route].append(seat_no)
        return f"Ticket booked. ID: {ticket_id}, Seat: {seat_no}, Fare: ₹{self.routes[route]}"

    def view_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            return "No ticket found."
        t = self.tickets[ticket_id]
        return (f"Ticket ID: {ticket_id}\n"
                f"Name: {t['name']} ({t['age']} yrs)\n"
                f"Mobile: {t['mobile']}\n"
                f"Route: {t['route']}\n"
                f"Seat: {t['seat']}\n"
                f"Fare: ₹{t['price']}")

    def cancel_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            return "No ticket found."
        t = self.tickets.pop(ticket_id)
        r = t["route"]
        s = t["seat"]
        self.seats_booked[r] = [x for x in self.seats_booked[r] if x != s]
        return f"Ticket {ticket_id} for {t['name']} cancelled."

def main():
    bus = BusReservation()
    while True:
        print("\n==== BUS RESERVATION MENU ====")
        print("1. Show Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            bus.show_routes()
        elif choice == "2":
            print("\n--- Book Ticket ---")
            name = input("Name: ")
            age = input("Age: ")
            mobile = input("Mobile: ")
            bus.show_routes()
            route = input("Enter Route (exact as shown): ")
            print(bus.book_ticket(name, age, mobile, route))
        elif choice == "3":
            tid = input("Enter Ticket ID: ")
            print(bus.view_ticket(tid))
        elif choice == "4":
            tid = input("Enter Ticket ID: ")
            print(bus.cancel_ticket(tid))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
