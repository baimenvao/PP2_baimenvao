# Task 1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

# Task 2
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)

n = int(input())
print(",".join(even_generator(n)))

# Task 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

# Task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for val in squares(1, 5):
    print(val)

# Task 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1