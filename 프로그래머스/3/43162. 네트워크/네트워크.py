# def solution(n, computers):
#     net = 0
  
#     for i in range(n):
#         computers[i][i] = 1
        
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j] == 1:
#                 net += 1
                
#     return 

def solution(n, computers):
    
    visited = [1]*n #네트워크 연결 확인 전 1, 확인 후 0
    
    def con_idx(idx):
        result = []
        for jdx, conn in enumerate(computers[idx]):
            if idx!=jdx and conn==1:
                result.append(jdx)
        return result
                
    def dfs(idx):
        visited[idx]=0
        for n_idx in con_idx(idx):
            if visited[n_idx]==1:
                dfs(n_idx)
        
    answer = 0
    
    for idx in range(n):
        if visited[idx]==1:
            dfs(idx)
            answer += 1
    
    return answer
