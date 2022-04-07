import timeit


def timer(f, *parameters):
    """
    The function receives a function and a some parameters, calls the function f and passes the parameters,
    and returns the run time of function f.
    :param f: The function which measures the running time.
    :param parameters: The parameters passed to the function f.
    :return: Run time of function f.
    """
    return timeit.timeit(lambda: f(parameters), number=1)


if __name__ == "__main__":
    timer(zip, [1, 2, 3], [4, 5, 6])
