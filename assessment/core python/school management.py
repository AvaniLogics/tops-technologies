class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def new_admission(self, name, age, student_class, mobile):
        if not (5 <= age <= 18):
            return "Age must be between 5 and 18."
        if len(mobile) != 10 or not mobile.isdigit():
            return "Mobile number must be 10 digits."
        if not (1 <= student_class <= 12):
            return "Class must be between 1 and 12."
        student_id = str(self.next_id).zfill(4)   # 0001, 0002, ...
        self.next_id += 1
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }
        return f"Admission successful. Student ID: {student_id}"

    def view_student(self, student_id):
        if student_id not in self.students:
            return "No record found."
        s = self.students[student_id]
        return (f"ID: {student_id}\n"
                f"Name: {s['name']}\n"
                f"Age: {s['age']}\n"
                f"Class: {s['class']}\n"
                f"Mobile: {s['mobile']}")

    def update_student(self, student_id, new_mobile=None, new_class=None):
        if student_id not in self.students:
            return "No record found."
        if new_mobile:
            if len(new_mobile) != 10 or not new_mobile.isdigit():
                return "Mobile number must be 10 digits."
            self.students[student_id]["mobile"] = new_mobile
        if new_class:
            if not (1 <= new_class <= 12):
                return "Class must be between 1 and 12."
            self.students[student_id]["class"] = new_class
        return "Student info updated."

    def remove_student(self, student_id):
        if student_id not in self.students:
            return "No record found."
        self.students.pop(student_id)
        return "Student record removed."

def main():
    sm = SchoolManagement()
    while True:
        print("\n==== SCHOOL MANAGEMENT MENU ====")
        print("1. New Admission")
        print("2. View Student")
        print("3. Update Student Info")
        print("4. Remove Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            name = input("Student Name: ")
            age = int(input("Age: "))
            student_class = int(input("Class (1-12): "))
            mobile = input("Guardian Mobile (10 digits): ")
            print(sm.new_admission(name, age, student_class, mobile))
        elif choice == "2":
            student_id = input("Enter Student ID: ")
            print(sm.view_student(student_id))
        elif choice == "3":
            student_id = input("Enter Student ID: ")
            new_mobile = input("New Mobile (or press Enter to skip): ").strip()
            new_mobile = new_mobile if new_mobile else None
            new_class = input("New Class (or press Enter to skip): ").strip()
            new_class = int(new_class) if new_class else None
            print(sm.update_student(student_id, new_mobile, new_class))
        elif choice == "4":
            student_id = input("Enter Student ID: ")
            print(sm.remove_student(student_id))
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
