# # Q1. Create and display a set
# numbers = {10, 20, 30, 40}
# print(numbers)

# # Q2. Set with different data types
# items = {10, "Python", 3.5, True}
# print(items)

# # Q3. Add a single element
# numbers = {10, 20, 30}
# numbers.add(40)
# print(numbers)

# # Q4. Add multiple elements
# numbers = {10, 20, 30}
# numbers.update([40, 50, 60])
# print(numbers)

# # Q5. Remove using remove()
# numbers = {10, 20, 30, 40}
# numbers.remove(30)
# print(numbers)

# # Q6. Remove using discard()
# numbers = {10, 20, 30, 40}
# numbers.discard(30)
# print(numbers)
# # Q7. Clear a set
# numbers = {10, 20, 30}
# numbers.clear()
# print(numbers)

# # Q8. Check membership
# numbers = {10, 20, 30, 40}
# print(20 in numbers)

# # Q9. Length of a set
# numbers = {10, 20, 30, 40}
# print(len(numbers))

# # Q10. Iterate through a set
# numbers = {10, 20, 30, 40}
# for number in numbers:
#     print(number)

# # Q11. Union of two sets
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))

# # Q12. Intersection of two sets
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))

# # Q13. Difference of two sets
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# print(a.difference(b))

# # Q14. Symmetric difference
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.symmetric_difference(b))

# # Q15. Check subset
# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a.issubset(b))

# # Q16. Check superset
# a = {1, 2, 3, 4}
# b = {1, 2}
# print(a.issuperset(b))

# # Q17. Check disjoint sets
# a = {1, 2, 3}
# b = {4, 5, 6}
# print(a.isdisjoint(b))

# # Q18. Remove elements of one set from another
# a = {1, 2, 3, 4, 5}
# b = {2, 4}
# a.difference_update(b)
# print(a)

# # Q19. Create a power set
# from itertools import combinations

# items = {1, 2, 3}
# power_set = []
# values = list(items)
# for size in range(len(values) + 1):
#     for group in combinations(values, size):
#         power_set.append(set(group))
# print(power_set)

# # Q20. Cartesian product
# a = {1, 2}
# b = {"x", "y"}
# product = {(x, y) for x in a for y in b}
# print(product)

# # Q21. Count distinct elements
# items = [1, 2, 2, 3, 4, 4, 5]
# print(len(set(items)))

# # Q22. Find duplicates using a set
# items = [1, 2, 3, 2, 4, 1, 5]
# seen = set()
# duplicates = set()
# for item in items:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)
# print(duplicates)

# # Q23. Remove duplicates using a set
# items = [1, 2, 2, 3, 4, 4, 5]
# unique_items = list(set(items))
# print(unique_items)

# # Q24. String to set of characters
# text = input("Enter a string: ")
# characters = set(text)
# print(characters)

# # Q25. Common letters in two strings
# text1 = input("Enter first string: ").lower()
# text2 = input("Enter second string: ").lower()
# common = set(text1).intersection(set(text2))
# common.discard(" ")
# print(common)

# # Q26. Unique words in a sentence
# sentence = input("Enter a sentence: ").lower()
# words = set(sentence.split())
# print(words)

# # Q27. Check anagrams using sets
# text1 = input("Enter first string: ").replace(" ", "").lower()
# text2 = input("Enter second string: ").replace(" ", "").lower()
# print(len(text1) == len(text2) and set(text1) == set(text2) and
#       all(text1.count(ch) == text2.count(ch) for ch in set(text1)))

# # Q28. Create and use a frozenset
# items = frozenset([10, 20, 30, 20])
# print(items)
# print("Contains 20:", 20 in items)
# print("Length:", len(items))
# # A frozenset cannot be changed after creation.

# # Q29. Maximum and minimum values
numbers = {25, 10, 45, 5, 30}
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# # Q30. Basic set operations
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print("Union:", a | b)
# print("Intersection:", a & b)
# print("Difference (A - B):", a - b)
# print("Symmetric difference:", a ^ b)
