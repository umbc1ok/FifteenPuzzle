def swap(board, zeroIndex, otherindex):   # przesuniecie naszego prostokata, funkcja uzywana tylko w makeMove()
    temp = board.tab[zeroIndex]
    board.tab[zeroIndex] = board.tab[otherindex]
    board.tab[otherindex] = temp


def makeMove(board, direction, index):  #sprawdza ktory ruch ma zostac wykonany i ten wykonuje
    if direction == "D":
        board.lastmove = "D"
        swap(board, index, index + board.w)
    elif direction == "U":
        board.lastmove = "U"
        swap(board, index, index - board.w)
    elif direction == "L":
        board.lastmove = "L"
        swap(board, index, index - 1)
    elif direction == "R":
        board.lastmove = "R"
        swap(board, index, index + 1)
    else:
        return


def findZero(board):    #znajduje index zera na planszy
    for index in range(0, board.tab.__sizeof__()):
        if board.tab[index] == "0":
            return index


def checkMoves(board, lastmove):             #zwraca liste dostepnych ruchow
    index = findZero(board)
    moves = list()
    if (int(index / board.w) != 0) and (lastmove != "D"):
        moves.append("U")
    if index % board.w != 0 and (lastmove != "R"):
        moves.append("L")
    if int(index / board.w) != board.h - 1 and (lastmove != "U"):
        moves.append("D")
    if index % board.w != board.w - 1 and (lastmove != "L"):
        moves.append("R")


    return moves


def next_in_order(order, board):     #returns list of moves in right order
    moves = checkMoves(board, board.lastmove)
    myMoves = list()
    for o in order:
        if o in moves:
            myMoves.append(o)
    return myMoves
