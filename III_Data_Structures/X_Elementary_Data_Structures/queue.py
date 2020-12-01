from typing import TypeVar


T = TypeVar('T')


class Queue:
  def __init__(self, capacity: int):
    self.items = [None for i in range(capacity)]
    self.head = 0
    self.tail = 0
    self.capacity = capacity

  def is_empty(self):
    if self.head == self.tail:
      return True
    return False

  def is_full(self):
    if self.head == self.tail + 1:
      return True
    if self.head == 0 and self.tail == self.capacity - 1:
      return True
    return False

  def enqueue(self, item: T) -> None:
    if self.is_full():
      raise OverflowError('Queue is full')
    self.items[self.tail] = item
    if self.tail == self.capacity - 1:
      self.tail = 0
    else:
      self.tail += 1

  def dequeue(self) -> T:
    if self.is_empty():
      raise Exception('Queue is empty')
    x = self.items[self.head]
    self.items[self.head] = None
    if self.head == self.capacity + 1:
      self.head = 0
    else:
      self.head += 1
    return x

  def __repr__(self) -> str:
    return self.items.__repr__()
