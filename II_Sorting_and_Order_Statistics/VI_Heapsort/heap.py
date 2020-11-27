from typing import TypeVar, Generic, List

T = TypeVar('T')


class Heap(Generic[T]):
  def __init__(self, array: List[T] = []) -> None:
    self.items = array
    self.heap_size = 0

  def parent(self, index: int) -> int:
    if index < 0:
      raise IndexError('index out of range')

    answer = (index - 1) // 2
    if answer >= len(self.items):
      raise IndexError('index out of range')

    return answer

  def left(self, index: int) -> int:
    answer = 2 * index + 1
    if answer < 0:
      raise IndexError('index out of range')
    return answer

  def right(self, index: int) -> int:
    answer = 2 * index + 2
    if answer < 0:
      raise IndexError("index out of range")
    return answer

  def max_heapify(self, index: int) -> None:
    l = self.left(index)
    r = self.right(index)
    largest: int = None
    if l < self.heap_size and self.items[l] > self.items[index]:
      largest = l
    else:
      largest = index

    if r < self.heap_size and self.items[r] > self.items[largest]:
      largest = r

    if largest != index:
      self.items[index], self.items[largest] = self.items[largest], self.items[index]
      self.max_heapify(largest)

  def build_max_heap(self):
    self.heap_size = len(self.items)
    for i in range((self.heap_size - 1) // 2, -1, -1):
      self.max_heapify(i)


if __name__ == '__main__':
  heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 4, 1])
  print(len(heap.items))
  heap.build_max_heap()
  print(heap.items)
