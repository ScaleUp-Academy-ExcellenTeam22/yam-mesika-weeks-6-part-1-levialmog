import timeit


def timer(f, *parameters):
    """
    The function receives a function named f and some parameters, calls function f, passes the parameters to it,
    and returns the run time of function f.
    :param f: The function that it's run time is measured.
    :param parameters: The parameters passed to function f.
    :return: Run time of function f.
    """
    return timeit.timeit(lambda: f(parameters), number=1)


if __name__ == "__main__":
    timer(zip, [1, 2, 3], [4, 5, 6])
