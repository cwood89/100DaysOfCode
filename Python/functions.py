# # after defining function all contained code must me indented
# def hello(name, age):
#     print("Hello! " + name)
#     print("You are " + str(age))
# hello("Chris", 27)
# # def cube(num):
# # return num * num * num
# # result = cube(20)
# # print(result)
# # print(2**3)  # prints 2 cubed
# def raise_to_power(base, pow):
#     result = 1
#     for i in range(pow):
#         result = result * base
#     return result
# print(raise_to_power(3, 4))
# def g(x): return x*x*x
# print(g(7))


from functools import reduce

numbers = [3, 2, 12, 6, 4, 9, 7, 15]

# List Comprehension
doubled = [i * 2 for i in numbers]
even = [i for i in numbers if i % 2 == 0]
print(doubled)  # creates new list with each item doubled
print(even)  # uses conditional argument to get even numbers

# Lambda Functions
cube = list(map(lambda x: (x * x * x), numbers))
odd = list(filter(lambda x: (x % 2 != 0), numbers))
add = reduce((lambda x, y: x + y), numbers)
print(cube)  # maps through numbers and retuns each item cubed
print(odd)  # filters all odds numbers and returns them in a list
print(add)  # reduce needs to be imported from functools
