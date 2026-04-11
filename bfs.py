#Breadth-First Search or Depth-First Search
from collections import deque
from data import location_names


class TransportGraph:

    def __init__(self):
        # Adjacency List
        self.graph = {
            'A': ['B', 'E'],
            'B': ['A', 'F', 'I', 'J'],
            'C': ['D', 'E'],
            'D': ['C', 'F'],
            'E': ['A', 'C', 'H'],
            'F': ['B', 'D', 'H'],
            'G': ['H', 'I', 'J'],
            'H': ['E', 'F', 'G', 'J'],
            'I': ['B', 'G', 'J'],
            'J': ['B', 'G', 'H', 'I']
        }

        # Adjacency Matrix (for representation only)
        self.matrix = [
            [0,1,0,0,1,0,0,0,0,0],
            [1,0,0,0,0,1,0,0,1,1],
            [0,0,0,1,1,0,0,0,0,0],
            [0,0,1,0,0,1,0,0,0,0],
            [1,0,1,0,0,0,0,1,0,0],
            [0,1,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1],
            [0,1,0,0,1,0,0,0,0,0],
            [0,1,0,0,1,0,0,0,0,0],
            [0,1,0,0,1,0,0,0,0,0]
        ]

    def bfs(self, start, goal):
        queue = deque([[start]])
        visited = set()

        discovery_time = {}
        time = 0

        print("\n=== BFS TRACE ===")

        while queue:

            print("\n----------------------------")
            print("Queue:", [" -> ".join(location_names[n] for n in p) for p in queue])
            print("Visited:", [location_names[v] for v in visited])

            path = queue.popleft()
            node = path[-1]

            if node not in visited:
                visited.add(node)

                time += 1
                discovery_time[node] = time

                print(f"\nVisit: {location_names[node]}")
                print("Path:",
                      " -> ".join(location_names[n] for n in path))
                print(f"Discovery Time: {time}")

                if node == goal:
                    print("\n=== RESULT ===")
                    print("Shortest Path:",
                          " -> ".join(location_names[n] for n in path))
                    print(f"Stops: {len(path) - 1}")
                    return

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        queue.append(new_path)
                        print(f"Enqueue: {' -> '.join(location_names[n] for n in new_path)}")

        print("\nNo path found.")

        print("\n--- DISCOVERY TIMES ---")
        for v in discovery_time:
            print(f"{location_names[v]}: {discovery_time[v]}")