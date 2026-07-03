import json
FILENAME = "students.json"

def save_data():
    with open(FILENAME, "w") as f:
        json.dump(students, f)

def load_data():
    global students
    try:
        with open(FILENAME, "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = {}

students = {}

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def print_divider():
    print("-" * 45)

def add_student():
    print_divider()
    print("ADD NEW STUDENT")
    print_divider()
    name = input("Enter student name: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return
    if name in students:
        print(f"{name} already exists.")
        return
    courses = ["Programming", "Business law", "Database design", "Accounting", "Computer networks", "Communication skills"]
    marks = []
    print(f"\nEnter marks for {name} (0 - 100):")
    for course in courses:
        while True:
            try:
                mark = float(input(f"{course}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Enter value between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")
    average = calculate_average(marks)
    grade = assign_grade(average)
    students[name] = {"courses": courses, "marks": marks, "average": average, "grade": grade}
    save_data()
    print_divider()
    print(f"{name} added successfully!")
    print(f"Average: {average:.1f} | Grade: {grade}")
    print_divider()
    input("\nPress Enter to return to the menu...")

def view_all_results():
    print_divider()
    print("ALL STUDENT RESULTS")
    print_divider()
    if not students:
        print("No students found.")
        return
    for name, data in students.items():
        print(f"\n{name}")
        for course, mark in zip(data["courses"], data["marks"]):
            print(f"  {course}: {mark:.1f}")
        print(f"  Average: {data['average']:.1f}")
        print(f"  Grade: {data['grade']}")
    print_divider()
    input("\nPress Enter to return to the menu...")

def search_student():
    print_divider()
    print("SEARCH STUDENT")
    print_divider()
    name = input("Enter student name: ").strip().title()
    if name not in students:
        print(f"{name} not found.")
        return
    data = students[name]
    print(f"\nResults for {name}:")
    for course, mark in zip(data["courses"], data["marks"]):
        print(f"  {course}: {mark:.1f}")
    print(f"  Average: {data['average']:.1f}")
    print(f"  Grade: {data['grade']}")
    input("\nPress Enter to return to the menu...")

def show_statistics():
    print_divider()
    print("CLASS STATISTICS")
    print_divider()
    if not students:
        print("No students found.")
        return
    averages = [data["average"] for data in students.values()]
    names = list(students.keys())
    class_average = calculate_average(averages)
    highest = max(averages)
    lowest = min(averages)
    top_student = names[averages.index(highest)]
    lowest_student = names[averages.index(lowest)]
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_average:.1f}")
    print(f"Highest Score: {highest:.1f} ({top_student})")
    print(f"Lowest Score: {lowest:.1f} ({lowest_student})")
    grades = [data["grade"] for data in students.values()]
    print("\nGrade Summary:")
    for grade in ["A+", "A", "B", "C", "D", "F"]:
        count = grades.count(grade)
        if count > 0:
            print(f"  Grade {grade}: {count} student(s)")
    print_divider()
    input("\nPress Enter to return to the menu...")

def delete_student():
    print_divider()
    print("DELETE STUDENT")
    print_divider()
    name = input("Enter student name to delete: ").strip().title()
    if name not in students:
        print(f"{name} not found.")
        return
    confirm = input(f"Delete {name}? (yes/no): ").strip().lower()
    if confirm == "yes":
        del students[name]
        save_data()
        print(f"{name} deleted.")
    else:
        print("Cancelled.")
    input("\nPress Enter to return to Menu...")

def edit_student():
    print_divider()
    print("EDIT STUDENT")
    print_divider()
    name = input("Enter student name to edit: ").strip().title()
    if name not in students:
        print(f"{name} not found.")
        return
    courses = students[name]["courses"]
    new_marks = []
    print(f"\nEnter new marks for {name}:")
    for course in courses:
        while True:
            try:
                mark = float(input(f"{course}: "))
                if 0 <= mark <= 100:
                    new_marks.append(mark)
                    break
                else:
                    print("Enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")
    average = calculate_average(new_marks)
    grade = assign_grade(average)
    students[name]["marks"] = new_marks
    students[name]["average"] = average
    students[name]["grade"] = grade
    save_data()
    print(f"\n{name}'s results have been updated!")
    print(f"New Average: {average:.1f}")
    print(f"New Grade: {grade}")
    input("\nPress Enter to return to the menu...")

def rank_students():
    print_divider()
    print("STUDENT RANKINGS")
    print_divider()
    if not students:
        print("No students found.")
        input("\nPress Enter to return to the menu...")
        return
    sorted_students = sorted(students.items(), key=lambda item: item[1]["average"], reverse=True)
    position = 1
    for name, data in sorted_students:
        print(f"{position}.{name} - {data['average']:.1f} ({data['grade']})")
        position += 1
    print_divider()
    input("\nPress Enter to return to the menu...")

def search_by_grade():
    print_divider()
    print("SEARCH BY GRADE")
    print_divider()
    if not students:
        print("No students found.")
        input("\nPress Enter to return to the menu...")
        return
    grade = input("Enter grade to search (A+, A, B, C, D, F): ").strip().upper()
    if grade not in ["A+", "A", "B", "C", "D", "F"]:
        print("Invalid grade. Enter A+, A, B, C, D or F.")
        input("\nPress Enter to return to the menu...")
        return
    found = False
    for name, data in students.items():
        if data["grade"] == grade:
            print(f"{name} {data['average']:.1f} ({data['grade']})")
            found = True
    if not found:
        print(f"No students found with Grade {grade}.")    
    print_divider()
    input("\nPress Enter to return to the menu...")

def show_menu():
    print("\n" + "=" * 40)
    print("    STUDENT RESULTS SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Results")
    print("3. Search Student")
    print("4. Class Statistics")
    print("5. Delete Student")
    print("6. Edit Student")
    print("7. Student Rankings")
    print("8. Search by Grade")
    print("9. Exit")
    print("=" * 40)

def main():
    load_data()
    print("Welcome to Student Results System!")
    while True:
        show_menu()
        choice = input("Choose (1-6): ").strip()
        print("You entered:", repr(choice))
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_results()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            edit_student()
        elif choice == "7":
            rank_students()
        elif choice == "8":
            search_by_grade()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main() 