import random
import cProfile


def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total


def sort_big_list(lst):
    return sorted(lst)


lst = list(range(1, 10001))
big_lst = [random.randint(1, 100000) for _ in range(10000)]

cProfile.run('sum_list(lst)')
cProfile.run('sort_big_list(big_lst)')
