import Board


def swap(board, zeroIndex, otherindex):
    temp = board.tab[zeroIndex]
    board.tab[zeroIndex] = board.tab[otherindex]
    board.tab[otherindex] = temp


def makeMove(board, direction, index):
    if direction == "D":
        a = int(index / board.w)
        if a != 3:
            swap(board, index, index + board.w)
    if direction == "U":
        a = int(index / board.w)
        if a != 0:
            swap(board, index, index - board.w)
    elif direction == "L":
        if index % board.w != 0:
            swap(board, index, index - 1)
    elif direction == "R":
        if index % board.w != 3:
            swap(board, index, index + 1)
    else:
        return


def findZero(board):
    for index in range(0, board.tab.__sizeof__()):
        if board.tab[index] == "0":
            return index


def checkMoves(board, lastmove):
    index = findZero(board)
    moves = list()
    if (int(index / board.w) != 0) and (lastmove != "D"):
        moves.append("U")
    if int(index / board.w) != 3 and (
            lastmove != "U"):  # tu jakis error wyskakiwal // jest tutaj hardcodowana szerokosc, trzeba poprawic
        moves.append("D")
    if index % board.w != 0 and (lastmove != "R"):
        moves.append("L")
    if index % board.w != 3 and (lastmove != "L"):
        moves.append("R")

    return moves


def dfs(board, depth, maxdepth, lastmove):
    if board.checkBoard() is True:
        print("Gotcha")
        board.testprint()
        return

    # if depth > maxdepth:
    #     maxdepth = depth #???

    if depth >= maxdepth:
        print("maxdepth")
        return
    moves = checkMoves(board, lastmove)
    for move in moves:
        newState = board.__deepcopy__()
        makeMove(newState, move, findZero(newState))
        dfs(newState, depth + 1, maxdepth, move)
        if newState.checkBoard() is True:
            return
    return


p1 = Board.Board(4, 4)
p1.testprint()
p1.readFromFile()
dfs(p1, 0, 10, None)
