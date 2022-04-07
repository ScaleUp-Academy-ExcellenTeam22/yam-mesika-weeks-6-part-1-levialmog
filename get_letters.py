def get_letters():
    """
    The function returns the letters A to Z and a to z as a list.
    :return: The list of all letters - A to Z and a to z.
    """
    return [chr(letter) for letter in range(ord('A'), ord('z') + 1) if chr(letter).isalpha()]


if __name__ == "__main__":
    print(get_letters())
