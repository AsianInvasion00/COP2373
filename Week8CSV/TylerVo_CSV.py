# Tyler Vo
# 11/03/2024

import csv


def write_student_exam():

    # Prompt for the number of students
    num_students = int(input("Enter the number of students: "))

    # Create and write the CSV header
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Table header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Collect and write student data
        for i in range(num_students):
            print(f"Enter data for student {i + 1}:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

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
        print(f"grades.csv not found.")


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