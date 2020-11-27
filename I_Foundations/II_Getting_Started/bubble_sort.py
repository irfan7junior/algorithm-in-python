from typing import TypeVar, List

T = TypeVar('T', int, float, str)


def bubble_sort(array: List[T]) -> None:
  for i in range(len(array) - 1):
    for j in range(len(array) - 1, i, -1):
      if array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
