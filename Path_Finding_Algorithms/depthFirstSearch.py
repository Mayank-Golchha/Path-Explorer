# DFS algorithm
# Depth-First Search (DFS) is an algorithm used to traverse or
# search a graph or tree data structure by exploring as far as possible along each branch before backtracking.
# this algorithm tries to find all possible paths and whichever path is the correct
# will be returned
# note : this algorithm will not necessarily find the shortest path
class PathFinder:
    def __init__(self,graph,start,end):
        self.graph = graph
        self.length = len(graph)
        self.start = start
        self.end = end
        self.path = []
        self.discovered = []    #so that we don't move on the same path again

    def availablePaths(self,index):
        # will find the different nodes the algorithm can go at a given index
        return [i for i in range(self.length) if self.graph[index][i] and i != index]

    def discover(self,current,end):
        # will find all possible paths
        if current == end:
            # if a node is equal to the end node then it is the correct path
            # note : a correct path is not necessarily the shortest path
            self.discovered.append(current)
            self.path.append(current)
            return 1
        moves = self.availablePaths(current)
        self.discovered.append(current)

        for m in moves:
            if m not in self.discovered and self.discover(m, end):
                self.path.append(current)
                self.discovered.append(m)
                return 1

        return 0

    def Find(self):
        if self.discover(self.start,self.end):
            return self.path
        return []

