from typing import List, TypeVar


T = TypeVar('T')


class Stack:
  def __init__(self, capacity: int) -> None:
    self.items = [None for i in range(capacity)]
    self.top = -1
    self.capacity = capacity

  def stack_empty(self) -> bool:
    if self.top == -1:
      return True
    return False

  def push(self, item: T) -> None:
    if self.top + 1 == self.capacity:
      raise OverflowError('Overflow')
    self.top += 1
    self.items[self.top] = item

  def pop(self) -> T:
    if self.stack_empty():
      raise Exception('Underflow Exception')
    self.top -= 1
    return self.items[self.top + 1]

  def __repr__(self) -> str:
    return self.items.__repr__()
