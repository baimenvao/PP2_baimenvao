#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
 
import re

pattern = r"ab*"
test_strings = ["a", "ab", "abbb", "b", "ac"]

print("Task 1 results:")
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"  '{s}' -> Matches")