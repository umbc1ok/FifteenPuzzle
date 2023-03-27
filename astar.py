import Board
import reader
import saver
import utilities as ut
import time

class astar:

    def __init__(self,metric):
        self.counter = 1
        self.reachedDepth = 0
        self.found = False
        self.visited = set()
        self.metric = metric
        self.boards = list()
        self.solution = ''





    def solve(self,board, lastmove, solution):
        self.visited.add(board.__hash__())
        # dane statystyczne
        if self.reachedDepth < board.depth:
            self.reachedDepth = board.depth
        board.solution += lastmove
        #############
        # ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            self.solution = board.solution
            return self.solution



        moves = ut.checkMoves(board, lastmove)
        self.counter = self.counter + len(moves)
        for move in moves:
            newState = board.__deepcopy__()
            newState.depth +=1
            ut.makeMove(newState,move,ut.findZero(newState))
            if newState.__hash__() not in self.visited:
                self.boards.append(newState)

        self.boards.sort()
        bestState = self.boards.pop(0)
        #print(bestState.depth)
        self.solve(bestState, bestState.lastmove, solution)
        return

# p1 = Board.Board(4, 4, reader.parseFromFile("uklad"))
# p1.testprint()
# solver = astar("manh")
# startTime = time.time()
# solver.solve(p1,"","")
# solvingtime = time.time()-startTime
# f1 = 'astarSollution'
# f2 = 'astarAdditional'
# saver.saveToFile(solver.found, f1, f2, solver.solution, solver.visited.__len__(), solver.counter, solver.reachedDepth, solvingtime)
# print("Czas dzialania:", solvingtime, "s")
# print("Stany odwiedzone: ", solver.counter)
# print("Stany preztworzone: ", solver.visited.__len__())
# print("Maksymalna glebokosc: " ,solver.reachedDepth)





