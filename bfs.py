#Breadth-First Search or Depth-First Search
from collections import deque

bfs_graph = {
    'A': ['B', 'E'],
    'B': ['A', 'F', 'I', 'J'],
    'C': ['D', 'E'],
    'D': ['C', 'F'],
    'E': ['A','C','H'],
    'F': ['B', 'D', 'H'],
    'G': ['H', 'I', 'J'],
    'H': ['E', 'F', 'G', 'J'],
    'I': ['B', 'G', 'J'],
    'J': ['B', 'G', 'H', 'I']
}

matrix_bfs = [
    #A,B,C,D,E,F,G,H,I,J
    [0,1,0,0,1,0,0,0,0,0],   #A
    [1,0,0,0,0,1,0,0,1,1],   #B
    [0,0,0,1,1,0,0,0,0,0],   #C
    [0,0,1,0,0,1,0,0,0,0],   #D
    [1,0,1,0,0,0,0,1,0,0],   #E
    [0,1,0,0,1,0,0,0,0,0],   #F
    [0,1,0,0,1,0,0,0,0,0],   #G
    [0,1,0,0,1,0,0,0,0,0],   #H
    [0,1,0,0,1,0,0,0,0,0],   #I
    [0,1,0,0,1,0,0,0,0,0],   #J
]

def bfs(bfs_graph, start, goal):
    queue = deque([[start]])
    visited = set()


    #discovery time tracker
    discovery_time = {}
    time = 0

    print("\n === BFS TRACE ===")

    while queue:
        print("\n=====================")
        print(f"Queue:{[' -> '.join(p) for p in queue]}")
        print(f"Visited: {visited}")

        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            #record discovery time
            time += 1
            discovery_time[node] = time

            print(f"\nVisit: {node}")
            print(f"Current Path: {' -> '.join(path)}")
            print(f"Discovery time of {node}:{time}")

            if node == goal:
                print("\n--- RESULT ---")
                print(f"Shortest path: {' -> '.join(path)}")
                print(f"Stops:{len(path)-1}")
                break

            for neighbor in bfs_graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)
                    print(f"Enqueue: {'->'.join(new_path)}")

    print("\n--- DISCOVERY TIMES ---")
    for v in discovery_time:
        print(f"{v}: {discovery_time[v]}")

#test
bfs(bfs_graph, 'G', 'A')