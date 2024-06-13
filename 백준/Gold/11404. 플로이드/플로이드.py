N = int(input())
M = int(input())

graph = []

for _ in range(N):
    graph.append([float('inf')]*N)

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i_s in graph:
    for i in i_s:
        if i==float('inf'):
            print(0, end=' ')
        else:
            print(i, end=' ')
    print()