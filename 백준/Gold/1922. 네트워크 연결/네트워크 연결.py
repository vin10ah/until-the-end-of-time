N = int(input())
M = int(input())

edges = []

for _ in range(M):
    edges.append(tuple(map(int,input().split())))

edges.sort(key=lambda x: x[2])


p_s = list(range(N+1))

def find_p(idx):
    if p_s[idx]==idx:
        return idx
    p_s[idx]=find_p(p_s[idx])
    return p_s[idx]

def union(u,v):
    u_root = find_p(u)
    v_root = find_p(v)
    if u_root > v_root:
        p_s[v_root] = u_root
    else:
        p_s[u_root] = v_root

total_cost = 0

for edge in edges:
    u, v, w = edge
    if find_p(u) != find_p(v):
        total_cost += w
        union(u, v)

print(total_cost)