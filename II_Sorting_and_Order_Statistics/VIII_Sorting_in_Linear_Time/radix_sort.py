from .counting_sort import counting_sort
from typing import TypeVar, List

T = TypeVar('T', str, int)


def radix_sort(array: List[T]) -> None:
  max_num = max(array)
  exp = 1
  while max_num > 0:
    counting_sort(array, exp)
    exp *= 10
    max_num /= exp
