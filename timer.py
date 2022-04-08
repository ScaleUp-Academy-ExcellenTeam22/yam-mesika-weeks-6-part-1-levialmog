import timeit


def timer(f, *parameters):
    """
    The function receives a function and some parameters, calls the function f, passes the parameters to it,
    and returns the run time of function f.
    :param f: The function which measures the run time.
    :param parameters: The parameters passed to function f.
    :return: Run time of function f.
    """
    return timeit.timeit(lambda: f(parameters), number=1)


if __name__ == "__main__":
    timer(zip, [1, 2, 3], [4, 5, 6])
