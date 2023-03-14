import Board
import reader
import utilities as u

class dfs:

    def __init__(self):
        self.counter = 0
        self.reachedDepth = 0

    def solve(self,board, depth, maxdepth, lastmove, solution):

        # dane statystyczne
        if self.reachedDepth < depth:
            self.reachedDepth = depth
        self.counter = self.counter+1
        solution += lastmove
        #solution to string, na ktory sklada sie ciag ruchow potrzebnych do otrzymania rozwiazania


        #ALGORYTM
        if board.checkBoard() is True:
            print(solution)
            return solution

        if depth >= maxdepth:
            return
        moves = u.checkMoves(board, lastmove)
        moves.sort()
        for move in moves:
            newState = board.__deepcopy__()
            u.makeMove(newState, move, u.findZero(newState))
            self.solve(newState, depth + 1, maxdepth, move, solution)
        return



p1 = Board.Board(4, 4, reader.parseFromFile())
p1.testprint()
solver = dfs()
solver.solve(p1, 0, 20, "", "")
print(solver.counter)
print(solver.reachedDepth)
