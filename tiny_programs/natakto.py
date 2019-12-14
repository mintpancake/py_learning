#method from https://miseregames.files.wordpress.com/2012/04/x-onlyttt.pdf

import copy,random

boards={'A':['0','1','2','3','4','5','6','7','8'],
        'B':['0','1','2','3','4','5','6','7','8'],
        'C':['0','1','2','3','4','5','6','7','8']}
valid_boards=['A','B','C']
patterns={'1': [['X', '1', '2', '3', '4', '5', '6', '7', '8'],
                ['0', 'X', '2', '3', '4', '5', '6', '7', '8'],
                ['X', 'X', 'X', '3', '4', '5', '6', '7', '8'],
                ['X', '1', '2', '3', 'X', '5', '6', '7', 'X'],
                ['X', '1', '2', '3', '4', 'X', '6', 'X', '8'],
                ['0', 'X', '2', '3', 'X', '5', '6', 'X', '8'],
                ['X', 'X', 'X', 'X', '4', '5', '6', '7', '8'],
                ['X', 'X', 'X', '3', 'X', '5', '6', '7', '8'],
                ['X', 'X', 'X', '3', '4', '5', 'X', '7', '8'],
                ['X', 'X', 'X', '3', '4', '5', '6', 'X', '8'],
                ['X', 'X', '2', '3', 'X', '5', '6', 'X', '8'],
                ['X', 'X', '2', '3', 'X', '5', '6', '7', 'X'],
                ['X', '1', 'X', '3', 'X', '5', 'X', '7', '8']],
         'a' : [['X', '1', '2', '3', '4', '5', '6', '7', 'X'],
                ['0', 'X', '2', 'X', '4', '5', '6', '7' , '8'],
                ['0', 'X', '2', '3', '4', '5', '6', 'X' , '8'],
                ['X', 'X', '2', '3', '4', '5', 'X', '7', '8'],
                ['X', '1', 'X', '3', 'X', '5', '6', '7', '8'],
                ['X', '1', 'X', '3', '4', '5', '6', 'X', '8'],
                ['X', '1', '2', '3', 'X', 'X', '6', '7', '8'],
                ['X', 'X', '2', 'X', 'X', '5', '6', '7', '8'],
                ['X', 'X', '2', 'X', '4', 'X', '6', '7', '8'],
                ['X', 'X', '2', 'X', '4', '5', '6', '7', 'X'],
                ['X', 'X', '2', '3', '4', '5', '6', 'X', 'X'],
                ['X', '1', 'X', '3', '4', '5', 'X', '7', 'X'],
                ['0', 'X', '2', 'X', '4', 'X', '6', 'X', '8'],
                ['X', 'X', '2', '3', 'X', 'X', 'X', '7', '8'],
                ['X', 'X', '2', '3', '4', 'X', 'X', 'X', '8'],
                ['X', 'X', '2', '3', '4', 'X', 'X', '7', 'X'],
                ['X', 'X', '2', 'X', '4', 'X', '6', 'X', 'X']],
         'b' : [['X', '1', 'X', '3', '4', '5', '6', '7', '8'],
                ['X', '1', '2', '3', 'X', '5', '6', '7', '8'],
                ['X', '1', '2', '3', '4', 'X', '6', '7', '8'],
                ['0', 'X', '2', '3', 'X', '5', '6', '7', '8'],
                ['X', 'X', '2', 'X', '4', '5', '6', '7', '8'],
                ['0', 'X', '2', 'X', '4', 'X', '6', '7', '8'],
                ['X', 'X', '2', '3', 'X', 'X', '6', '7', '8'],
                ['X', 'X', '2', '3', 'X', '5', 'X', '7', '8'],
                ['X', 'X', '2', '3', '4', 'X', 'X', '7', '8'],
                ['X', 'X', '2', '3', '4', '5', 'X', 'X', '8'],
                ['X', 'X', '2', '3', '4', '5', 'X', '7', 'X'],
                ['X', '1', 'X', '3', 'X', '5', '6', 'X', '8'],
                ['X', '1', '2', '3', 'X', 'X', '6', 'X', '8'],
                ['X', 'X', '2', 'X', '4', 'X', '6', 'X', '8'],
                ['X', 'X', '2', 'X', '4', 'X', '6', '7', 'X']],
         'c' : [['0', '1', '2', '3', '4', '5', '6', '7', '8']],
         'd' : [['X', 'X', '2', '3', '4', 'X', '6', '7', '8'],
                ['X', 'X', '2', '3', '4', '5', '6', 'X', '8'],
                ['X', 'X', '2', '3', '4', '5', '6', '7', 'X']],
        'ab' : [['X', 'X', '2', '3', 'X', '5', '6', '7', '8'],
                ['X', '1', 'X', '3', '4', '5', 'X', '7', '8'],
                ['0', 'X', '2', 'X', 'X', '5', '6', '7', '8'],
                ['X', 'X', '2', '3', '4', 'X', '6', 'X', '8'],
                ['X', 'X', '2', '3', '4', 'X', '6', '7', 'X']],
        'ad' : [['X', 'X', '2', '3', '4', '5', '6', '7', '8']],
        'c2' : [['0', '1', '2', '3', 'X', '5', '6', '7', '8']]}

