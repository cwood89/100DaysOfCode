
secret_word = "wolf"
guess = ""
strike_count = 0
strikes = 3
out = False

while guess != secret_word and not(out):
    if strike_count < strikes:
        guess = input("Enter guess: ")
        strike_count += 1
    else:
        out = True

if out:
    print("You Lose")
else:
    print("You Win!!")
