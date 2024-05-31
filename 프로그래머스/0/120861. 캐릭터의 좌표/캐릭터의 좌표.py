# def solution(keyinput, board):
#     answer = [0, 0]
#     keys = {'up':1, 'down':-1, 'left':-1, 'right':1}
    
#     for key in keyinput:
#         if key == 'up' or key == 'down':
#             if abs(answer[1]) < board[1]//2:
#                 answer[1] += keys[key]
#         else:
#             if abs(answer[0]) < board[0]//2:
#                 answer[0] += keys[key]
    
#     return answer

def solution(keyinput, board):
    answer = [0, 0]
    keys = {'up':(0,1), 'down':(0,-1), 'left':(-1,0), 'right':(1,0)}
    
    for key in keyinput:
        x, y = keys[key]
        new_x = answer[0] + x
        new_y = answer[1] + y
        
        if abs(new_x) <= board[0]//2:
            answer[0] = new_x
        if abs(new_y) <= board[1]//2:
            answer[1] = new_y
    
    return answer
    