import math


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if type(math.sqrt(sq)) != "int":
        print(math.sqrt(sq))
        return -1
    else:
        num = sq + 1
        while type(math.sqrt(num)) != "int":
            num + 1
    return num


print(find_next_square(144))
