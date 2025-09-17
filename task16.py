# Generate squares from 1 to 10
squares = [x*x for x in range(1, 11)]
print(squares)



# List comprehension to get vowels
text = "Python Programming is fun!"
vowels = [a for a in text if a.lower() in "aeiou"]
print(vowels)


# List of numbers from 1 to 20
numbers = list(range(1, 21))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
