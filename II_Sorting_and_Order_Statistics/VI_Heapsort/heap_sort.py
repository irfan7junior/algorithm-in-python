from typing import TypeVar, List
from .heap import Heap
import sys


T = TypeVar('T', str, int, float)


def heap_sort(array: List[T]) -> None:
  """
  heap sort algorithm using heap functionality defined
  in a different file.
  """
  heap = Heap(array)
  heap.build_max_heap()
  for _ in range(len(heap.items) - 1, 0, -1):
    heap.items[heap.heap_size -
               1], heap.items[0] = heap.items[0], heap.items[heap.heap_size - 1]
    heap.heap_size -= 1
    heap.max_heapify(0)
