from collections import defaultdict, deque

def shortest_path_length(V, edges, start, end):
    if start == end:
        return 0

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  

    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)

    while queue:
        current, distance = queue.popleft()
        for neighbor in graph[current]:
            if neighbor == end:
                return distance + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

#Test Case 1
print("Test Cases:")
V = 5
Edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4
print("1. Input:")
print("V =", V)
print("Edges =", Edges)
print("start =", start)
print("end =", end)
print("Output:", shortest_path_length(V, Edges, start, end))  
print()

#Test Case 2
V = 3
Edges = [[0, 1], [1, 2]]
start = 0
end = 2
print("2. Input:")
print("V =", V)
print("Edges =", Edges)
print("start =", start)
print("end =", end)
print("Output:", shortest_path_length(V, Edges, start, end))  
print()

#Test Case 3
V = 4
Edges = [[0, 1], [1, 2]]
start = 2
end = 3
print("3. Input:")
print("V =", V)
print("Edges =", Edges)
print("start =", start)
print("end =", end)
print("Output:", shortest_path_length(V, Edges, start, end))  
