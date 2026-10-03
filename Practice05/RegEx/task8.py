#Write a Python program to split a string at uppercase letters.



import re

text = "SplitThisStringByCapital"
result = re.split(r"(?=[A-Z])", text)