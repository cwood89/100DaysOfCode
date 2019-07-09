is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are not a male nor tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or not tall or both")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
else:
    print("Yor are not a male")
