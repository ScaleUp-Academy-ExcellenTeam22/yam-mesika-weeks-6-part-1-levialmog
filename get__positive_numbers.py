def get_positive_numbers():
    """
    Function receives input from the user - a numbers that separate with a comma,
    convert the input to int and return all the positive numbers that entered as a list of int numbers.
    :return: all the positive numbers that entered.
    """
    user_input = input("Enter numbers: ").split(',')

    return filter(lambda number: number > 0, [int(number) for number in user_input])

if __name__ == "__main__":
    print(list(get_positive_numbers()))
