# 1. Extract the first and last character of a string: text = "Programming" print(text[0], text[-1])

text = "Programming"
print(text[0], text[-1])

# 2. Reverse a string: reversed_text = text[::-1] print(reversed_text) # gnimmargorP
reversed_text = text[::-1]
print(reversed_text)

# 3. Count occurrences of a specific character: print(text.count("m"))
print(text.count("m"))

# 4. Replace spaces with underscores: sentence = "Python is fun to learn" print(sentence.replace(" ", "_")) # Python_is_fun_to_learn
sentence = "Python is fun to learn"
print(sentence.replace("_", "_"))

# 5. Check if a string is a palindrome: word = "madam" print(word == word[::-1])
word = "madam"
print(word == word[::-1])
