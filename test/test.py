import random

def ai_transform_rotate(trial_board):
    all_rotated_boards=[]
    temp_board=trial_board[:]
    for _ in range(3):
        rotated_board=trial_board[:]
        rotated_board[0]=temp_board[6]
        rotated_board[1]=temp_board[3]
        rotated_board[2]=temp_board[0]
        rotated_board[3]=temp_board[7]
        rotated_board[5]=temp_board[1]
        rotated_board[6]=temp_board[8]
        rotated_board[7]=temp_board[5]
        rotated_board[8]=temp_board[2]
        temp_board=rotated_board[:]
        for i in range(9):
            if temp_board[i]!='X':
                temp_board[i]=str(i)
        all_rotated_boards.append(temp_board)
    return all_rotated_boards

def ai_transform_reflect(trial_board):
    all_reflected_boards=[]
    reflected_board=trial_board[:]
    reflected_board[0]=trial_board[6]
    reflected_board[1]=trial_board[7]
    reflected_board[2]=trial_board[8]
    reflected_board[6]=trial_board[0]
    reflected_board[7]=trial_board[1]
    reflected_board[8]=trial_board[2]
    for i in range(9):
        if reflected_board[i] != 'X':
            reflected_board[i]=str(i)
    all_reflected_boards.append(reflected_board)
    reflected_board=trial_board[:]
    reflected_board[0]=trial_board[2]
    reflected_board[2]=trial_board[0]
    reflected_board[3]=trial_board[5]
    reflected_board[5]=trial_board[3]
    reflected_board[6]=trial_board[8]
    reflected_board[8]=trial_board[6]
    for i in range(9):
        if reflected_board[i] != 'X':
            reflected_board[i]=str(i)
    all_reflected_boards.append(reflected_board)
    reflected_board=trial_board[:]
    reflected_board[1]=trial_board[3]
    reflected_board[3]=trial_board[1]
    reflected_board[5]=trial_board[7]
    reflected_board[7]=trial_board[5]
    reflected_board[2]=trial_board[6]
    reflected_board[6]=trial_board[2]
    for i in range(9):
        if reflected_board[i] != 'X':
            reflected_board[i]=str(i)
    all_reflected_boards.append(reflected_board)
    reflected_board=trial_board[:]
    reflected_board[0]=trial_board[8]
    reflected_board[8]=trial_board[0]
    reflected_board[1]=trial_board[5]
    reflected_board[5]=trial_board[1]
    reflected_board[3]=trial_board[7]
    reflected_board[7]=trial_board[3]
    for i in range(9):
        if reflected_board[i] != 'X':
            reflected_board[i]=str(i)
    all_reflected_boards.append(reflected_board)
    return all_reflected_boards

def ai_transformt(trial_board):
    all_transformed_boards=[trial_board]
    for i in ai_transform_rotate(trial_board):
        if i not in all_transformed_boards:
            all_transformed_boards.append(i)
    for i in ai_transform_reflect(trial_board):
        if i not in all_transformed_boards:
            all_transformed_boards.append(i)
    return all_transformed_boards

def ai_transform(trial_board):
    all_transformed_boards=[trial_board]
    transform_patterns=[[6,3,0,7,4,1,8,5,2],
                        [8,7,6,5,4,3,2,1,0],
                        [2,5,8,1,4,7,0,3,6],
                        [6,7,8,3,4,5,0,1,2],
                        [2,1,0,5,4,3,8,7,6],
                        [0,3,6,1,4,7,2,5,8],
                        [8,5,2,7,4,1,6,3,0]]
    for transform_pattern in transform_patterns:
        new_board=[]
        for i in range(9):
            if trial_board[transform_pattern[i]]=='X':
                new_board.append('X')
            else:
                new_board.append(str(i))
        if new_board not in all_transformed_boards:
            all_transformed_boards.append(new_board)
    return all_transformed_boards

b=['0','1','2','3','4','5','6','7','8']
for i in range(1000):
    for j in range(9):
        b[random.randint(0,8)]='X'
    m=ai_transform(b)
    n=ai_transformt(b)
    if m!=n:
        print(b)
        print(m)
        print(n)
        print()
    b=['0','1','2','3','4','5','6','7','8']
