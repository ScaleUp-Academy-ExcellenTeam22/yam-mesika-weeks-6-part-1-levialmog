def my_function(iterate):
    if iterate:
        return True

    return False


def my_filter(my_function, my_iterable):
    return [iterate for iterate in my_iterable if my_function(iterate)]


if __name__ == "__main__":
    my_iterable = [1, True, 0, False]
    print(my_filter(my_function, my_iterable))
