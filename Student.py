import os
import time
from termcolor import colored, cprint

class Student:
    def __init__(self):
        self.students = []

    def create_student(self):
        roll = input(colored("Enter Roll Number: ", "green"))
        name = input(colored("Enter Name: ", "green"))
        marks = input(colored("Enter Marks: ", "green"))

        self.students.append({
            "roll": roll,
            "name": name,
            "marks": marks
        })

        cprint("Student added successfully!", "green")
        self.animate("Creating Student")

    def display_students(self):
        if not self.students:
            cprint("No student records found!", "red")
            return

        cprint("\n===== Student Records =====", "cyan")
        for student in self.students:
            print(colored(
                f"Roll No: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}",
                "blue"
            ))

    def update_student(self):
        roll = input(colored("Enter Roll Number to Update: ", "green"))

        for student in self.students:
            if student["roll"] == roll:
                student["name"] = input(colored("Enter New Name: ", "green"))
                student["marks"] = input(colored("Enter New Marks: ", "green"))

                cprint("Student record updated successfully!", "yellow")
                self.animate("Updating Student")
                return

        cprint("Student not found!", "red")

    def delete_student(self):
        roll = input(colored("Enter Roll Number to Delete: ", "green"))

        for student in self.students:
            if student["roll"] == roll:
                self.students.remove(student)

                cprint("Student record deleted successfully!", "blue")
                self.animate("Deleting Student")
                return

        cprint("Student not found!", "red")

    def animate(self, action):
        for _ in range(3):
            print(colored(f"{action}...", "yellow"))
            time.sleep(0.3)
            self.clear_screen()

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


def student_operations():
    adt = Student()

    cprint("Welcome to Student ADT Program", "cyan", attrs=["bold"])

    while True:
        print("\n")
        print(colored("1. Create Student", "yellow"))
        print(colored("2. Display Students", "yellow"))
        print(colored("3. Update Student", "yellow"))
        print(colored("4. Delete Student", "yellow"))
        print(colored("5. Exit", "yellow"))

        try:
            choice = int(input(colored("Enter your choice (1-5): ", "green")))
        except ValueError:
            cprint("Please enter a valid number!", "red")
            continue

        if choice == 1:
            adt.create_student()

        elif choice == 2:
            adt.display_students()

        elif choice == 3:
            adt.update_student()

        elif choice == 4:
            adt.delete_student()

        elif choice == 5:
            cprint("Thank you! Program terminated.", "cyan", attrs=["bold"])
            break

        else:
            cprint("Invalid Choice!", "red")


if __name__ == "__main__":
    student_operations()
