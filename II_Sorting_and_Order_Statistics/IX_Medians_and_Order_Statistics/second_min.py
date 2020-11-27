from typing import List, TypeVar


T = TypeVar('T', float, int, str)


def second_min(array: List[T]) -> int:
  first_min = array[0]
  second_min = float('inf')
  for i in range(1, len(array)):
    if array[i] < second_min:
      if array[i] < first_min:
        first_min, second_min = array[i], first_min
      else:
        second_min = array[i]
  return second_min
