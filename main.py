import pandas as pd
from datetime import date
import os

# ==========================================
# Create CSV files if they don't exist
# ==========================================

if not os.path.exists("students.csv"):
    pd.DataFrame(columns=["RollNo", "Name"]).to_csv(
        "students.csv",
        index=False
    )

if not os.path.exists("attendance.csv"):
    pd.DataFrame(columns=["Date", "RollNo", "Status"]).to_csv(
        "attendance.csv",
        index=False
    )


# ==========================================
# Safe CSV Reading
# ==========================================

def load_students():

    import os

    print("Reading from:",
          os.path.abspath("students.csv"))

    try:
        return pd.read_csv("students.csv")
    except Exception as e:
        print(e)
        return pd.DataFrame(
            columns=["RollNo", "Name"]
        )


def load_attendance():
    try:
        return pd.read_csv("attendance.csv")
    except:
        return pd.DataFrame(columns=["Date", "RollNo", "Status"])


# ==========================================
# Add Student
# ==========================================

def add_student():

    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()

    students = load_students()

    if roll in students["RollNo"].astype(str).values:
        print("Student already exists!")
        return

    new_student = pd.DataFrame({
        "RollNo": [roll],
        "Name": [name]
    })

    students = pd.concat(
        [students, new_student],
        ignore_index=True
    )

    students.to_csv(
        "students.csv",
        index=False
    )

    print("Student added successfully!")


# ==========================================
# View Students
# ==========================================

def view_students():

    students = load_students()

    print("\nRows:", len(students))
    print(students)

# ==========================================
# Mark Attendance
# ==========================================

def mark_attendance():

    students = load_students()

    if students.empty:
        print("No students available.")
        return

    today = str(date.today())

    attendance = load_attendance()

    print(f"\nAttendance for {today}")

    attendance_data = []

    for _, student in students.iterrows():

        while True:

            status = input(
                f"{student['Name']} (P/A): "
            ).upper()

            if status in ["P", "A"]:
                break

            print("Please enter only P or A.")

        attendance_data.append({
            "Date": today,
            "RollNo": student["RollNo"],
            "Status": status
        })

    attendance = pd.concat(
        [attendance, pd.DataFrame(attendance_data)],
        ignore_index=True
    )

    attendance.to_csv(
        "attendance.csv",
        index=False
    )

    print("\nAttendance recorded successfully!")


# ==========================================
# Generate Attendance Report
# ==========================================

def generate_report():

    students = load_students()
    attendance = load_attendance()

    if students.empty:
        print("No students found.")
        return

    if attendance.empty:
        print("No attendance records found.")
        return

    print("\n===== ATTENDANCE REPORT =====\n")

    for _, student in students.iterrows():

        roll = student["RollNo"]

        records = attendance[
            attendance["RollNo"].astype(str)
            == str(roll)
        ]

        total_classes = len(records)

        if total_classes == 0:
            percentage = 0
        else:
            present_classes = len(
                records[
                    records["Status"] == "P"
                ]
            )

            percentage = (
                present_classes /
                total_classes
            ) * 100

        if percentage < 75:

            print(
                f"{student['Name']} "
                f"({roll}) : "
                f"{percentage:.2f}% "
                f"⚠ SHORTAGE"
            )

        else:

            print(
                f"{student['Name']} "
                f"({roll}) : "
                f"{percentage:.2f}%"
            )


# ==========================================
# Search Student
# ==========================================

def search_student():

    roll = input(
        "Enter Roll Number: "
    ).strip()

    students = load_students()

    result = students[
        students["RollNo"].astype(str)
        == roll
    ]

    if result.empty:
        print("Student not found.")
    else:
        print("\nStudent Found:")
        print(result.to_string(index=False))


# ==========================================
# Delete Student
# ==========================================

def delete_student():

    roll = input(
        "Enter Roll Number to delete: "
    ).strip()

    students = load_students()

    before = len(students)

    students = students[
        students["RollNo"].astype(str)
        != roll
    ]

    after = len(students)

    if before == after:
        print("Student not found.")
        return

    students.to_csv(
        "students.csv",
        index=False
    )

    print("Student deleted successfully.")


# ==========================================
# Menu
# ==========================================

def menu():

    print("\n")
    print("=" * 40)
    print("ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Generate Report")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Exit")


# ==========================================
# Main Program
# ==========================================

while True:

    menu()

    choice = input(
        "\nEnter your choice: "
    )

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        generate_report()

    elif choice == "5":
        search_student()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
