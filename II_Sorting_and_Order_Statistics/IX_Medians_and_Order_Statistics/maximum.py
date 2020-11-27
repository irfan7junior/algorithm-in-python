from typing import List, TypeVar


T = TypeVar('T', int, float, str)


def maximum(array: List[T]) -> int:
  max_el = array[0]
  for i in range(2, len(array)):
    if max_el < array[i]:
      max_el = array[i]
  return max_el
