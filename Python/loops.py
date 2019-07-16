
# as long as condition is true this will continually run
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop.")

# loops through each letter and prints
for letter in "Wolf":
    print(letter)

friends = ["mike", "sarah", "jim", "kevin"]
len(friends)  # gets the length of array
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first number")
    else:
        print("number")
