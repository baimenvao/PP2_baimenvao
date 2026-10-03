#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

pattern = r"ab{2,3}"
test_strings = ["ab", "abb", "abbb", "abbbb"]

print("Task 2 results:")
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"  '{s}' -> Matches")