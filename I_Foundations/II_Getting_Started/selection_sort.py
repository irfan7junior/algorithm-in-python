from typing import TypeVar, List

T = TypeVar('T', int, float, str)


def selection_sort(array: List[T]) -> None:
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    if i != min_index:
      array[i], array[min_index] = array[min_index], array[i]
