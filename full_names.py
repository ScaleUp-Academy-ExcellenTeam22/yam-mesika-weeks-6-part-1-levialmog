def full_names(first_names, last_names, min_length=0):
    """
    The function gets a list of first names, last names and optional - a minimum length to attach to the list.
    To each first name adds the last names, and if given to us min_length then the first name + last name is equal
    or grater to min_length.
    :param first_names: The list that contains all the first names.
    :param last_names: The list that contains all the last names
    :param min_length: The minimum length of first name plus last name that append to the list.
    :return:
    """
    return [first_name.capitalize() + " " + last_name.capitalize() for first_name in first_names
            for last_name in last_names if len(first_name) + len(last_name) >= min_length]


if __name__ == "__main__":
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    print(full_names(first_names, last_names))
