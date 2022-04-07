def get_letters():
    """
    The function goes through all the letters between A to Z and a to z and creates all the arranged pairs.
    :return: The list of all characters between a and z and between A and Z.
    """
    return [(chr(capital_letter), chr(lower_letter))
            for capital_letter in range(ord('B'), ord('Z'))
            for lower_letter in range(ord('b'), ord('z'))]


if __name__ == "__main__":
    print(get_letters())
