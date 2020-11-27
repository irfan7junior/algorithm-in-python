from typing import List


def counting_sort(A: List[int], exp: int) -> None:
  k = 9

  # Temporary Output storage
  B: List[int] = [None for x in A]

  # Initializing Count to zero
  Count: List[int] = [0 for i in range(k + 1)]

  # Change Count so that it contains the number of occurence of a digit
  for i in range(len(A)):
    index = (A[i] // exp) % 10
    Count[index] += 1

  # Modifying Count so that it contains the position of a particular digit
  for i in range(1, k + 1):
    Count[i] += Count[i - 1]

  for i in range(len(A) - 1, -1, -1):
    index = (A[i] // exp) % 10
    B[Count[index] - 1] = A[i]
    Count[index] -= 1

  for i in range(len(A)):
    A[i] = B[i]
