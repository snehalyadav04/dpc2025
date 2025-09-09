def has_cycle(V, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

test_cases = [
    (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]),
    (3, [[0, 1], [1, 2]]),
    (4, [[0, 1], [1, 2], [2, 0]])
]

for idx, (V, edges) in enumerate(test_cases, 1):
    result = has_cycle(V, edges)
    print(f"Input : V = {V}, Edges = {edges}")
    print(f"Output: {str(result).lower()}\n")
