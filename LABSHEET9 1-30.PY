# # Q1: Create a list of student records
# students = [
#     {"roll": 1, "name": "Aman", "marks": 85},
#     {"roll": 2, "name": "Riya", "marks": 92}
# ]
# print("Student records created")

# # Q2: Display all student records
# students = [
#     {"roll": 1, "name": "Aman", "marks": 85},
#     {"roll": 2, "name": "Riya", "marks": 92}
# ]
# for student in students:
#     print(student)

# # Q3: Search for a student by name
# students = [{"roll": 1, "name": "Aman", "marks": 85},
#             {"roll": 2, "name": "Riya", "marks": 92}]
# name = input("Enter name: ").strip().lower()
# for student in students:
#     if student["name"].lower() == name:
#         print(student)
#         break
# else:
#     print("Student not found")

# # Q4: Update a student's marks
# students = [{"roll": 1, "name": "Aman", "marks": 85},
#             {"roll": 2, "name": "Riya", "marks": 92}]
# roll = int(input("Enter roll number: "))
# for student in students:
#     if student["roll"] == roll:
#         student["marks"] = float(input("Enter new marks: "))
#         print("Marks updated:", student)
#         break
# else:
#     print("Student not found")

# # Q5: Delete a student by roll number
# students = [{"roll": 1, "name": "Aman", "marks": 85},
#             {"roll": 2, "name": "Riya", "marks": 92}]
# roll = int(input("Enter roll number: "))
# students = [s for s in students if s["roll"] != roll]
# print(students)

# # Q6: CRUD operations on an employee dictionary
# employees = {1: {"name": "Aman", "salary": 25000}}

# # Create
# employees[2] = {"name": "Riya", "salary": 30000}
# # Read
# print(employees)
# # Update
# employees[1]["salary"] = 28000
# # Delete
# employees.pop(2, None)
# print("Final data:", employees)

# # Q7: Menu-driven CRUD operations on a list of books
# books = []
# while True:
#     print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
#     choice = input("Choice: ")
#     if choice == "1":
#         books.append({"id": input("Book ID: "), "title": input("Title: ")})
#     elif choice == "2":
#         print(books)
#     elif choice == "3":
#         bid = input("Book ID to update: ")
#         for book in books:
#             if book["id"] == bid:
#                 book["title"] = input("New title: ")
#                 break
#     elif choice == "4":
#         bid = input("Book ID to delete: ")
#         books = [b for b in books if b["id"] != bid]
#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice")

# # Q8: CRUD operations for product details
# products = {}
# # Create
# products[101] = {"name": "Pen", "price": 10}
# # Read
# print(products)
# # Update
# products[101]["price"] = 12
# # Delete
# products.pop(101, None)
# print("Final products:", products)

# # Q9: Save student data to a text file and read it back
# students = ["1,Aman,85", "2,Riya,92"]
# with open("students.txt", "w") as f:
#     f.write("\n".join(students))
# with open("students.txt", "r") as f:
#     print(f.read())

# # Q10: File-based CRUD: add, view, modify, delete student records
# FILE = "students.txt"

# def read_records():
#     try:
#         with open(FILE, "r") as f:
#             return [line.strip().split(",") for line in f if line.strip()]
#     except FileNotFoundError:
#         return []

# def save_records(records):
#     with open(FILE, "w") as f:
#         for record in records:
#             f.write(",".join(record) + "\n")

# # Add
# records = read_records()
# records.append(["1", "Aman", "85"])
# save_records(records)
# # View
# print(read_records())
# # Modify marks for roll number 1
# records = read_records()
# for record in records:
#     if record[0] == "1":
#         record[2] = "90"
# save_records(records)
# # Delete roll number 1
# records = [r for r in read_records() if r[0] != "1"]
# save_records(records)
# print("File CRUD completed")

# # Q11: Connect to SQLite and create students table
# import sqlite3
# with sqlite3.connect("college.db") as con:
#     con.execute("""CREATE TABLE IF NOT EXISTS students
#                    (roll INTEGER PRIMARY KEY, name TEXT, marks REAL)""")
# print("Connected; table ready")

# # Q12: Insert a new student record
# import sqlite3
# with sqlite3.connect("college.db") as con:
#     con.execute("INSERT INTO students (roll, name, marks) VALUES (?, ?, ?)",
#                 (1, "Aman", 85))
# print("Record inserted")

# # Q13: Display all student records
# import sqlite3
# with sqlite3.connect("college.db") as con:
#     for row in con.execute("SELECT * FROM students"):
#         print(row)

# # Q14: Search for a student by roll number
# import sqlite3
# roll = int(input("Enter roll number: "))
# with sqlite3.connect("college.db") as con:
#     row = con.execute("SELECT * FROM students WHERE roll=?", (roll,)).fetchone()
#     print(row if row else "Student not found")

# # Q15: Update student marks using roll number
# import sqlite3
# roll = int(input("Enter roll number: "))
# marks = float(input("Enter new marks: "))
# with sqlite3.connect("college.db") as con:
#     con.execute("UPDATE students SET marks=? WHERE roll=?", (marks, roll))
# print("Marks updated if roll number exists")

# # Q16: Delete a student by roll number
# import sqlite3
# roll = int(input("Enter roll number: "))
# with sqlite3.connect("college.db") as con:
#     con.execute("DELETE FROM students WHERE roll=?", (roll,))
# print("Record deleted if roll number exists")

# # Q17: Count total records in the table
# import sqlite3
# with sqlite3.connect("college.db") as con:
#     total = con.execute("SELECT COUNT(*) FROM students").fetchone()[0]
# print("Total records:", total)

# # Q18: Display records sorted by student name
# import sqlite3
# with sqlite3.connect("college.db") as con:
#     for row in con.execute("SELECT * FROM students ORDER BY name ASC"):
#         print(row)

# # Q19: Find the student with the highest marks
# import sqlite3
# with sqlite3.connect("college.db") as con:
#     row = con.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 1").fetchone()
# print(row if row else "No student records found")

# # Q20: Menu-driven student CRUD application using SQLite
import sqlite3

con = sqlite3.connect("college.db")
con.execute("""CREATE TABLE IF NOT EXISTS students
               (roll INTEGER PRIMARY KEY, name TEXT, marks REAL)""")

while True:
    print("\n1.Add  2.View  3.Update  4.Delete  5.Exit")
    choice = input("Choice: ")
    if choice == "1":
        roll = int(input("Roll: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        try:
            con.execute("INSERT INTO students VALUES (?, ?, ?)", (roll, name, marks))
            con.commit()
            print("Student added")
        except sqlite3.Error as e:
            print("Database error:", e)
    elif choice == "2":
        for row in con.execute("SELECT * FROM students"):
            print(row)
    elif choice == "3":
        roll = int(input("Roll to update: "))
        marks = float(input("New marks: "))
        con.execute("UPDATE students SET marks=? WHERE roll=?", (marks, roll))
        con.commit()
        print("Student updated if roll exists")
    elif choice == "4":
        roll = int(input("Roll to delete: "))
        con.execute("DELETE FROM students WHERE roll=?", (roll,))
        con.commit()
        print("Student deleted if roll exists")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
con.close()