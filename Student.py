# student_class.py

class Student:
    def __init__(self, student_id, name, age, phone, address, grades):
        """
        Adding some Attributes from my side :
            student_id (str): Unique ID for the student.
            name (str): Name of the student.
            age (int): Age of the student.
            phone (str): Phone number of the student.
            address (str): Address of the student.
            grades (list): List of grades for the student.
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.grades = grades

    def display_details(self):
        """
        display student details
        """
        return (f"Student ID: {self.student_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Phone: {self.phone}\n"
                f"Address: {self.address}\n"
                f"Grades: {self.grades}")

    def calculate_average(self):
        """
        Calculates and returns average of the students grades.
        """
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def update_info(self, name=None, age=None, phone=None, address=None, grades=None):
        """
        Updates  students details.
       
            name (str): New name (optional).
            age (int): New age (optional).
            phone (str): New phone number (optional).
            address (str): New address (optional).
            grades (list): New grades (optional).
        """
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address
        if grades is not None:
            self.grades = grades


def main():
    print("Welcome to the Student Management System!")

    # Create a student object with initial details
    student = Student(
        student_id="P123",
        name="Priya Gupta",
        age=20,
        phone="4369043092",
        address="Sun city hotel",
        grades=[85, 90, 78,34]
    )

    while True:
        print("\nChoices:")
        print("1. Display Student Details")
        print("2. Calculate Average Grade")
        print("3. Update Student Information")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("\nStudent Details:")
            print(student.display_details())

        elif choice == 2:
            avg_grade = student.calculate_average()
            print(f"\nAverage Grade: {avg_grade:.2f}")

        elif choice == 3:
            print("\nUpdate Student Information:")
            name = input("Enter new name : ").strip()
            age = input("Enter new age : ").strip()
            phone = input("Enter new phone number : ").strip()
            address = input("Enter new address : ").strip()
            grades = input("Enter new grades with comma-separated list : ").strip()

            # Validate and update the details
            student.update_info(
                name=name if name else None,
                age=int(age) if age.isdigit() else None,
                phone=phone if phone else None,
                address=address if address else None,
                grades=[int(grade.strip()) for grade in grades.split(',')] if grades else None
            )
            print("Student information updated successfully!")

        elif choice == 4:
            print("Thank you for using the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
