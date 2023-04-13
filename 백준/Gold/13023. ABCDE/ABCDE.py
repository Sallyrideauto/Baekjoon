def dfs(graph, start, depth, visited):
    if depth == 4:
        return True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            visited[neighbor] = True
            if dfs(graph, neighbor, depth + 1, visited):
                return True
            visited[neighbor] = False

    return False


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = 0
    for i in range(n):
        visited = [False] * n
        visited[i] = True
        if dfs(graph, i, 0, visited):
            result = 1
            break

    print(result)


if __name__ == "__main__":
    main()
