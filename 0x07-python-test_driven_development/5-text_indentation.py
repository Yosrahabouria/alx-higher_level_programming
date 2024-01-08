#!/usr/bin/python3
def text_indentation(text):
    """prints a text with 2 new lines after characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for a in ".,?":
        text = (a + "\n\n").join(
               [b.strip(" ") for b in text.split(a)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
