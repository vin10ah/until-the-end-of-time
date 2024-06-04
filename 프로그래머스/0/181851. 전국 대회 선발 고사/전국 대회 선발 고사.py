def solution(rank, attendance):
    answer = 0
    real = {}
    for i in range(len(rank)):
        if attendance[i] == True:
            real[i] = rank[i]
    real = sorted(real.items(), key= lambda item:item[1])
    
    # rank = [i for i in real.values()]
    
    return real