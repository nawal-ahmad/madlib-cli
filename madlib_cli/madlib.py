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


def read_template(path):
    with open(path, "r") as file:
        file = file.read()
    return file.strip()


# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
# find all the words inside brackets,and replace them with an empty
def parse_template(text):
    parse = re.findall(r'\{(.*?)\}', text)
    for word in parse:
        text = text.replace(word, '', 1)
    return (text, tuple(parse))


def merge(text, parse):
    new_text = text.format(*parse)
    with open('assets/parse_merge.text', 'w') as output:
        output.write(new_text)
    return new_text
