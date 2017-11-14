import random
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
board2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
win_commbinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def check_board():      
    for actual_win_comb in win_commbinations:
        if board[actual_win_comb[0]] == "x" and board[actual_win_comb[1]] == "x" and board[actual_win_comb[2]] == "x":
            print(usrOne, "! You are the winner!")
            return True

        elif board[actual_win_comb[0]] == "o" and board[actual_win_comb[1]] == "o" and board[actual_win_comb[2]] == "o":
            print(usrTwo, " You are the winner!")
            return True
    return False
def help():
    print('TIC TAC TOE HELP')
    print('|-----------|')
    print('|', board2[6], '|', board2[7], '|', board2[8], '|')
    print('|-----------|')
    print('|', board2[3], '|', board2[4], '|', board2[5], '|')
    print('|-----------|')
    print('|', board2[0], '|', board2[1], '|', board2[2], '|')
    print('|-----------|')
    print('REMEMBER,AFTER EACH ROUND PLAYERS SWAP POSITION.')
    print('SECOND PLAYER GOES FIRST,FIRST GOES SECOND AND SO ON.')


def getchar():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def show():
    print('|-----------|')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('|-----------|')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('|-----------|')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('|-----------|')


x = 0
o = 0
t = 0
p1 = None
p2 = None
while p1 == p2:
    p1 = input("Your name: ")
    p2 = input("Your name: ")
    if p1 == p2:
        print('Try different name!')

for i in range(1, 2):
    sorszam = (random.randrange(2) + 1)
    if sorszam == 1:
        print('\n' + p1 + ' goes first!')
    else:
        temp = p1
        p1 = p2
        p2 = temp
        print('\n' + p1 + ' goes first!')
print('\n' + p1 + '  vs  ' + p2)
while True:
    print('\nPress any key to start or "q" to quit or "h" for help: ')
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    ex = getchar()
    if ex == "q":
        break
    if ex == "h":
        help()
        continue
    owin = False
    xwin = False
    b = 0
    while b < 1:
        a = 0
        while a < 1:
            print("\nFirst player select a spot: ")
            first = getchar()
            if first == "h":
                help()
                continue
            try:
                first = int(first)
                if not first in range(0, 10):
                    print('Cant choose that number!')
                    continue
            except:
                print("thats not a number!")
                continue
            if board[first - 1] != 'X' and board[first - 1] != 'O':
                board[first - 1] = 'X'
                a += 1
                show()
                if board[6] == "X" and board[7] == "X" and board[8] == "X" or \
                        board[3] == "X" and board[4] == "X" and board[5] == "X" or \
                        board[0] == "X" and board[1] == "X" and board[2] == "X" or \
                        board[6] == "X" and board[3] == "X" and board[0] == "X" or \
                        board[7] == "X" and board[4] == "X" and board[1] == "X" or \
                        board[8] == "X" and board[5] == "X" and board[2] == "X" or \
                        board[6] == "X" and board[4] == "X" and board[2] == "X" or \
                        board[8] == "X" and board[4] == "X" and board[0] == "X":
                    show()
                    b += 1
                    x += 1
                    print("\nX wins")
                    xwin = True
                    print(p1 + " wins:%d " % (x) + '\n' + p2 + " wins:%d " % (o) + '\n' + "Tie:%d" % (t))
                    temp = p1
                    p1 = p2
                    p2 = temp
                    temp2 = x
                    x = o
                    o = temp2
                    break
            else:
                print("this spot is taken!")
        if xwin == True:
            break
            show()
        if " " not in board:
            t += 1
            print("\nTie")
            print(p1 + " wins:%d " % (x) + '\n' + p2 + " wins:%d " % (o) + '\n' + "Tie:%d" % (t))
            break
        while a == 1:
            print("\nSecond player select a spot: ")
            second = getchar()
            if second == "h":
                help()
                continue
            try:
                second = int(second)
                if not second in range(0, 10):
                    print('Cant choose that number!')
                    continue
            except:
                print("thats not a number!")
                continue
            if board[second - 1] != 'X' and board[first - 1] != 'O':
                board[second - 1] = 'O'
                a -= 1
                show()
                if board[6] == "O" and board[7] == "O" and board[8] == "O" or \
                        board[3] == "O" and board[4] == "O" and board[5] == "O" or \
                        board[0] == "O" and board[1] == "O" and board[2] == "O" or \
                        board[6] == "O" and board[3] == "O" and board[0] == "O" or \
                        board[7] == "O" and board[4] == "O" and board[1] == "O" or \
                        board[8] == "O" and board[5] == "O" and board[2] == "O" or \
                        board[6] == "O" and board[4] == "O" and board[2] == "O" or \
                        board[8] == "O" and board[4] == "O" and board[0] == "O":
                    show()
                    b += 1
                    o += 1
                    print("\nO wins")
                    print(p1 + " wins:%d " % (x) + '\n' + p2 + " wins:%d " % (o) + '\n' + "Tie:%d" % (t))
                    owin = True
                    temp = p1
                    p1 = p2
                    p2 = temp
                    temp2 = o
                    o = x
                    o = temp2
                    break
            else:
                print("this spot is taken!")
        if owin == True:
            break
            show()
        if " " not in board:
            t += 1
            print("\nTie")
            print(p1 + " wins:%d " % (x) + '\n' + p2 + " wins:%d " % (o) + '\n' + "Tie:%d" % (t))
            temp = p1
            p1 = p2
            p2 = temp
            break
