def count_words(checked_text):
    """
    The function receives text and returns a dictionary where the values are the words from the text
    and the keys are the length of the word.
    :param checked_text: The text that the function received as a parameter.
    :return: The dictionary where the values are the words from the text and the keys are the length of the word.
    """
    return {word: len(word) for word in checked_text.split()}


if __name__ == "__main__":
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
