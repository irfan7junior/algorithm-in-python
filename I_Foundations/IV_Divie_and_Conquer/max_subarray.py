from typing import Tuple, TypeVar, List, NewType

T = TypeVar('T', str, float, int)
ReturnType = NewType('ReturnType', Tuple[int, int, int])


def find_max_crossing_subarray(array: List[T], low: int, mid: int, high: int) -> ReturnType:
  left_sum = -float('inf')
  sum = 0
  max_left = None
  for i in range(mid, low - 1, -1):
    sum = sum + array[i]
    if sum > left_sum:
      left_sum = sum
      max_left = i

  right_sum = -float('inf')
  sum = 0
  max_right = None
  for j in range(mid + 1, high + 1):
    sum = sum + array[j]
    if sum > right_sum:
      right_sum = sum
      max_right = j

  return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(array: List[T], low: int, high: int) -> ReturnType:
  if high == low:
    return [low, high, array[low]]
  mid = (low + high) // 2
  [left_low, left_high, left_sum] = find_max_subarray(array, low, mid)
  [right_low, right_high, right_sum] = find_max_subarray(array, mid + 1, high)
  [cross_low, cross_high, cross_sum] = find_max_crossing_subarray(
      array, low, mid, high)

  if left_sum >= right_sum and left_sum >= cross_sum:
    return [left_low, left_high, left_sum]
  elif right_sum >= left_sum and right_sum >= cross_sum:
    return [right_low, right_high, right_sum]
  else:
    return [cross_low, cross_high, cross_sum]
