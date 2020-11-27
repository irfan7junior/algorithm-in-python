from ..VII_Quicksort import random_quick_sort


from typing import List, TypeVar


T = TypeVar('T', int, float, str)


def randomized_select(array: List[T], p: int, r: int, i: int) -> int:
  # only one element is left return that
  if p == r:
    return array[p]

  # partition the array around a random element
  q = random_quick_sort.partition(array, p, r)

  # index of the partition element
  k = q - p

  # if the array[k] is the ith smallest element, return it
  if i == k:
    return array[q]

  # if 'i' is less than 'k', continue our seach in the left-hand side
  elif i < k:
    return randomized_select(array, p, q - 1, i)
  # if 'i' is greater than 'k', continue our search in the right-hand side
  else:
    return randomized_select(array, q + 1, r, i - k - 1)
