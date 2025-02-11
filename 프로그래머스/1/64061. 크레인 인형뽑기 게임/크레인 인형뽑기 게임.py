def solution(board, moves):
    bag = []
    score = 0
    
    for move in moves:
        m = move-1
        for i in range(len(board)):
            if board[i][m] == 0:
                continue
            else:
                if bag and bag[-1] == board[i][m]:
                    board[i][m] = 0
                    bag.pop()
                    score += 2
                    break
                else:
                    bag.append(board[i][m])
                    board[i][m] = 0
                    break

    return score
    
    
    
    
    


