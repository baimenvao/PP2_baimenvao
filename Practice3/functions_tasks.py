import math
from itertools import permutations
import random

# ==========================================
# Task 1: Grams to Ounces
# ==========================================
# Here is a function to convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams


# ==========================================
# Task 2: Fahrenheit to Centigrade
# ==========================================
# Here is a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


# ==========================================
# Task 3: Chickens and Rabbits puzzle
# ==========================================
# Here is a function to solve the chickens and rabbits puzzle
def solve(numheads, numlegs):
    # c + r = heads  =>  2c + 2r = 2heads
    # 2c + 4r = legs =>  2r = legs - 2heads => r = (legs - 2heads) / 2
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    if rabbits >= 0 and chickens >= 0 and (2 * chickens + 4 * rabbits == numlegs):
        return chickens, rabbits
    return "No solution", "No solution"


# ==========================================
# Task 4: Filter prime numbers from list
# ==========================================
# Here is a function to filter prime numbers from a list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


# ==========================================
# Task 5: Print all permutations of a string
# ==========================================
# Here is a function to print all permutations of a string
def print_permutations(text):
    perms = [''.join(p) for p in permutations(text)]
    print(f"Permutations of '{text}':", perms)


# ==========================================
# Task 6: Reverse words in a sentence
# ==========================================
# Here is a function to reverse the order of words in a sentence
def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(reversed(words))


# ==========================================
# Task 7: Check for consecutive 3s
# ==========================================
# Here is a function to check if a list has consecutive 3s
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


# ==========================================
# Task 8: Check for 007 sequence
# ==========================================
# Here is a function to check if the list contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False


# ==========================================
# Task 9: Volume of a sphere
# ==========================================
# Here is a function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)


# ==========================================
# Task 10: Unique elements in a list without set()
# ==========================================
# Here is a function that returns unique elements from a list without using set
def unique_list(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


# ==========================================
# Task 11: Palindrome checker
# ==========================================
# Here is a function to check if a word or phrase is a palindrome
def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


# ==========================================
# Task 12: Histogram printer
# ==========================================
# Here is a function to print a histogram using asterisks
def histogram(numbers):
    for n in numbers:
        print("*" * n)


# ==========================================
# Task 13: Guess the number game
# ==========================================
# Here is the Guess the Number game function
def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


# ==========================================
# Task 14: Demonstration of the functions
# ==========================================
if __name__ == "__main__":
    print("Task 1 (100 grams to ounces):", grams_to_ounces(100))
    print("Task 2 (100 Fahrenheit to Celsius):", fahrenheit_to_celsius(100))
    chickens, rabbits = solve(35, 94)
    print(f"Task 3: Chickens = {chickens}, Rabbits = {rabbits}")
    print("Task 4 (Primes):", filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print_permutations("abc")
    print("Task 6:", reverse_sentence("We are ready"))
    print("Task 7 (has_33):", has_33([1, 3, 3]), has_33([1, 3, 1, 3]))
    print("Task 8 (spy_game):", spy_game([1, 2, 4, 0, 0, 7, 5]), spy_game([1, 7, 2, 0, 4, 5, 0]))
    print("Task 9 (Sphere volume, r=5):", sphere_volume(5))
    print("Task 10 (Unique):", unique_list([1, 2, 2, 3, 4, 4, 5]))
    print("Task 11 (Palindrome 'madam'):", is_palindrome("madam"))
    print("Task 12 (Histogram):")
    histogram([4, 9, 7])

   
    # guess_the_number()