from typing import TypeVar


T = TypeVar('T')


class Node:
  def __init__(self, key: T) -> None:
    self.key = key
    self.next: Node = None
    self.prev: Node = None


class LinkedList:
  def __init__(self) -> None:
    self.head: Node = None

  def search(self, key: T) -> Node:
    x: Node = self.head
    while x is not None and x.key != key:
      x = x.next
    return x

  def insert(self, node: Node) -> None:
    node.next = self.head
    if self.head is not None:
      self.head.prev = node
    self.head = node

  def delete(self, node: Node) -> None:
    if node.prev is not None:
      node.prev.next = node.next
    else:
      self.head = node.next
    if node.next is not None:
      node.next.prev = node.prev

  def __repr__(self) -> str:
    x: Node = self.head
    answer = []
    while x is not None:
      answer.append(x.key)
      x = x.next
    answer.append(None)
    return '->'.join(map(str, answer))
