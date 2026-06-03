# Attendance Management System

A simple Python-based Attendance Management System that allows users to manage student records, mark attendance, and generate attendance reports using CSV files and Pandas.

## Features

* Add new students
* View all students
* Mark attendance (Present/Absent)
* Generate attendance reports
* Search for a student by Roll Number
* Delete student records
* Automatic attendance percentage calculation
* Attendance shortage alerts for students below 75%

## Technologies Used

* Python 3
* Pandas
* CSV Files

## Project Structure

```
Attendance-Management-System/
│
├── main.py
├── students.csv
├── attendance.csv
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Attendance-Management-System
```

### 2. Install Dependencies

```bash
pip install pandas
```

### 3. Run the Project

```bash
python main.py
```

## Menu Options

```
1. Add Student
2. View Students
3. Mark Attendance
4. Generate Report
5. Search Student
6. Delete Student
7. Exit
```

## Sample Student Data

```
RollNo,Name
101,Aarav Sharma
102,Ananya Reddy
103,Rahul Verma
...
```

## Sample Attendance Report

```
===== ATTENDANCE REPORT =====

Aarav Sharma (101) : 80.00%
Ananya Reddy (102) : 75.00%
Rahul Verma (103) : 60.00% ⚠ SHORTAGE
```

## Learning Outcomes

This project helped practice:

* Python Functions
* File Handling
* CSV Operations
* Pandas DataFrames
* Data Filtering and Analysis
* CRUD Operations
* Report Generation

## Future Enhancements

* Tkinter GUI Version
* Subject-wise Attendance Tracking
* Excel Report Export
* Student Login System
* Flask Web Application
* Database Integration (MySQL/SQLite)

## Author

Vijaya Sankari Kuppa

B.Tech Computer Science
