'''
we implement bfs and dfs
'''

import numpy as np


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class QueuedLinked:
    def __init__(self) -> None:
        self._front = None
        self._rare = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rare._next = newest
        self._rare = newest
        self._size += 1

    def dequeue(self):
        '''
        This method take O(1) to take out the element.
        '''
        if self.is_empty():
            print('Queue is Empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rare = None
        return e

    def first(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end='<--')
            p = p._next
        print()


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))  # rows, cloumns
        self._dfs_visited = [0] * self._vertices

    def insert_edge(self, u, v, weight=1):
        self._adjMat[u][v] = weight

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, '--', j)

    def outdrgree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count += 1
        return count

    def display_adjMat(self):
        print(self._adjMat)

    def BFS(self, s):
        i = s
        q = QueuedLinked()
        visited = [0] * self._vertices
        print(i, end=' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end=' ')
                    visited[j] = 1
                    q.enqueue(j)

    def DFS(self, s):
        if self._dfs_visited[s] == 0:
            # means the vetex is not vistied
            print(s, end=' ')
            self._dfs_visited[s] = 1
            for j in range(self._vertices):
                if self._adjMat[s][j] == 1 and self._dfs_visited[j] == 0:
                    self.DFS(j)


G = Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)
print('Edges:')
G.edges()
print('BFS:')
G.BFS(0)
print('DFS:')
G.DFS(0)
