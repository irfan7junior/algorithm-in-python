from typing import Dict, Literal, Set, TypeVar

Color = Literal['white', 'black', 'gray']


class Vertex(object):

  def __init__(self, key, color: Color = 'white', parent=None, distance: int = None):
    self.key: str = key
    self.neighbors: Set[(Vertex, int)] = set()
    self.color: Color = color
    self.parent: Vertex = parent
    self.distance: int = distance

  def add_neighbor(self, vertex, weight=None):
    if isinstance(vertex, str):
      new_vertex = Vertex(vertex)
      self.neighbors.add((new_vertex, weight))
    elif isinstance(vertex, Vertex):
      self.neighbors.add((vertex, weight))
    else:
      raise Exception('Invalid vertex provided')

  def get_neighbors(self):
    return self.neighbors

  def __repr__(self):
    key_str = f'key: {self.key}'
    neighbor_str = str(
        [f'{vertex.key}({weight})' for (vertex, weight) in self.neighbors])
    return f'({key_str} => {neighbor_str})'


class Graph(object):

  def __init__(self, by=False):
    self.vertices: Dict[Vertex] = dict()
    self.bidirectional = by

  def add_edge(self, source, destination, weight=None):
    if isinstance(source, str) and isinstance(destination, str):
      if source in self.vertices:
        source = self.vertices[source]
      else:
        source = Vertex(source)
        self.vertices[source.key] = source
      if destination in self.vertices:
        destination = self.vertices[destination]
      else:
        destination = Vertex(destination)
        self.vertices[destination.key] = destination

    if isinstance(source, Vertex) and isinstance(destination, Vertex):
      source.add_neighbor(destination, weight)
      if self.bidirectional:
        destination.add_neighbor(source, weight)
    else:
      raise Exception('Wrong source and destination type')

  def __repr__(self):
    result = ''
    for _key, vertex in self.vertices.items():
      result += str(vertex) + '\n'
    return result


if __name__ == '__main__':
  graph = Graph(True)
  graph.add_edge('1', '2', 4)
  graph.add_edge('1', '5', 4)
  graph.add_edge('2', '5', 4)
  graph.add_edge('2', '4', 4)
  graph.add_edge('5', '4', 4)
  graph.add_edge('2', '3', 4)
  graph.add_edge('2', '4', 4)
  graph.add_edge('4', '3', 4)
  print(graph)
