import sys

class Graph:
    """Class to represent weighted, non-directed graph.
    
    Attributes:
        V : int 
            vertex count
        graph : list 
            edges and weights
    
    Methods:
        add(u, v, w, label):
            Adds an edge to the graph
        def find(parent, i):
        def union(parent, rank, x, y):
        def union(parent, rank, x, y):
        def kruskal(self):    
    """
    def __init__(self, vertices):
        """Initializes Graph with vertex count and empty list."""
        self.V = vertices
        self.graph = []

    def add(self, u, v, w, label):
        """Adds an edge to the graph"""
        self.graph.append([u, v, w, label])

    # Recursive implementation of union-find/disjoint-set data structure
    def find(self, parent, i):
        """Determines which subset a given element belongs to"""
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """Joins two subsets into one subset"""
        xset = self.find(parent, x)
        yset = self.find(parent, y)

        if rank[xset] < rank[yset]:
            parent[xset] = yset
        elif rank[xset] > rank[yset]:
            parent[yset] = xset
        else:
            parent[yset] = xset
            rank[xset] += 1

    # Main function to create MWST from Kruskal's algorithm
    def kruskal(self):

        result = [] #MWST

        i, e, total = 0, 0, 0  #Edge index, MWST edge index, total weight

        # Sort edges by increasing weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # Create V subsets with single elements
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)

        # E(G) = V(G)-1
        while e < self.V - 1:

            # Pick smallest edge
            u, v, w, label = self.graph[i]
            i = i + 1
            x = self.find(parent, u-1)
            y = self.find(parent, v-1)

            if x != y:
                e = e + 1
                result.append([u, v, w, label])
                self.union(parent, rank, x, y)

        with open("output.txt", "w") as outFile:
            for u, v, weight, lab in result:
                total += weight
                outFile.write("{3:>4}: ({0:1}, {1:1}) {2:.1f}\n".format(u, v, weight, lab))
            outFile.write("Total Weight = %0.2f" % total)

def main():
    with open("points.txt", "r") as file:
        graph = Graph(int(file.readline()))
        edgeCount = int(file.readline())
        for label, edge in enumerate(file, start=1):
            v1, v2, weight = map(int, edge.split())
            graph.add(v1, v2, weight, label)
        graph.kruskal()      

if __name__ == '__main__':
    main()