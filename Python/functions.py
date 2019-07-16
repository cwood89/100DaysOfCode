# after defining function all contained code must me indented
def hello(name, age):
    print("Hello! " + name)
    print("You are " + str(age))


hello("Chris", 27)


def cube(num):
    return num * num * num


result = cube(20)
print(result)


print(2**3)  # prints 2 cubed


def raise_to_power(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result


print(raise_to_power(3, 4))
