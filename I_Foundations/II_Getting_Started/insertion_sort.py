from typing import TypeVar, List

T = TypeVar('T', int, str, float)


def insertion_sort(array: List[T]) -> None:
  "Insertion Sort"
  for i in range(0, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
      array[j+1] = array[j]
      j -= 1
    array[j+1] = key


if __name__ == '__main__':
  array = [1, 2, 3, 9, 8, 5, 4]
  insertion_sort(array)
  print(array)
