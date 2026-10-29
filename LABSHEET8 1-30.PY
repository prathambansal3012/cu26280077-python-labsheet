# # Q1: Connect to SQLite database
# import sqlite3
# con = sqlite3.connect("college.db")
# print("Database connected successfully")
# con.close()

# # Q2: Create a new SQLite database
# import sqlite3
# con = sqlite3.connect("college.db")  # Creates database if absent
# print("Database created")
# con.close()

# # Q3: Create students table
# import sqlite3
# con = sqlite3.connect("college.db")
# con.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks REAL)")
# con.commit()
# print("Table created")
# con.close()

# # Q4: Describe students table structure
# import sqlite3
# con = sqlite3.connect("college.db")
# for column in con.execute("PRAGMA table_info(students)"):
#     print(column)
# con.close()

# # Q5: List all database tables
# import sqlite3
# con = sqlite3.connect("college.db")
# for table in con.execute("SELECT name FROM sqlite_master WHERE type='table'"):
#     print(table[0])
# con.close()

# # Q6: Drop students table (run only when needed)
# import sqlite3
# con = sqlite3.connect("college.db")
# con.execute("DROP TABLE IF EXISTS students")
# con.commit()
# print("Table deleted")
# con.close()

# # Q7: Check whether students table exists
# import sqlite3
# con = sqlite3.connect("college.db")
# row = con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ("students",)).fetchone()
# print("Table exists" if row else "Table not found")
# con.close()

# # Q8: Insert a single student record
# import sqlite3
# con = sqlite3.connect("college.db")
# con.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (1, "Aman", 20, 85))
# con.commit()
# print("Record inserted")
# con.close()

# # Q9: Insert multiple student records
# import sqlite3
# con = sqlite3.connect("college.db")
# records = [(2, "Riya", 21, 92), (3, "Karan", 20, 75), (4, "Neha", 22, 35)]
# con.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", records)
# con.commit()
# print("Records inserted")
# con.close()

# # Q10: Display all student records
# import sqlite3
# con = sqlite3.connect("college.db")
# for row in con.execute("SELECT * FROM students"):
#     print(row)
# con.close()

# # Q11: Display name and marks only
# import sqlite3
# con = sqlite3.connect("college.db")
# for row in con.execute("SELECT name, marks FROM students"):
#     print(row)
# con.close()

# # Q12: Display students with marks greater than 80
# import sqlite3
# con = sqlite3.connect("college.db")
# for row in con.execute("SELECT * FROM students WHERE marks > ?", (80,)):
#     print(row)
# con.close()

# # Q13: Sort students by marks descending
# import sqlite3
# con = sqlite3.connect("college.db")
# for row in con.execute("SELECT * FROM students ORDER BY marks DESC"):
#     print(row)
# con.close()

# # Q14: Count total student records
# import sqlite3
# con = sqlite3.connect("college.db")
# count = con.execute("SELECT COUNT(*) FROM students").fetchone()[0]
# print("Total students:", count)
# con.close()

# # Q15: Display top 3 highest-scoring students
# import sqlite3
# con = sqlite3.connect("college.db")
# for row in con.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3"):
#     print(row)
# con.close()

# # Q16: Update marks using student ID
# import sqlite3
# con = sqlite3.connect("college.db")
# sid = int(input("Student ID: "))
# marks = float(input("New marks: "))
# con.execute("UPDATE students SET marks=? WHERE id=?", (marks, sid))
# con.commit()
# print("Marks updated")
# con.close()

# # Q17: Update student name
# import sqlite3
# con = sqlite3.connect("college.db")
# sid = int(input("Student ID: "))
# name = input("New name: ")
# con.execute("UPDATE students SET name=? WHERE id=?", (name, sid))
# con.commit()
# print("Name updated")
# con.close()

# # Q18: Delete student by ID
# import sqlite3
# con = sqlite3.connect("college.db")
# sid = int(input("Student ID: "))
# con.execute("DELETE FROM students WHERE id=?", (sid,))
# con.commit()
# print("Record deleted")
# con.close()

# # Q19: Delete students with marks below 40
# import sqlite3
# con = sqlite3.connect("college.db")
# con.execute("DELETE FROM students WHERE marks < 40")
# con.commit()
# print("Low-scoring records deleted")
# con.close()

