from typing import TypeVar, List

T = TypeVar('T', int, str, float)


def linear_search(array: List[T], key: T) -> int:
  for i in range(len(array)):
    if array[i] == key:
      return i
  return -1
