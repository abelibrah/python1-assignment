# assignment.py
# 1. Create empty list
my_list = []

# 2. Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append:", my_list)

# 3. Insert 15 at second position (index 1)
my_list.insert(1, 15)
print("After insert:", my_list)

# 4. Extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extend:", my_list)

# 5. Remove the last element
removed = my_list.pop()
print("Removed:", removed)
print("After pop:", my_list)

# 6. Sort ascending
my_list.sort()
print("After sort:", my_list)

# 7. Find and print index of 30
print("Index of 30:", my_list.index(30))
