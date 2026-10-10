
# # Q1. Find sum and average
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for number in numbers:
#     total += number
# average = total / len(numbers) if numbers else 0
# print("Sum:", total)
# print("Average:", average)

# # Q2. Rotate a list by n positions
# numbers = [1, 2, 3, 4, 5]
# n = int(input("Enter rotation positions: "))
# if numbers:
#     n = n % len(numbers)
#     numbers = numbers[-n:] + numbers[:-n] if n else numbers
# print(numbers)

# # Q3. Remove negative numbers
# numbers = [10, -5, 20, -3, 0, 8]
# result = []
# for number in numbers:
#     if number >= 0:
#         result.append(number)
# print(result)

# # Q4. Product of all elements
# numbers = [2, 3, 4, 5]
# product = 1
# for number in numbers:
#     product *= number
# print("Product:", product)

# # Q5. Squares from 1 to n
# n = int(input("Enter n: "))
# squares = []
# for number in range(1, n + 1):
#     squares.append(number * number)
# print(squares)

# # Q6. Split a list into two halves
# numbers = [1, 2, 3, 4, 5, 6]
# middle = len(numbers) // 2
# first_half = numbers[:middle]
# second_half = numbers[middle:]
# print("First half:", first_half)
# print("Second half:", second_half)

# # Q7. Check whether a list is sorted
# numbers = [1, 2, 3, 4, 5]
# is_sorted = True
# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         is_sorted = False
#         break
# print("Sorted" if is_sorted else "Not sorted")

# # Q8. Find pairs with a given sum
# numbers = [2, 4, 3, 5, 7, 8]
# target = int(input("Enter target sum: "))
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])

# # Q9. Flatten a nested list
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = []
# for sublist in nested:
#     for item in sublist:
#         flat.append(item)
# print(flat)

# # Q10. Convert a list into a string without join()
# items = ["Python", "is", "easy"]
# result = ""
# for item in items:
#     if result:
#         result += " "
#     result += str(item)
# print(result)

# # Q11. Student names and marks
# students = {"Aman": 85, "Riya": 92, "Rahul": 78}
# print(students)

# # Q12. Maximum and minimum marks
# marks = {"Aman": 85, "Riya": 92, "Rahul": 78}
# values = list(marks.values())
# if values:
#     maximum = minimum = values[0]
#     for mark in values:
#         if mark > maximum:
#             maximum = mark
#         if mark < minimum:
#             minimum = mark
#     print("Maximum marks:", maximum)
#     print("Minimum marks:", minimum)

# # Q13. Character frequency
# text = input("Enter a string: ")
# frequency = {}
# for char in text:
#     frequency[char] = frequency.get(char, 0) + 1
# print(frequency)

# # Q14. Merge two dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = dict1.copy()
# merged.update(dict2)
# print(merged)

# # Q15. Sort dictionary by keys
# data = {"banana": 3, "apple": 5, "cherry": 2}
# sorted_data = dict(sorted(data.items()))
# print(sorted_data)

# # Q16. Sort dictionary by values
# data = {"Aman": 75, "Riya": 92, "Rahul": 81}
# sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
# print(sorted_data)

# # Q17. Update a dictionary value
# student = {"name": "Aman", "marks": 80}
# student["marks"] = 90
# print(student)

# # Q18. Remove a key
# student = {"name": "Aman", "marks": 80, "roll": 12}
# student.pop("roll", None)
# print(student)

# # Q19. Check whether a key exists
# student = {"name": "Aman", "marks": 80}
# key = input("Enter key to check: ")
# print(key in student)

# # Q20. Sum of dictionary values
# marks = {"Aman": 80, "Riya": 90, "Rahul": 75}
# total = 0
# for value in marks.values():
#     total += value
# print("Sum:", total)

# # Q21. Key with maximum value
# marks = {"Aman": 80, "Riya": 95, "Rahul": 75}
# if marks:
#     max_key = next(iter(marks))
#     for key in marks:
#         if marks[key] > marks[max_key]:
#             max_key = key
#     print("Key:", max_key)
#     print("Value:", marks[max_key])

# # Q22. Numbers and their squares
# n = int(input("Enter n: "))
# squares = {}
# for number in range(1, n + 1):
#     squares[number] = number * number
# print(squares)

# # Q23. Convert two lists into a dictionary
# keys = ["name", "age", "city"]
# values = ["Aman", 21, "Roorkee"]
# result = dict(zip(keys, values))
# print(result)

# # Q24. Invert a dictionary
# data = {"a": 1, "b": 2, "c": 3}
# inverted = {}
# for key, value in data.items():
#     inverted[value] = key
# print(inverted)

# # Q25. Word frequency
# paragraph = input("Enter a paragraph: ").lower()
# frequency = {}
# for word in paragraph.split():
#     word = word.strip(".,!?;:\"'()")
#     if word:
#         frequency[word] = frequency.get(word, 0) + 1
# print(frequency)

# # Q26. Check dictionary equality
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 2, "a": 1}
# print(dict1 == dict2)

# # Q27. Remove duplicate values
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# result = {}
# seen = []
# for key, value in data.items():
#     if value not in seen:
#         result[key] = value
#         seen.append(value)
# print(result)

# # Q28. Nested dictionary for student details
# students = {
#     "student1": {"Name": "Aman", "Roll": 1, "Marks": 85},
#     "student2": {"Name": "Riya", "Roll": 2, "Marks": 92}
# }
# print(students)

# # Q29. Find common keys
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 5, "c": 6, "d": 7}
# common_keys = []
# for key in dict1:
#     if key in dict2:
#         common_keys.append(key)
# print(common_keys)

# # Q30. Character frequency dictionary
# text = input("Enter a string: ")
# frequency = {}
# for char in text:
#     frequency[char] = frequency.get(char, 0) + 1
# print(frequency)
