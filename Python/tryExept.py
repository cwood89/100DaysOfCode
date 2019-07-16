
number = int(input("Enter a number: "))

print(number)

# if user enters a letter program will crash

# try except will catch errors
try:
    value = 10/0  # cant divide by zero throws error
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
