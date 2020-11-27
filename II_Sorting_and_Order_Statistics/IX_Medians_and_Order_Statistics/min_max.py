from typing import List, Tuple, TypeVar


T = TypeVar('T', int, float, str)


def min_max(array: List[T]) -> Tuple[int, int]:
  isOdd: bool = len(array) % 2

  min_el = float('inf')
  max_el = -float('inf')

  if isOdd:
    min_el = array[0]
    max_el = array[0]
  else:
    if array[0] < array[1]:
      min_el = array[0]
      max_el = array[1]
    else:
      min_el = array[1]
      max_el = array[0]

  start_index = 1 if isOdd else 2

  for i in range(start_index, len(array), 2):
    if array[i] < array[i+1]:
      if min_el > array[i]:
        min_el = array[i]
      if max_el < array[i+1]:
        max_el = array[i+1]
    else:
      if min_el > array[i+1]:
        min_el = array[i+1]
      if max_el < array[i]:
        max_el = array[i]
  return [min_el, max_el]
