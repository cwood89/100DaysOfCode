
enemies = ["Mike", "Tracy", "Bob", "Kurt", "Jim"]
enemies[1] = "Bruce"

print(enemies[1])  # arrays start at 0
print(enemies[-1])  # prints last item in array
print(enemies[1:])  # colon returns all items starting from specified index
print(enemies[1:3])  # gives a range, index 1 to but not including index 3

# list functions ==================
lucky_numbers = [9, 12, 34, 45, 38, 17]
friends = ["Jim", "Mike", "Tracy", "Bob", "Kurt", "Jim"]
friends.append("Kobe")  # adds item to end of list
friends.insert(2, "Chris")  # adds item in a specified index
friends.pop()  # removes last element
friends.index("Bob")  # which index
friends.count("Jim")  # how many
friends.sort()  # acending order
friends.reverse()  # reverses a list
friends2 = friends.copy()  # copies a list
friends.clear()  # emptys list
friends.extend(lucky_numbers)  # adds another list to the end of the first list
# tuples
coordnates = (4, 5)  # tuples are the same as lists or arrays but are imutable
places = [(1, 2), (3, 4), (5, 6)]  # list of tuples
