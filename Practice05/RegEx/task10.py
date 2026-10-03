#Write a Python program to convert a given camel case string to snake case.

import re


def camel_to_snake(text):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()