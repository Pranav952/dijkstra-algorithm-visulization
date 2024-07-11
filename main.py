import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, V: int):  
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.edges = []
        
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.edges.append((u, v, w))


    def shortestPath(self, src: int):

        pq = []
        heapq.heappush(pq, (0, src))

        dist = [float('inf')] * self.V
        dist[src] = 0

        prev = [None] * self.V

        while pq:

            d, u = heapq.heappop(pq)

 
            for v, weight in self.adj[u]:

                if dist[v] > dist[u] + weight:

                    dist[v] = dist[u] + weight
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))


        return dist, prev


    def reconstruct_path(self, prev, src, dest):
        path = []
        while dest is not None:
            path.append(dest)
            dest = prev[dest]
        path.reverse()
        if path[0] == src:
            return path
        else:
            return []

    def visualize(self, src: int, dest: int, pos):
        G = nx.Graph()  
        for u, v, w in self.edges:
            G.add_edge(u, v, weight=w)

        edge_labels = {(u, v): w for u, v, w in self.edges}

        dist, prev = self.shortestPath(src)
        shortest_path = self.reconstruct_path(prev, src, dest)

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        if shortest_path:
            path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

        plt.title(f"Shortest Path from Node {src} to Node {dest}")
        plt.show()

if __name__ == "__main__":

    V = 9
    g = Graph(V)


    g.addEdge(0, 1, 2)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 1)
    g.addEdge(2, 6, 3)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)


    pos = {
        0: (0, 0), 
        1: (1, 2), 
        2: (3, 2), 
        3: (5, 2), 
        4: (7, 2), 
        5: (5, 0), 
        6: (3, 0), 
        7: (1, 0), 
        8: (3, -2)
    }


    g.visualize(0, 5, pos)

