# # Q1: Create a file and write text into it
# with open("data.txt", "w") as f:
#     f.write("Hello Python!")
# print("Data written successfully")

# # Q2: Read and display the complete file content
# with open("data.txt", "r") as f:
#     print(f.read())

# # Q3: Read the file one line at a time
# with open("data.txt", "r") as f:
#     for line in f:
#         print(line, end="")

# # Q4: Count words by splitting the file content
# with open("data.txt", "r") as f:
#     words = f.read().split()
# print("Words:", len(words))

# # Q5: Count lines and characters in the file
# with open("data.txt", "r") as f:
#     content = f.read()
# print("Lines:", len(content.splitlines()))
# print("Characters:", len(content))

# # Q6: Display lines numbered 2, 4, 6, and so on
# with open("data.txt", "r") as f:
#     for line_number, line in enumerate(f, start=1):
#         if line_number % 2 == 0:
#             print(line, end="")

# # Q7: Save user-entered lines until the user types "stop"
# with open("data.txt", "w") as f:
#     while True:
#         line = input("Enter text (stop to finish): ")
#         if line.lower() == "stop":
#             break
#         f.write(line + "\n")
# print("File saved")

# # Q8: Append text without deleting existing content
# with open("data.txt", "a") as f:
#     f.write("\nWelcome to Python")
# print("Content appended")

# # Q9: Copy data.txt content into copy.txt
# with open("data.txt", "r") as source:
#     content = source.read()
# with open("copy.txt", "w") as destination:
#     destination.write(content)
# print("File copied successfully")

# # Q10: Convert all file text to uppercase and display it
# with open("data.txt", "r") as f:
#     content = f.read()
# print(content.upper())

# # Q11: Search for a whole word, ignoring letter case
# with open("data.txt", "r") as f:
#     words = f.read().lower().split()
# search_word = input("Enter word to search: ").lower()
# if search_word in words:
#     print("Word found")
# else:
#     print("Word not found")

# # Q12: Count how many times a word appears
# with open("data.txt", "r") as f:
#     words = f.read().lower().split()
# search_word = input("Enter word: ").lower()
# print("Occurrences:", words.count(search_word))

# # Q13: Read whitespace-separated numbers from numbers.txt
# with open("numbers.txt", "r") as f:
#     numbers = list(map(float, f.read().split()))
# if numbers:
#     total = sum(numbers)
#     print("Sum:", total)
#     print("Average:", total / len(numbers))
# else:
#     print("No numbers found in the file")

# # Q14: Find and display the longest line
# with open("data.txt", "r") as f:
#     lines = f.readlines()
# if lines:
#     print("Longest line:", max(lines, key=len).strip())
# else:
#     print("File is empty")

# # Q15: Replace every occurrence and save changes
# with open("data.txt", "r") as f:
#     content = f.read()
# content = content.replace("Python", "Java")
# with open("data.txt", "w") as f:
#     f.write(content)
# print("Word replaced successfully")

# # Q16: Display first and last lines if the file is not empty
# with open("data.txt", "r") as f:
#     lines = f.readlines()
# if lines:
#     print("First line:", lines[0].strip())
#     print("Last line:", lines[-1].strip())
# else:
#     print("File is empty")

# # Q17: Remove blank lines from a file
# with open("data.txt", "r") as f:
#     lines = f.readlines()
# with open("data.txt", "w") as f:
#     for line in lines:
#         if line.strip():
#             f.write(line)
# print("Blank lines removed")

# # Q18: Store only unique words in another file
# with open("data.txt", "r") as f:
#     words = f.read().split()
# unique_words = list(dict.fromkeys(words))
# with open("unique.txt", "w") as f:
#     f.write("\n".join(unique_words))
# print("Unique words saved")

# # Q19: Sort all words alphabetically and save to a new file
# with open("data.txt", "r") as f:
#     words = f.read().split()
# words.sort(key=str.lower)
# with open("sorted.txt", "w") as f:
#     f.write(" ".join(words))
# print("Sorted words saved")

# # Q20: Merge two text files into a third file
# with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
#     content = f1.read() + "\n" + f2.read()
# with open("merged.txt", "w") as f3:
#     f3.write(content)
# print("Files merged")

# # Q21: Create and write data into a CSV file
# import csv

# with open("students.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Marks"])
#     writer.writerow(["Aman", 85])
#     writer.writerow(["Riya", 92])
# print("CSV file created")

# # Q22: Read and display data from a CSV file
# import csv

# with open("students.csv", "r", newline="") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# # Q23: Calculate the average of numeric columns in a CSV file
# import csv

# totals = {}
# counts = {}
# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         for key, value in row.items():
#             try:
#                 number = float(value)
#                 totals[key] = totals.get(key, 0) + number
#                 counts[key] = counts.get(key, 0) + 1
#             except (ValueError, TypeError):
#                 pass
# for key in totals:
#     print(key, "average:", totals[key] / counts[key])

# # Q24: Count the number of rows and columns in a CSV file
# import csv

# with open("students.csv", "r", newline="") as f:
#     reader = csv.reader(f)
#     rows = list(reader)
# if rows:
#     print("Rows (excluding header):", len(rows) - 1)
#     print("Columns:", len(rows[0]))
# else:
#     print("CSV file is empty")

# # Q25: Append a new record to an existing CSV file
# import csv

# with open("students.csv", "a", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Karan", 78])
# print("Record added")

# # Q26: Copy data from one CSV file to another
# import csv

# with open("students.csv", "r", newline="") as source:
#     rows = list(csv.reader(source))
# with open("students_copy.csv", "w", newline="") as destination:
#     writer = csv.writer(destination)
#     writer.writerows(rows)
# print("CSV data copied")

# # Q27: Display specific columns such as Name and Marks
# import csv

# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["Name"], row["Marks"])

# # Q28: Find and display the highest marks in a CSV file
# import csv

# with open("students.csv", "r", newline="") as f:
#     students = list(csv.DictReader(f))
# if students:
#     top_student = max(students, key=lambda row: float(row["Marks"]))
#     print("Highest marks:", top_student["Marks"])
#     print("Student:", top_student["Name"])
# else:
#     print("No student records found")

# # Q29: Search for a record by student name
# import csv

# name = input("Enter student name: ").strip().lower()
# found = False
# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row["Name"].strip().lower() == name:
#             print(row)
#             found = True
# if not found:
#     print("Record not found")

# # Q30: Combine multiple CSV files into one file (same columns)
# import csv

# input_files = ["students1.csv", "students2.csv"]
# with open("combined.csv", "w", newline="") as output:
#     writer = csv.writer(output)
#     header_written = False
#     for filename in input_files:
#         with open(filename, "r", newline="") as source:
#             reader = csv.reader(source)
#             header = next(reader, None)
#             if header is None:
#                 continue
#             if not header_written:
#                 writer.writerow(header)
#                 header_written = True
#             for row in reader:
#                 writer.writerow(row)
# print("CSV files combined")