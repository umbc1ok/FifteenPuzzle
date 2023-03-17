import time

import Board
import reader
import utilities as u

class bfs:

    def __init__(self):
        self.counter = 0
        self.reachedDepth = 0
        self.found = False
        self.visited = set()
        self.queue = []

    def solve(self, board, solution):
        self.visited.add(board.__hash__())
        self.queue.popleft()
        # dane statystyczne
        #jeśli dojdzie do końca linii przerzucić na kolejną głębokość (czzy nie lepiej dodać pole depth do board i ta która będzie dobra to to zwracać?)

        self.counter = self.counter+1
        if board.lastmove != null:
            solution += board.lastmove
        #solution to string, na ktory sklada sie ciag ruchow potrzebnych do otrzymania rozwiazania


        #ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            print(solution)
            return solution

        #if depth >= maxdepth:
            #return
        moves = u.checkMoves(board, lastmove)
        for move in moves:
            newState = board.__deepcopy__()
            u.makeMove(newState, move, u.findZero(newState))    #index funkcja (argument to wartosc z listy, w tym przypadku 0)
            newState.lastmove = move
            if newState.__hash__() not in self.visited:
                self.queue.append(newState)
                #self.solve(newState, depth + 1, maxdepth, move, solution)
            if self.found is True:
                return
        for q in self.queue:
            self.solve(q, solution)
        return



p1 = Board.Board(4, 4, reader.parseFromFile())
p1.testprint()
solver = dfs()
start = time.time()
solver.solve(p1, 0, 100, "", "")
end = time.time() - start
print(end)
print(solver.counter)
print(solver.reachedDepth)
