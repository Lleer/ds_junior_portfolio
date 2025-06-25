def summ_all(*args):
    """
    Складывает все переданные числа.

    Sums all provided numbers.
    Returns:
        int: сумма всех чисел / sum of all numbers
        """
    return sum(args)


def show_info(**kwargs):
    """
    Печатает все переданные пары ключ-значение.

    Prints all provided key-value pairs.
    """
    for key, value in kwargs.items():
        print(key, value)
