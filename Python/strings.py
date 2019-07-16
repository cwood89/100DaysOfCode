# The backslash ( "\" ) character is a special escape
#  character used to indicate other special characters such
# as new lines ( \n ), tabs ( \t ), or quotation marks ( \" ).
#  If you want to include a backslash character itself, you need two backslashes or use the @ verbatim string: "\\Tasks" or @"\Tasks" .

phrase = "Chris\n is learning \"Python!\""

print(phrase)

print(phrase.upper())  # changes string to uppercase
print(phrase.lower())  # changes string to lowercase
print(phrase.islower())  # true if all letters are lowercase
print(phrase.isupper())  # true if all letters are uppercase
print(len(phrase))  # prints length of strings in number of characters
print(phrase[0])  # prints specific character based on index
print(phrase.index("P"))
# prints index of passed in character or group of characters
print(phrase.replace("Chris", "Bobby"))
# replace characters or words in string
