import random


def header():

    print("               _____ _           _____               _____     _                   ")
    print("              |_   _(_)         |_   _|             |_   _|   | |                  ")
    print("                | |  _  ___ ______| | __ _  ___ ______| | __ _| |__   ___          ")
    print("                | | | |/ __|______| |/ _` |/ __|______| |/ _` | '_ \ / _ \         ")
    print("                | | | | (__       | | (_| | (__       | | (_| | | | | (_) |       ")
    print("                \_/ |_|\___|      \_/\__,_|\___|      \_/\__,_|_| |_|\___/        ")
    print("                                                                                   ")
    print("                                                                                   ")
    print("                 _____                _           _   _                             ")
    print("                /  __ \              | |         | | | |                            ")
    print("                | /  \/_ __ ___  __ _| |_ ___  __| | | |__  _   _                   ")
    print("                | |   | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |                  ")
    print("                | \__/| | |  __| (_| | ||  __| (_| | | |_) | |_| |                   ")
    print("                \____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |                   ")
    print("                                                            __/ |                   ")
    print("                                                            |___/                    ")
    print("                ______            _     _                   _  ___  ___      _       ")
    print("                |  _  \          (_)   | |                 | | |  \/  |     | |      ")
    print("                | | | |__ ___   ___  __| |   __ _ _ __   __| | | .  . | __ _| |_ ___ ")
    print("                | | | / _` \ \ / | |/ _` |  / _` | '_ \ / _` | | |\/| |/ _` | __/ _ \ ")
    print("                | |/ | (_| |\ V /| | (_| | | (_| | | | | (_| | | |  | | (_| | ||  __/ ")
    print("                |___/ \__,_| \_/ |_|\__,_|  \__,_|_| |_|\__,_| \_|  |_/\__,_|\__\___| ")


def check_board(board, s):
    return board[6] == s and board[7] == s and board[8] == s or \
        board[3] == s and board[4] == s and board[5] == s or \
        board[0] == s and board[1] == s and board[2] == s or \
        board[6] == s and board[3] == s and board[0] == s or \
        board[7] == s and board[4] == s and board[1] == s or \
        board[8] == s and board[5] == s and board[2] == s or \
        board[6] == s and board[4] == s and board[2] == s or \
        board[8] == s and board[4] == s and board[0] == s


def help():
    print('TIC TAC TOE HELP')
    show(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
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


def show(board):
    print('|-----------|')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('|-----------|')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('|-----------|')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('|-----------|')


def choose_name():
    ply1 = None
    ply2 = None
    while ply1 == ply2:
        ply1 = input("Your name: ")
        ply2 = input("Your name: ")
        if ply1 == ply2:
            print('Try different name!')
    for i in range(1, 2):
        sorszam = (random.randrange(2) + 1)
        if sorszam == 1:
            print('\n' + ply1 + ' goes first!')
        else:
            temp = ply1
            ply1 = ply2
            ply2 = temp
            print('\n' + ply1 + ' goes first!')
    print('\n' + ply1 + '  vs  ' + ply2)
    return [ply1, ply2]


def choose_nameai():
    ply1 = None
    ply2 = None
    while ply1 == ply2:
        ply1 = input("Your name: ")
        ply2 = str("Pisti")
        if ply1 == ply2:
            print('Try different name!')
    print('\n' + ply1 + '  vs  ' + ply2)
    return [ply1, ply2]


def game_on():
    p1, p2 = choose_name()
    xwinner = 0
    owinner = 0
    tie = 0
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
        roundend = 0
        while roundend < 1:
            nextplayer = 0
            while nextplayer < 1:
                print("\nFirst player select a spot: ")
                first = getchar()
                if first == "h":
                    help()
                    continue
                try:
                    first = int(first)

                except:
                    print("thats not a number!")
                    continue

                if board[first - 1] != 'X' and board[first - 1] != 'O':
                    board[first - 1] = 'X'
                    nextplayer += 1
                    show(board)
                    if check_board(board, "X"):
                        show(board)
                        roundend += 1
                        xwinner += 1
                        print("\nX wins")
                        xwin = True
                        print(p1 + " wins:%d " % (xwinner) + '\n' + p2 +
                              " wins:%d " % (owinner) + '\n' + "Tie:%d" % (tie))
                        temp = p1
                        p1 = p2
                        p2 = temp
                        temp2 = xwinner
                        xwinner = owinner
                        owinner = temp2
                        break
                else:
                    print("this spot is taken")
            if xwin == True:
                break
                show(board)
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                break
            while nextplayer == 1:
                print("\nSecond player select a spot: ")
                second = getchar()
                if second == "h":
                    help()
                    continue
                try:
                    second = int(second)
                except:
                    print("thats not a number!")
                    continue
                if board[second - 1] != 'X' and board[second - 1] != 'O':
                    board[second - 1] = 'O'
                    nextplayer -= 1
                    show(board)
                    if check_board(board, "O"):
                        show(board)
                        roundend += 1
                        owinner += 1
                        print("\nO wins")
                        print(p1 + " wins:%d " % (xwinner) + '\n' + p2 +
                              " wins:%d " % (owinner) + '\n' + "Tie:%d" % (tie))
                        owin = True
                        temp = p1
                        p1 = p2
                        p2 = temp
                        temp2 = owinner
                        owinner = xwinner
                        xwinner = temp2
                        break
                else:
                    print("this spot is taken!")
            if owin == True:
                break
                show(board)
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                temp = p1
                p1 = p2
                p2 = temp
                break


def game_ai():
    p1, p2 = choose_nameai()
    xwinner = 0
    owinner = 0
    tie = 0
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
        roundend = 0
        while roundend < 1:
            nextplayer = 0
            while nextplayer < 1:
                print("\n" + p1 + " select a spot: ")
                first = getchar()
                if first == "h":
                    help()
                    continue
                try:
                    first = int(first)

                except:
                    print("thats not a number!")
                    continue

                if board[first - 1] != 'X' and board[first - 1] != 'O':
                    board[first - 1] = 'X'
                    nextplayer += 1
                    show(board)
                    if check_board(board, "X"):
                        show(board)
                        roundend += 1
                        xwinner += 1
                        print("\nX wins")
                        xwin = True
                        print(p1 + " wins:%d " % (xwinner) + '\n' + p2 +
                              " wins:%d " % (owinner) + '\n' + "Tie:%d" % (tie))
                        break
                else:
                    print("this spot is taken")
            if xwin == True:
                break
                show(board)
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                break
            while nextplayer == 1:
                move = random.randint(1, 9)
                if board[move - 1] != 'X' and board[move - 1] != 'O':
                    board[move - 1] = 'O'
                    nextplayer -= 1
                    show(board)
                    if check_board(board, "O"):
                        show(board)
                        roundend += 1
                        owinner += 1
                        print("\nO wins")
                        print(p1 + " wins:%d " % (xwinner) + '\n' + p2 +
                              " wins:%d " % (owinner) + '\n' + "Tie:%d" % (tie))
                        owin = True
                        break
                else:
                    continue
            if owin == True:
                break
                show(board)
            if " " not in board:
                tie += 1
                print("\nTie")
                print(p1 + " wins:%d " % (xwinner) + '\n' + p2 + " wins:%d " %
                      (owinner) + '\n' + "Tie:%d" % (tie))
                break


header()
k = input("player or ai: ")
if k == "player":
    game_on()
else:
    game_ai()
