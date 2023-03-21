import Board
import reader
import utilities as ut
import time

class astar:

    def __init__(self,metric):
        self.counter = 0
        self.reachedDepth = 0
        self.found = False
        self.visited = set()
        self.metric = metric
        self.boards = list()





    def solve(self,board, lastmove, solution):
        #self.visited.add(board.__hash__())
        # dane statystyczne
        if self.reachedDepth < board.depth:
            self.reachedDepth = board.depth
        solution += lastmove
        self.counter = self.counter +1
        # solution to string, na ktory sklada sie ciag ruchow potrzebnych do otrzymania rozwiazania

        # ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            print(solution)
            return solution

        moves = ut.checkMoves(board, lastmove)
        for move in moves:
            newState = board.__deepcopy__()
            newState.depth = newState.depth+1
            ut.makeMove(newState,move,ut.findZero(newState))
            self.boards.append(newState)

        self.boards.sort()
        bestState = self.boards.pop(0)
        self.solve(bestState, bestState.lastmove, solution)
        return

p1 = Board.Board(4, 4, reader.parseFromFile())
p1.testprint()
solver = astar("manh")
startTime = time.time()
solver.solve(p1,"","")
solvingtime = time.time()-startTime
print("Czas dzialania:", solvingtime, "s")
print("Stany odwiedzone: ", solver.boards.__len__())
print("Stany preztworzone: ", solver.counter)
print("Maksymalna glebokosc: " ,solver.reachedDepth)





