#!/usr/bin/python3

"""Module for the text_indentation function"""


def text_indentation(text):
    """
    prints 2 lines when encountering specific chars

    Args:
        text: the text to be printed

    Raises:
        TypeError: if text is not a string

    Return:
        the printed text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    text = '\n'.join(lines)

    print(text)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
