# Use dictionary to store adjacency details
# Using adjacency list
from collections import defaultdict

class Graph:
  def __init__(self, root, adj_list=None):
    self.adj_list = defaultdict(list)
    self.root = root
    self.adj_list[root]

  def vertices(self):
    return self.adj_list.keys()

  def edges(self):
    list_tup = []
    # return all tuples
    for vert in self.adj_list.keys():
      for edge in self.adj_list[vert]:
        list_tup.append((vert, edge))

    return list_tup

  def add_edge(self, src, dest):
    self.adj_list[src].append(dest)
    #print(self.adj_list[src])
    return self.adj_list[src]

  def BFS(self):
    #print(max(self.adj_list.values()))
    visited = [ False] * (max(self.adj_list.values())[0] + 1) # index corresponds to vert number. Maxi vert number
    #print(visited)
    queue = []

    queue.append(self.root)
    visited[self.root] = True

    while queue:
      elem = queue.pop(0)
      print (str(elem) + " ")
      for i in self.adj_list[elem]:
        #print(visited[i])
        if visited[i] == False:
          queue.append(i)
          visited[i] = True

  def DFS(self, leaf, visited):

    if leaf == None:
      return

    if visited[leaf] == False:
      print(leaf)
      visited[leaf] = True

    for neighbour in self.adj_list[leaf]:
      self.DFS(neighbour, visited)

  # Route Between Nodes: Given a directed graph, design an algorithm
  # to find out whether there is a route between two nodes.


  def route_btwn_nodes_bfs(self, node1, node2):
    visited = [False] * (max(self.adj_list.values())[0] + 1)

    queue = []
    queue.append(node1)
    visited[node1] = True
    while queue:
      elem = queue.pop(0)

      if elem == node2:
        return True # Base case
      for child in self.adj_list[elem]:
        queue.append(child)
        visited[child] = True

    return False


  def route_btwn_nodes_dfs(self, node1, node2, visited):
    # Start at node1
    # Check if any of theh children has the node recursively
    # return true if any of the node val = node2
    # Else return False

    if node1 == None:
      return
    print(node1, node2)

    if node1 == node2:
      return True
    else:
      if visited[node1] == False:
        for child in self.adj_list[node1]:
          visited[child] = True
          self.route_btwn_nodes_dfs(child, node2, visited)
    return False


if __name__ == "__main__":
  graph = Graph(root=0, adj_list = [1])
  graph.add_edge(0, 1)
  graph.add_edge(0, 3)
  graph.add_edge(1, 2)
  graph.add_edge(1, 4)
  graph.add_edge(2, 5)
  graph.add_edge(2, 6)
  graph.add_edge(3, 7)
  graph.add_edge(4, 8)

  '''
       0
      / \
     1   3
    / \   \
   2   4   7
  / \   \
 5   6   8

 DFS: 0 - 1 - 2 - 5 - 6 - 4 - 8 - 3 - 7
 BFS: 0 - 1 - 3 - 2 - 4 - 7 - 5 - 6 - 8
  '''
  #graph.vertices()
  #graph.edges()

  #print("BFS:")
  #graph.BFS()

  #print("DFS:")
  visited = [ False] * (max(graph.adj_list.values())[0] + 1)
  #graph.DFS(graph.root, visited)

  print(graph.route_btwn_nodes_dfs(0, 7, visited))
