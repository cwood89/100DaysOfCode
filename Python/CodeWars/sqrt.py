# Return the next square number after the one passed in as a paramter. If the number passed in is not square return -1

import math


def find_next_square(sq):
    if not math.sqrt(sq).is_integer():
        return -1
    elif math.sqrt(sq).is_integer() or sq == 0:
        num = sq + 1
        while not math.sqrt(num).is_integer():
            num += 1
            if math.sqrt(num).is_integer():
                return num


print(find_next_square(121))  # should be 169


# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     return -1
