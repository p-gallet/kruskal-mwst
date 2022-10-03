import sys

# Class to represent weighted, non-directed graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add(self, u, v, w, label):
        self.graph.append([u, v, w, label])

    # Recursive implementation of union-find/disjoint-set data structure
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
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

        result = []  # MWST

        i = 0  # Edge index
        e = 0  # MWST edge index
        total = 0  # Total weight

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

        for u, v, weight, lab in result:
            total += weight
            f1.write("{3:>4}: ({0:1}, {1:1}) {2:.1f}\n".format(u, v, weight, lab))

        f1.write("Total Weight = %0.2f" % total)


f = open(sys.argv[1], "r")
f1 = open(sys.argv[2], "w")

g = Graph(int(f.readline()))
f.readline()
lb = 1

for line in f:
    a, b, c = map(int, line.split())
    g.add(a, b, c, lb)
    lb += 1

g.kruskal()
f.close()
f1.close()
