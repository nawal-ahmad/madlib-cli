# read_template, parse_template, merge

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


def the_game():

    print('Welcome to Madlib Game')
    print('Are you ready 🔥🔥')
    print('answer the questions and enjoy it!')

    text = read_template('assets/game.txt')

    text, parse = parse_template(text)
    input_list = []
    for i in parse:
        user_input = input(f'Enter a {i} ')
        input_list.append(user_input)

    text_output = merge(text, input_list)

    return text_output


if __name__ == '__main__':
    print(the_game())
