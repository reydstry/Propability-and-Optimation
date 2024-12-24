from collections import defaultdict
import heapq
from prettytable import PrettyTable

INFINITY = float('inf')

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
        self.nodes = set()

    def add_vertex(self, name, edges):
        self.graph[name] = edges
        self.nodes.update([name] + list(self.graph[name].keys()))

    def dijkstra(self, src):
        distances = {node: INFINITY for node in self.nodes}
        predecessors = {node: None for node in self.nodes}
        distances[src] = 0
        pq = [(0, src)]  # Priority queue (distance, node)
        visited = set()

        # Buat tabel dengan PrettyTable
        nodes_sorted = sorted(self.nodes)
        table = PrettyTable()
        table.field_names = ["Step"] + nodes_sorted

        step = 1

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)

            # Tambahkan langkah ke tabel
            self.print_step(step, distances, nodes_sorted, table)
            step += 1

            for neighbor, weight in self.graph[current_node].items():
                alt_distance = current_distance + weight
                if alt_distance < distances[neighbor]:
                    distances[neighbor] = alt_distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (alt_distance, neighbor))

        # Tampilkan tabel
        self.print_step(step, distances, nodes_sorted, table)
        print(table)

        # Menampilkan jarak terpendek
        self.print_shortest_distances(src, distances, predecessors)

    def print_step(self, step, distances, nodes_sorted, table):
        tr = '\u221e'
        row = [f"{distances[node]:<3}" if distances[node] < INFINITY else tr for node in nodes_sorted]
        table.add_row([step] + row)

    def print_shortest_distances(self, src, distances, predecessors):
        print("\nShortest distances and paths:")
        for node in sorted(self.nodes):
            if distances[node] < INFINITY and node != src:
                print(f"Shortest distance from {src} to {node}: {distances[node]}")
                path = []
                current = node
                while current:
                    path.append(current)
                    current = predecessors[current]
                path.reverse()
                print(" -> ".join(path))
            elif distances[node] == INFINITY:
                print(f"{node} is unreachable from {src}.")


# Membuat instance graf
g = Graph()
g.add_vertex('v1', {'v2': 7, 'v3': 13})
g.add_vertex('v2', {'v3': 4, 'v4': 8})
g.add_vertex('v3', {'v2': 5, 'v4': 3, 'v5': 8})
g.add_vertex('v4', {'v2': 7, 'v3': 5, 'v5': 2})

# Menjalankan algoritma Dijkstra dari node v1
g.dijkstra('v1')
