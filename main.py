import Board


def swap(board, zeroIndex, otherindex):
    temp = board.tab[zeroIndex]
    board.tab[zeroIndex] = board.tab[otherindex]
    board.tab[otherindex] = temp
    return board


def move(board, direction, index):
    if direction == "U":
        a = int(index / board.w)
        if a != 0:
            swap(board, index, index - board.w)
    elif direction == "D":
        a = int(index / board.w)
        if a != 3:
            swap(board, index, index - board.w)
    elif direction == "L":
        if index % board.w != 0:
            swap(board, index, index - 1)
    elif direction == "R":
        if index % board.w != 3:
            swap(board, index, index + 1)
    else:
        return

    return board

def dfs(board):
    visited = set()






p1 = Board.Board(4, 4)
p1.testprint()
move(p1, "U", 15)
p1.testprint()
