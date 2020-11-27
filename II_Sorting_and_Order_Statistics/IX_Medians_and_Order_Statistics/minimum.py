from typing import List, TypeVar

T = TypeVar('T', int, float, str)


def minimum(array: List[T]) -> int:
  min_el = array[0]
  for i in range(1, len(array)):
    if min_el > array[i]:
      min_el = array[i]
  return min_el
