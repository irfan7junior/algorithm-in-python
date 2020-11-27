from typing import TypeVar, List, Generic
from .heap import Heap

T = TypeVar('T', str, int, float)


class Priority_Queue(Generic[T]):
  def __init__(self, array: List[T]) -> None:
    self.heap = Heap(array)
    self.heap.build_max_heap()

  def heap_maximum(self) -> T:
    return self.heap.items[0]

  def extract_max(self) -> T:
    if self.heap.heap_size < 0:
      raise IndexError('already empty heap')
    max = self.heap.items[0]
    self.heap.items[0] = self.heap.items[self.heap.heap_size - 1]
    self.heap.heap_size -= 1
    self.heap.items.pop()
    self.heap.max_heapify(0)
    return max

  def heap_increase_key(self, index: int, key: int) -> None:
    if key < self.heap.items[index]:
      raise Exception('new key is smaller than the current key')
    self.heap.items[index] = key
    while index > 0 and self.heap.items[self.heap.parent(index)] < self.heap.items[index]:
      self.heap.items[self.heap.parent(
          index)], self.heap.items[index] = self.heap.items[index], self.heap.items[self.heap.parent(index)]
      index = self.heap.parent(index)

  def max_heap_insert(self, key: int) -> None:
    self.heap.heap_size += 1
    self.heap.items.append(-float('inf'))
    self.heap_increase_key(self.heap.heap_size - 1, key)