def show():
    for i in range(len(valid_boards)-1):
        print(f'{valid_boards[i]}      ',end='')
    print(valid_boards[-1])
    for i in range(3):
        for j in range(len(valid_boards)-1):
            print(f'{boards[valid_boards[j]][3*i]} {boards[valid_boards[j]][3*i+1]} {boards[valid_boards[j]][3*i+2]}  ',end='')
        print(f'{boards[valid_boards[-1]][3*i]} {boards[valid_boards[-1]][3*i+1]} {boards[valid_boards[-1]][3*i+2]}')

def scan(n):
    ipt=list((input(f'Player {n}: ')))
    while len(ipt)!=2 or ipt[0] not in valid_boards or (not (int(ipt[1])>=0 and int(ipt[1])<=8)) or boards[ipt[0]][int(ipt[1])]=='X':
        print('Invalid move, please input again')
        ipt=list((input(f'Player {n}: ')))
    return ipt

def modify(ipt):
    boards[ipt[0]][int(ipt[1])]='X'
    return

def judge_winner():
    if len(valid_boards)==1 and judge_dead_board()[0]:
         return True
    else:
        return False

def judge_dead_board():
    dead=False
    dead_board=''
    for i in valid_boards:
        for j in range(3):
            if boards[i][3*j]==boards[i][3*j+1] and boards[i][3*j+1]==boards[i][3*j+2]:
                dead=True
                dead_board=i
                break
            if boards[i][j]==boards[i][3+j] and boards[i][3+j]==boards[i][6+j]:
                dead=True
                dead_board=i
                break
            if (boards[i][0]==boards[i][4] and boards[i][4]==boards[i][8]) or (boards[i][2]==boards[i][4] and boards[i][4]==boards[i][6]):
                dead=True
                dead_board=i
                break
        if dead==True:
            break
    return dead,dead_board

def ai_find_blanks():
    blanks=[]
    for i in valid_boards:
        for j in boards[i]:
            if j!='X':
                blanks.append([i,j])
    return blanks

def ai_get_trial_boards(ipt):
    trial_boards=copy.deepcopy(boards)
    trial_boards[ipt[0]][int(ipt[1])]='X'
    return trial_boards

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

def ai_transform(trial_board):
    all_transformed_boards=[trial_board]
    for i in ai_transform_rotate(trial_board):
        if i not in all_transformed_boards:
            all_transformed_boards.append(i)
    for i in ai_transform_reflect(trial_board):
        if i not in all_transformed_boards:
            all_transformed_boards.append(i)
    return all_transformed_boards

def ai_get_pattern(trial_board):
    all_patterns=[]
    for pattern in patterns:
        all_patterns.extend(patterns[pattern])
    transformed_board=[]
    for board in ai_transform(trial_board):
        if board in all_patterns:
            transformed_board=board
            break
    if transformed_board in patterns['1']:
        return {'1':1}
    elif transformed_board in patterns['a']:
        return {'a':1}
    elif transformed_board in patterns['b']:
        return {'b':1}
    elif transformed_board in patterns['c']:
        return {'c':1}
    elif transformed_board in patterns['d']:
        return {'d':1}
    elif transformed_board in patterns['ab']:
        return {'a':1, 'b':1}
    elif transformed_board in patterns['ad']:
        return {'a':1, 'd':1}
    elif transformed_board in patterns['c2']:
        return {'c':2}
    else:
        return {}

def ai_calculate_total_pattern(trial_boards):
    total_pattern={}
    existing_patterns=[]
    for _ in range(3-len(valid_boards)):
        existing_patterns.append({'1':1})
    for trial_board in trial_boards:
        existing_patterns.append(ai_get_pattern(trial_boards[trial_board]))
    for pattern in existing_patterns:
        for para in pattern:
            if para not in total_pattern:
                total_pattern[para]=pattern[para]
            else:
                total_pattern[para]+=pattern[para]
    if '1' in total_pattern:
        if len(total_pattern.keys())!=1:
            del total_pattern['1']
        else:
            total_pattern={'1':1}
    return total_pattern

def ai_test_trial_boards(trial_boards):
    winning_total_patterns=[{"a":1}, {"b":2}, {"c":2}, {"b":1, "c":1}]
    total_pattern=ai_calculate_total_pattern(trial_boards)
    if total_pattern in winning_total_patterns:
        return True
    return False

def ai():
    ipts=[]
    possible_ipts=ai_find_blanks()
    for ipt in possible_ipts:
        trial_boards=ai_get_trial_boards(ipt)
        yes_trial_boards=ai_test_trial_boards(trial_boards)
        if yes_trial_boards:
            ipts.append(ipt)
    ipt=random.choice(ipts)
    return ipt

def stupid_ai():
    ipts=ai_find_blanks()
    ipt=random.choice(ipts)
    return ipt


def main():
    player=1
    while True:
        show()
        if player==1:
            #ipt=scan(player)
            ipt=ai()
            #ipt=stupid_ai()
            print(f"Player 1: {''.join(ipt)}")
        elif player==2:
            ipt=scan(player)
            #ipt=ai()
            #ipt=stupid_ai()
            #print(f"Player 2: {''.join(ipt)}")
        modify(ipt)
        if judge_winner():
            print(f'Player {player%2+1} wins game')
            break
        if judge_dead_board()[0]:
            dead_board=judge_dead_board()[1]
            valid_boards.remove(dead_board)
            del boards[dead_board]
        player=player%2+1
    return

main()