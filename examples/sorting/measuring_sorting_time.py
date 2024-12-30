from random import randint
from time import time

from algorithms.sorting import quick_sort, merge_sort


def time_sorting_algorithm(algorithm, arr_length: int = 10000):
    """
    Counts the execution time of sorting algorithm

    Args:
        algorithm: sorting algorithm that will be tested
        arr_length: array length to be used by sorting algorithm
    """

    arr = [randint(1, 1000) for _ in range(arr_length)]

    start_time = time()
    algorithm(arr)
    end_time = time()

    print(f'Execution time of {algorithm.__name__} algorithm is {end_time - start_time:.6f}')


if __name__ == '__main__':
    time_sorting_algorithm(quick_sort, 1000000)
    time_sorting_algorithm(merge_sort, 1000000)
