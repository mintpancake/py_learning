'''
'1':  [['X', '1', '2', '3', '4', '5', '6', '7', '8'],
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
             ['X', 'X', '2', 'X', '4', 'X', '6', 'X', 'X']]
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
'c2' : [['0', '1', '2', '3', 'X', '5', '6', '7', '8']]

def ai_test_trial_boards(trial_boards):
    winning_total_patterns=[{"a":1}, {"b":2}, {"c":2}, {"b":1, "c":1}]
    total_pattern=ai_calculate_total_pattern(trial_boards)
    if total_pattern in winning_total_patterns:
        return 10#??????????
    return 0#??????????
        return True
    return False

def ai():
    ipts=[]
    possible_ipts=ai_find_blanks()
    maxValue=-float('inf')#??????????
    for ipt in possible_ipts:
        trial_boards=ai_get_trial_boards(ipt)
        yes_trial_boards=ai_test_trial_boards(trial_boards)
        if yes_trial_boards>maxValue:#??????????
            maxValue=yes_trial_boards#??????????
    for ipt in possible_ipts:
        trial_boards=ai_get_trial_boards(ipt)
        yes_trial_boards=ai_test_trial_boards(trial_boards)
        if yes_trial_boards==maxValue:
            ipts.append(ipt)
    for ipt in possible_ipts:
        trial_boards=ai_get_trial_boards(ipt)
        yes_trial_boards=ai_test_trial_boards(trial_boards)
        if yes_trial_boards:
            ipts.append(ipt)
    ipt=random.choice(ipts)
    return ipt
'''

board={'A':['0','1','2','3','4','5','6','7','8'],'B':['0','1','2','3','4','5','6','7','8'],'C':['0','1','2','3','4','5','6','7','8']}
valid_key=['A','B','C']

def show():
    for i in range(len(valid_key)-1):
        print(f'{valid_key[i]}      ',end='')
    print(valid_key[-1])
    for i in range(3):
        for j in range(len(valid_key)-1):
            print(f'{board[valid_key[j]][3*i]} {board[valid_key[j]][3*i+1]} {board[valid_key[j]][3*i+2]}  ',end='')
        print(f'{board[valid_key[-1]][3*i]} {board[valid_key[-1]][3*i+1]} {board[valid_key[-1]][3*i+2]}')

def scan(n):
    ipt=list((input(f'Player {n}: ')))
    while len(ipt)!=2 or ipt[0] not in valid_key or (not (ipt[1]>='0' and ipt[1]<='8')) or board[ipt[0]][int(ipt[1])]=='X':
        print('Invalid move, please input again')
        ipt=list((input(f'Player {n}: ')))
    return ipt

def modify(ipt):
    board[ipt[0]][int(ipt[1])]='X'
    return

def judge_winner():
    if len(valid_key)==1 and judge_dead_board()[0]:
         return True
    else:
        return False

def judge_dead_board():
    dead=False
    dead_board=''
    for i in board:
        for j in range(3):
            if board[i][3*j]==board[i][3*j+1] and board[i][3*j+1]==board[i][3*j+2]:
                dead=True
                dead_board=i
                break
            if board[i][j]==board[i][3+j] and board[i][3+j]==board[i][6+j]:
                dead=True
                dead_board=i
                break
            if (board[i][0]==board[i][4] and board[i][4]==board[i][8]) or (board[i][2]==board[i][4] and board[i][4]==board[i][6]):
                dead=True
                dead_board=i
                break
        if dead==True:
            break
    return dead,dead_board

def main():
    player=1
    while True:
        show()
        ipt=scan(player)
        modify(ipt)
        if judge_winner():
            print(f'Player {player%2+1} wins game')
            break
        if judge_dead_board()[0]:
            dead_board=judge_dead_board()[1]
            valid_key.remove(dead_board)
            del board[dead_board]
        player=player%2+1
    return

main()