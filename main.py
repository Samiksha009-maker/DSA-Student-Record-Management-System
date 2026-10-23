"""DSA Mini Project: Student Record Management System
Uses Python lists, linear search, and bubble sort. No external packages required.
"""

students = []  # Each student is stored as a dictionary inside a list.


def find_student(prn):
    """Linear search: return the student index, or -1 if not found."""
    for index, student in enumerate(students):
        if student["prn"].lower() == prn.lower():
            return index
    return -1


def add_student():
    prn = input("Enter PRN/ID: ").strip()
    if not prn:
        print("PRN cannot be empty.")
        return
    if find_student(prn) != -1:
        print("A student with this PRN already exists.")
        return
    name = input("Enter student name: ").strip()
    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Please enter valid marks between 0 and 100.")
        return
    students.append({"prn": prn, "name": name, "marks": marks})
    print("Student added successfully.")


def display_students(records=None):
    records = students if records is None else records
    if not records:
        print("No student records found.")
        return
    print("\n{:<15} {:<25} {:>8}".format("PRN/ID", "NAME", "MARKS"))
    print("-" * 50)
    for student in records:
        print("{:<15} {:<25} {:>8.2f}".format(
            student["prn"], student["name"][:24], student["marks"]
        ))


def search_student():
    prn = input("Enter PRN/ID to search: ").strip()
    index = find_student(prn)
    if index == -1:
        print("Student not found.")
    else:
        display_students([students[index]])


def update_student():
    prn = input("Enter PRN/ID to update: ").strip()
    index = find_student(prn)
    if index == -1:
        print("Student not found.")
        return
    student = students[index]
    new_name = input(f"New name [{student['name']}]: ").strip()
    if new_name:
        student["name"] = new_name
    new_marks = input(f"New marks [{student['marks']}]: ").strip()
    if new_marks:
        try:
            marks = float(new_marks)
            if not 0 <= marks <= 100:
                raise ValueError
            student["marks"] = marks
        except ValueError:
            print("Invalid marks. Marks were not changed.")
    print("Update completed.")


def delete_student():
    prn = input("Enter PRN/ID to delete: ").strip()
    index = find_student(prn)
    if index == -1:
        print("Student not found.")
        return
    removed = students.pop(index)
    print(f"Deleted record for {removed['name']}.")


def sort_by_marks():
    """Bubble sort: sort records by marks, highest first."""
    sorted_records = students.copy()
    n = len(sorted_records)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_records[j]["marks"] < sorted_records[j + 1]["marks"]:
                sorted_records[j], sorted_records[j + 1] = sorted_records[j + 1], sorted_records[j]
                swapped = True
        if not swapped:
            break
    display_students(sorted_records)


def load_sample_data():
    """Add sample records only when the list is empty."""
    if students:
        print("Sample data can only be loaded when the record list is empty.")
        return
    students.extend([
        {"prn": "DSA101", "name": "Aarav Patil", "marks": 82.0},
        {"prn": "DSA102", "name": "Priya Sharma", "marks": 91.5},
        {"prn": "DSA103", "name": "Rohan Joshi", "marks": 76.0},
    ])
    print("Three sample records added.")


def main():
    while True:
        print("\n=== STUDENT RECORD MANAGEMENT SYSTEM ===")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student by PRN/ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Sort students by marks (highest first)")
        print("7. Load sample data")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1": add_student()
        elif choice == "2": display_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6": sort_by_marks()
        elif choice == "7": load_sample_data()
        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
