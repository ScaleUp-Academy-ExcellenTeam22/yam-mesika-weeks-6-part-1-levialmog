def my_filter(my_iterable):
    """
    The function receives a list and returns the elements that return true.
    :param my_iterable: The checked list.
    :return: Only the object that returns true.
    """
    return [iterate for iterate in my_iterable if iterate]


if __name__ == "__main__":
    print(my_filter([1, True, 0, False]))
