#Write a Python program to insert spaces between words starting with capital letters.



import re

text = "InsertSpacesBetweenWords"
result = re.sub(r"(\w)([A-Z])", r"\1 \2", text)