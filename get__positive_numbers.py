def get_positive_numbers():
    """
    Function receives input from the user using, convert the input to int and return all the positive numbers that
    entered, as a list of int numbers.
    :return: all the positive numbers that entered.
    """
    user_input = input("Enter numbers: ").split(',')

    user_input = [int(number) for number in user_input]

    return filter(lambda number: number > 0, user_input)


if __name__ == "__main__":
    print(list(get_positive_numbers()))
