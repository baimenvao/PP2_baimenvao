# Here is a filter function using lambda to extract only even numbers
numbers = [12, 17, 24, 33, 40, 55, 68]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# Here is a filter function using lambda to select passing scores
scores = [85, 42, 73, 58, 90, 48, 65]
passing_scores = list(filter(lambda score: score >= 60, scores))
print("Passing scores (60 and above):", passing_scores)


# Here is a filter function using lambda to keep only long words
words = ["apple", "cat", "banana", "dog", "orange", "sun"]
long_words = list(filter(lambda word: len(word) > 4, words))
print("Words longer than 4 letters:", long_words)
