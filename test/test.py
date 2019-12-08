board={'A':['0','1','2','3','4','5','6','7','8','9'],'B':['0','1','2','3','4','5','6','7','8','9'],'C':['0','1','2','3','4','5','6','7','8','9']}
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
    while len(ipt)!=2 or ipt[0] not in valid_key or (not (int(ipt[1])>=0 and int(ipt[1])<=8)) or board[ipt[0]][int(ipt[1])]=='X':
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

def ai():
    return 'A0'

def main():
    player=1
    while True:
        show()
        if player==1:
            ipt=ai()
        if player==2:
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