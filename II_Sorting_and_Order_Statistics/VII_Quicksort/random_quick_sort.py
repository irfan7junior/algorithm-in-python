from typing import TypeVar, List
import random
from .quick_sort import partition

T = TypeVar('T', str, float, int)


def randomized_partition(array: List[T], p: int, r: int) -> int:
  rand_value = random.randint(p, r)
  array[rand_value], array[r] = array[r], array[rand_value]
  return partition(array, p, r)


def quick_sort(array: List[T], p: int, r: int) -> None:
  if p < r:
    q = randomized_partition(array, p, r)
    quick_sort(array, p, q - 1)
    quick_sort(array, q + 1, r)
