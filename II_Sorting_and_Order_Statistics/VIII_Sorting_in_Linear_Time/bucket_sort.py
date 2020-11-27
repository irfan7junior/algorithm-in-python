from CLRS.I_Foundations.II_Getting_Started.insertion_sort import insertion_sort
from typing import List
import math


def count_len(num: int) -> int:
  # It will return the number of digits in the integer
  count = 0
  while num > 0:
    count += 1
    num = num // 10
  return count


def bucket_sort(array: List[int]) -> None:
  # getting the length of the max element in the array
  length = count_len(max(array))

  # converting all the values of the array in to floats
  A: List[float] = [(x/(10**length)) for x in array]

  # creating the list of list of floats
  B: List[List[float]] = [[] for _ in range(len(array))]

  # filling in the values in list of list of floats
  for i in range(len(A)):
    B[math.floor(A[i] * len(A))].append(A[i])

  # sorting each list in the list of list of floats using insertion sort
  for i in range(len(B)):
    insertion_sort(B[i])

  # storing back all the values from B to A
  k = 0
  for i in range(len(B)):
    for j in range(len(B[i])):
      array[k] = int(B[i][j] * (10**length))
      k += 1
