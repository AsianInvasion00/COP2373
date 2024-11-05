# Tyler Vo
# 11/03/2024

import csv


def get_valid_int(prompt):
    # Get a valid integer input
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid integer.")


def write_student_exam():
    # Prompt for the number of students
    num_students = get_valid_int("Enter the number of students: ")

    # Create and write the CSV header
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Collect and write student data
        for i in range(num_students):
            print(f"Enter data for student {i + 1}:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            exam1 = get_valid_int("Exam 1 grade: ")
            exam2 = get_valid_int("Exam 2 grade: ")
            exam3 = get_valid_int("Exam 3 grade: ")

            # Write the data to the file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"\nGrades saved to grades.csv.\n")


def read_student_exam():
    try:
        with open('grades.csv', 'r') as file:
            reader = csv.reader(file)
            print("\n--- Student Grades ---")

            # Display the table header and rows
            for row in reader:
                print("{:<15} {:<15} {:<7} {:<7} {:<7}".format(*row))
    except FileNotFoundError:
        print("grades.csv not found.")


def main():
    # Write or read depending on the user's input
    while True:
        print("\n1. Enter student grades")
        print("2. Display student grades")
        print("3. Quit")
        choice = input("Type the number to select an input: ")

        if choice == '1':
            write_student_exam()
        elif choice == '2':
            read_student_exam()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


main()
