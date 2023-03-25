import time

import Board
import reader
import saver
import utilities as u


class bfs:

    def __init__(self):
        self.counter = 1
        self.reachedDepth = 0
        self.found = False
        self.visited = set()    #przetworzone
        self.queue = []
        self.solution = ""

    def solve(self, board, order):
        self.visited.add(board.__hash__())

        if len(self.queue) > 0:
            self.queue.pop(0)
        # dane statystyczne
        # jeśli dojdzie do końca linii przerzucić na kolejną głębokość (czzy nie lepiej dodać pole depth do board i ta która będzie dobra to to zwracać?)

        #self.counter = self.counter + 1
        if board.lastmove is not None:
            board.solution = board.solution + board.lastmove
        # solution to string, na ktory sklada sie ciag ruchow potrzebnych do otrzymania rozwiazania

        # ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            print(board.solution)
            self.solution = board.solution
            return board.solution

        # if depth >= maxdepth:
        # return

        moves = u.next_in_order(order, board)
        self.counter = self.counter + len(moves)
        for move in moves:
            newState = board.__deepcopy__()
            u.makeMove(newState, move,
                       u.findZero(newState))  # index funkcja (argument to wartosc z listy, w tym przypadku 0)
            newState.lastmove = move
            if newState.__hash__() not in self.visited:
                #self.counter = self.counter + 1
                self.queue.append(newState)
                # self.solve(newState, depth + 1, maxdepth, move, solution)
            # if self.found is True:
            #   print(self.found)
            #  print(newState.checkBoard())
            # newState.testprint()
            # return
        if self.found is False:
            #print("checking next board in queue")
            #print(self.queue[0].testprint())
            self.solve(self.queue[0], order)
        return



# p1 = Board.Board(4, 4, reader.parseFromFile("uklad"))
# p1.testprint()
# solver = bfs()
# start = time.time()
# solver.solve(p1, ['L', 'U', 'R', 'D'])
# solvingtime = time.time() - start
# f1 = 'bfsSollution'
# f2 = 'bfsAdditional'
# saver.saveToFile(solver.found, f1, f2, solver.solution, solver.visited.__len__(), solver.counter, solver.reachedDepth, solvingtime)
# print("Czas dzialania:", solvingtime, "s")
# print("Stany odwiedzone: ", solver.counter)
# print("Stany preztworzone: ", solver.visited.__len__())
# print("Maksymalna glebokosc: " ,solver.solution.__len__())
