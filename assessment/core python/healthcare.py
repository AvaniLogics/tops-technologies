class ClinicSystem:
    def __init__(self):
        self.doctors = ["Dr. A", "Dr. B", "Dr. C"]
        self.time_slots = ["10 AM", "11 AM", "12 PM", "2 PM", "3 PM"]
        self.appointments = {}
        for doctor in self.doctors:
            self.appointments[doctor] = {}
            for slot in self.time_slots:
                self.appointments[doctor][slot] = []

        self.patient_lookup = {}

    def book(self, name, age, mobile, doctor, slot):
        if doctor not in self.doctors:
            return " Doctor not available."

        if slot not in self.time_slots:
            return " Invalid slot selected."
        
        if mobile in self.patient_lookup:
            return " Appointment already exists for this mobile."

        if len(self.appointments[doctor][slot]) >= 3:
            return f" Slot {slot} for {doctor} is full (3/3)."

        patient = {"name": name, "age": age, "mobile": mobile}
        self.appointments[doctor][slot].append(patient)
        self.patient_lookup[mobile] = (doctor, slot, patient)

        return f"✅ Appointment confirmed with {doctor} at {slot}."

    def view(self, mobile):
        if mobile not in self.patient_lookup:
            return "No appointment found for this number."

        doctor, slot, patient = self.patient_lookup[mobile]
        return f"Appointment: {patient['name']} ({patient['age']} yrs) with {doctor} at {slot}."

    def cancel(self, mobile):
        if mobile not in self.patient_lookup:
            return "No appointment to cancel for this number."

        doctor, slot, patient = self.patient_lookup[mobile]

        updated_list = []
        for p in self.appointments[doctor][slot]:
            if p["mobile"] != mobile:
                updated_list.append(p)
        self.appointments[doctor][slot] = updated_list
        del self.patient_lookup[mobile]
        return f"Appointment cancelled for {patient['name']}."

    def show_schedule(self, doctor):
        if doctor not in self.doctors:
            return "Doctor not available."

        output = f"\n📅 Schedule for {doctor}\n"
        output += "-" * 25 + "\n"
        for slot in self.time_slots:
            booked = len(self.appointments[doctor][slot])
            output += f"{slot}: {booked}/3 booked\n"
        return output

def main():
    clinic = ClinicSystem()
    while True:
        print("\n===== CLINIC MENU =====")
        print("1. Book Appointment")
        print("2. View Appointment")
        print("3. Cancel Appointment")
        print("4. Show Doctor Schedule")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            print("\n--- Booking Appointment ---")
            name = input("Patient Name: ")
            age = input("Age: ")
            mobile = input("Mobile: ")

            print("Available Doctors:", ", ".join(clinic.doctors))
            doctor = input("Choose Doctor: ")

            print("Time Slots:", ", ".join(clinic.time_slots))
            slot = input("Choose Slot: ")

            print(clinic.book(name, age, mobile, doctor, slot))

        elif choice == "2":
            print("\n--- View Appointment ---")
            mobile = input("Enter Mobile: ")
            print(clinic.view(mobile))

        elif choice == "3":
            print("\n--- Cancel Appointment ---")
            mobile = input("Enter Mobile: ")
            print(clinic.cancel(mobile))

        elif choice == "4":
            print("\n--- Doctor Schedule ---")
            doctor = input("Enter Doctor Name: ")
            print(clinic.show_schedule(doctor))

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()

