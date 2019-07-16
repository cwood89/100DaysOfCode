
# "r" - read only
# "w" - write: creates new file or rewrites exiting file
# "a" - appends to file
# "r+" - read and write

fave_cars = open("list.txt", "r")  # read

print(fave_cars.readable())  # true
print(fave_cars.read())  # reads whole file
print(fave_cars.readline())  # reads first line
print(fave_cars.readline())  # reads second line
print(fave_cars.readlines())  # takes each line and returns a list
print(fave_cars.readlines()[1])  # reads first line
# prints all lines using for loop
for line in (fave_cars):
    print(line)

# if you open a file you have to close the file
fave_cars.close()

fave_car = open("list.txt", "a")  # append
fave_car.write("\nDodge - Challenger")
# used escape character to create new line
fave_car.close()

# creates new file
fave_shows = open("list1.txt", "w")  # write
fave_shows.write("Game of Thrones")
fave_shows.close()
