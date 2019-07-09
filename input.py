name = input("What's your name? ")
age = input("How old are you? ")
print("Hello " + name + "! You are " + age + " years old!")

# caculator =====================

num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

result = float(num1) + float(num2)
# int() converts to whole number, float() converts to decimal number
print("Your result: " + str(result))


# madlibs python
adj = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
plural_noun = input("Enter a plural noun: ")
print("I used to be " + adj)
print("But now I'm " + adj2)
print("All because I wanted some " + plural_noun)
