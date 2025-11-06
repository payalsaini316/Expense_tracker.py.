# ------------------------------------------------------------
# Student Marks Analyzer
# Author: Payal Saini
# Date: November 2025
# Course: Foundations of Programming using Python (ETCCPP103)
# ------------------------------------------------------------

import csv

def display_menu():
    print("\n====== STUDENT MARKS ANALYZER ======")
    print("1. Enter student marks manually")
    print("2. Read marks from CSV file")
    print("3. View statistical analysis")
    print("4. View grades for all students")
    print("5. View pass/fail summary")
    print("6. Export results to CSV")
    print("7. Exit")
    print("====================================")

# Global dictionary to store student data
students = {}

# ------------------ Task 2: Data Entry ------------------
def enter_marks_manually():
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks of {name}: "))
        students[name] = marks
    print("\n✅ Marks entered successfully!")

def read_marks_from_csv():
    filename = input("Enter CSV filename (with .csv extension): ")
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header if present
            for row in reader:
                if len(row) >= 2:
                    name, marks = row[0], float(row[1])
                    students[name] = marks
        print("\n✅ Marks loaded successfully from CSV!")
    except FileNotFoundError:
        print("❌ File not found! Please check the filename and try again.")

# ------------------ Task 3: Statistical Analysis ------------------
def show_statistics():
    if not students:
        print("⚠️ No data available! Please enter or load marks first.")
        return

    marks_list = list(students.values())
    top_score = max(marks_list)
    avg_score = sum(marks_list) / len(marks_list)
    pass_count = len([m for m in marks_list if m >= 40])
    fail_count = len(marks_list) - pass_count

    print("\n📊 STATISTICAL ANALYSIS")
    print("----------------------------")
    print(f"Top Score: {top_score}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Pass Count: {pass_count}")
    print(f"Fail Count: {fail_count}")

# ------------------ Task 4: Grade Assignment ------------------
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def show_grades():
    if not students:
        print("⚠️ No data available!")
        return

    print("\n🎓 STUDENT GRADES")
    print("Name\t\tMarks\tGrade")
    print("-" * 30)
    for name, marks in students.items():
        print(f"{name}\t\t{marks}\t{assign_grade(marks)}")

# ------------------ Task 5: Pass/Fail Summary ------------------
def show_pass_fail_summary():
    if not students:
        print("⚠️ No data available!")
        return

    passed = [name for name, marks in students.items() if marks >= 40]
    failed = [name for name, marks in students.items() if marks < 40]

    print("\n✅ Passed Students:")
    print(", ".join(passed) if passed else "None")

    print("\n❌ Failed Students:")
    print(", ".join(failed) if failed else "None")

# ------------------ Bonus: Export Results ------------------
def export_to_csv():
    if not students:
        print("⚠️ No data to export!")
        return

    with open("results.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for name, marks in students.items():
            writer.writerow([name, marks, assign_grade(marks)])
    print("\n💾 Results exported successfully to results.csv")

# ------------------ Task 6: Loop Menu ------------------
while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        enter_marks_manually()
    elif choice == "2":
        read_marks_from_csv()
    elif choice == "3":
        show_statistics()
    elif choice == "4":
        show_grades()
    elif choice == "5":
        show_pass_fail_summary()
    elif choice == "6":
        export_to_csv()
    elif choice == "7":
        print("👋 Exiting the program. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please select a valid option.")
