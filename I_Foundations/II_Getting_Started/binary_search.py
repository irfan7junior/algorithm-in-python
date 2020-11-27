from typing import TypeVar, List

T = TypeVar('T', int, float, str)


def binary_search(array: List[T], key: T) -> int:
  low = 0
  high = len(array) - 1
  mid = (low + high) // 2
  while low <= high:
    if array[mid] == key:
      return mid
    elif key < array[mid]:
      high = mid - 1
      mid = (low + high) // 2
    else:
      low = mid + 1
      mid = (low + high) // 2
  return -1
