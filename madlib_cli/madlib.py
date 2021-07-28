#read_template, parse_template, merge

import re
from typing import Text

# Print a welcome message to the user, explaining the Madlib process and command line interactions


def welcome():
    print(
        """
    Welcome to MadLib Game!
    Are you ready ?
    lets get started ...

    """
    )

# Read a template Madlib file (Example), and parse that file into usable parts.


def read_template(path: str) -> str:
    try:
        with open(path, "r") as file:
            file = file.read()
        return file.strip()
    except FileNotFoundError:
        raise

# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
# find all the words inside brackets,and replace them with an empty


def parse_template(text: str) -> list:
    parse = re.findall(r'\{(.*?)\}', text)
    for word in parse:
        text = text.replace(word, '', 1)
    return (text, tuple(parse))

#  Function for merge the text with the empty brackets and the user's answer


def merge(text, parse):
    new_text = text.format(*parse)
    with open('assets/parse_merge.text', 'w') as output:
        output.write(new_text)
    return new_text


def sum_matrix(matrix):
    length = len(matrix)
    arr_sum = []
    for i in range(length):
        sum = 0
        for element in matrix[i]:
            sum += element
        arr_sum += [sum]
    return arr_sum


m = [[1, 2], [3, 4], [5, 6, 7]]
print(sum_matrix(m))
