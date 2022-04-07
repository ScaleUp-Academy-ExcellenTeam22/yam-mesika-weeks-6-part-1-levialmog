def words_length(sentence):
    """
    The function receives a sentence, divides the sentence to words and returns the lengths of the words in their order.
    :param sentence: The accepted sentence.
    :return: List of word lengths.
    """
    return [len(word) for word in sentence.split()]


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
