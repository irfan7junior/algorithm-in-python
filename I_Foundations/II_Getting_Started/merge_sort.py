from typing import TypeVar, List

T = TypeVar('T', str, int, float)


def merge(array: List[T], p: int, q: int, r: int) -> None:
  n1 = q - p + 1
  n2 = r - q

  L = [array[p + i] for i in range(n1)]
  R = [array[q + i + 1] for i in range(n2)]

  L.append(float('inf'))
  R.append(float('inf'))

  i = 0
  j = 0

  for k in range(p, r + 1):
    if L[i] < R[j]:
      array[k] = L[i]
      i += 1
    else:
      array[k] = R[j]
      j += 1


def merge_sort(array: List[T], low: int, high: int) -> None:
  if low < high:
    mid = (low + high) // 2
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)
    merge(array, low, mid, high)
