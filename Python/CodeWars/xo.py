# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.


def xo(s):
    x = 0
    o = 0
    result = False
    for letter in s:
        if letter.lower() == "o":
            o += 1
        elif letter.lower() == "x":
            x += 1
    if x == o:
        result = True
    return result


print(xo("XOoOx"))  # should be false
print(xo("XXXxxxOOOooo"))  # should be true

# More efficent version

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')