# # Q20: Empty table while keeping its structure
# import sqlite3
# con = sqlite3.connect("college.db")
# con.execute("DELETE FROM students")  # SQLite has no TRUNCATE TABLE
# con.commit()
# print("All records deleted; table retained")
# con.close()

# # Q21: Create courses table and insert data
# import sqlite3
# con = sqlite3.connect("college.db")
# con.execute("CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, student_id INTEGER, course_name TEXT)")
# con.executemany("INSERT OR REPLACE INTO courses VALUES (?, ?, ?)",
#                 [(1, 1, "Python"), (2, 2, "DBMS"), (3, 3, "AI")])
# con.commit()
# print("Courses saved")
# con.close()

# # Q22: INNER JOIN students and courses
# import sqlite3
# con = sqlite3.connect("college.db")
# sql = """SELECT s.name, c.course_name FROM students s
#          INNER JOIN courses c ON s.id = c.student_id"""
# for row in con.execute(sql):
#     print(row)
# con.close()

# # Q23: LEFT JOIN students and courses
# import sqlite3
# con = sqlite3.connect("college.db")
# sql = """SELECT s.name, c.course_name FROM students s
#          LEFT JOIN courses c ON s.id = c.student_id"""
# for row in con.execute(sql):
#     print(row)
# con.close()

# # Q24: Calculate average student marks
# import sqlite3
# con = sqlite3.connect("college.db")
# avg = con.execute("SELECT AVG(marks) FROM students").fetchone()[0]
# print("Average marks:", avg if avg is not None else "No records")
# con.close()

# # Q25: Group students by age and count them
# import sqlite3
# con = sqlite3.connect("college.db")
# for row in con.execute("SELECT age, COUNT(*) FROM students GROUP BY age"):
#     print("Age:", row[0], "Count:", row[1])
# con.close()

# # Q26: Export student records to CSV
# import sqlite3
# import csv
# con = sqlite3.connect("college.db")
# rows = con.execute("SELECT id, name, age, marks FROM students").fetchall()
# with open("students.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["id", "name", "age", "marks"])
#     writer.writerows(rows)
# print("CSV exported")
# con.close()

# # Q27: Import student records from CSV
# import sqlite3
# import csv
# con = sqlite3.connect("college.db")
# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)
#     records = [(int(r["id"]), r["name"], int(r["age"]), float(r["marks"])) for r in reader]
# con.executemany("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", records)
# con.commit()
# print("CSV imported")
# con.close()

# # Q28: Handle and display database errors
# import sqlite3
# try:
#     con = sqlite3.connect("college.db")
#     con.execute("SELECT * FROM unknown_table")
# except sqlite3.Error as error:
#     print("Database error:", error)
# finally:
#     if "con" in locals():
#         con.close()

# # Q29: Use functions to insert and fetch students
# import sqlite3

# def add_student(sid, name, age, marks):
#     with sqlite3.connect("college.db") as con:
#         con.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
#                     (sid, name, age, marks))

# def show_students():
#     with sqlite3.connect("college.db") as con:
#         for row in con.execute("SELECT * FROM students"):
#             print(row)

# add_student(5, "Pooja", 21, 88)
# show_students()

# # Q30: Menu-driven student management application
# import sqlite3

# con = sqlite3.connect("college.db")
# con.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks REAL)")
# while True:
#     print("\n1.Add  2.View  3.Update  4.Delete  5.Exit")
#     choice = input("Choice: ")
#     if choice == "1":
#         sid = int(input("ID: "))
#         name = input("Name: ")
#         age = int(input("Age: "))
#         marks = float(input("Marks: "))
#         con.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (sid, name, age, marks))
#         con.commit()
#     elif choice == "2":
#         for row in con.execute("SELECT * FROM students"):
#             print(row)
#     elif choice == "3":
#         sid = int(input("ID: "))
#         marks = float(input("New marks: "))
#         con.execute("UPDATE students SET marks=? WHERE id=?", (marks, sid))
#         con.commit()
#     elif choice == "4":
#         sid = int(input("ID: "))
#         con.execute("DELETE FROM students WHERE id=?", (sid,))
#         con.commit()
#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice")
# con.close()