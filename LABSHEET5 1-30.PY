# # Q1. Create and display a tuple
# t = (10, 20, 30, 40)
# print(t)

# # Q2. Tuple with different data types
# t = (10, "Python", 3.5, True)
# print(t)

# # Q3. Find tuple length
# t = (10, 20, 30, 40, 50)
# print(len(t))

# # Q4. Access elements using indexing
# t = (10, 20, 30, 40, 50)
# print(t[0])
# print(t[2])
# print(t[-1])

# # Q5. Access elements using slicing
# t = (10, 20, 30, 40, 50)
# print(t[1:4])

# # Q6. Check if an element exists
# t = (10, 20, 30, 40, 50)
# print(30 in t)

# # Q7. Count occurrences
# t = (10, 20, 10, 30, 10, 40)
# print(t.count(10))

# # Q8. Find element index
# t = (10, 20, 30, 40, 50)
# print(t.index(30))

# # Q9. Concatenate tuples
# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# print(t1 + t2)

# # Q10. Repeat tuple n times
# t = (10, 20)
# n = 3
# print(t * n)

# # Q11. Convert list to tuple
# numbers = [10, 20, 30, 40]
# print(tuple(numbers))

# # Q12. Convert tuple to string
# t = ("P", "y", "t", "h", "o", "n")
# print("".join(t))

# # Q13. Maximum and minimum values
# t = (25, 10, 45, 5, 30)
# print("Maximum:", max(t))
# print("Minimum:", min(t))

# # Q14. Sum of numeric elements
# t = (10, 20, 30, 40, 50)
# print(sum(t))

# # Q15. Sort numbers in ascending order
# t = (40, 10, 30, 20, 50)
# print(tuple(sorted(t)))

# # Q16. Sort strings alphabetically
# t = ("Mango", "Apple", "Banana", "Orange")
# print(tuple(sorted(t)))

# # Q17. Reverse a tuple
# t = (10, 20, 30, 40, 50)
# print(t[::-1])

# # Q18. Check tuple equality
# t1 = (10, 20, 30)
# t2 = (10, 20, 30)
# print(t1 == t2)

# # Q19. Remove duplicate elements
# t = (10, 20, 10, 30, 20, 40)
# print(tuple(dict.fromkeys(t)))

# # Q20. Length of the longest word
# words = ("Python", "Programming", "Computer", "Code")
# longest = 0
# for word in words:
#     if len(word) > longest:
#         longest = len(word)
# print(longest)

# # Q21. Nested tuple and access elements
# t = ((10, 20), (30, 40), (50, 60))
# print(t[1])
# print(t[1][0])

# # Q22. Flatten a nested tuple
# t = ((10, 20), (30, 40), (50, 60))
# result = tuple(item for subtuple in t for item in subtuple)
# print(result)

# # Q23. Swap two tuples
# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# t1, t2 = t2, t1
# print("t1:", t1)
# print("t2:", t2)

# # Q24. Common elements
# t1 = (10, 20, 30, 40)
# t2 = (30, 40, 50, 60)
# print(tuple(x for x in t1 if x in t2))

# # Q25. Difference between tuples
# t1 = (10, 20, 30, 40)
# t2 = (30, 40, 50, 60)
# print(tuple(x for x in t1 if x not in t2))

# # Q26. Tuple of tuples to dictionary
# t = (("a", 1), ("b", 2), ("c", 3))
# print(dict(t))

# # Q27. Unzip list of tuples
# items = [(1, "A"), (2, "B"), (3, "C")]
# numbers, letters = zip(*items)
# print(list(numbers))
# print(list(letters))

# # Q28. Find repeated items
# t = (10, 20, 10, 30, 20, 40)
# repeated = tuple(x for x in dict.fromkeys(t) if t.count(x) > 1)
# print(repeated)

# # Q29. Check if all elements are the same
# t = (10, 10, 10, 10)
# print(all(x == t[0] for x in t))

# # Q30. Element-wise sum
# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# print(tuple(a + b for a, b in zip(t1, t2)))
