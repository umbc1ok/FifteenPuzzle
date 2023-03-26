import time

import Board
import reader
import saver
import utilities as u

class dfs:

    def __init__(self):
        self.counter = 1
        self.reachedDepth = 0
        self.found = False
        self.visited = {}
        self.solution = ''

    def solve(self, board, depth, maxdepth, lastmove, solution, order):
        #if board.__hash__() not in self.visited:
        #    self.visited[board.__hash__()] = board.depth

        if depth > maxdepth:
            return
        # dane statystyczne
        if self.reachedDepth < depth:
            self.reachedDepth = depth
        #self.counter = self.counter+1
        solution += lastmove
        #solution to string, na ktory sklada sie ciag ruchow potrzebnych do otrzymania rozwiazania


        #ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            #print(solution)
            self.solution = solution
            return solution


        moves = u.next_in_order(order, board)
        self.counter = self.counter + len(moves)
        for move in moves:
            newState = board.__deepcopy__()
            u.makeMove(newState, move, u.findZero(newState))    #index funkcja (argument to wartosc z listy, w tym przypadku 0)
            if ( (newState.__hash__() in self.visited) and (self.visited[newState.__hash__()] < depth)) or newState.__hash__() not in self.visited:
                self.visited[newState.__hash__()] = board.depth
                self.solve(newState, depth + 1, maxdepth, move, solution, order)
            if self.found is True:
                return
        return



# p1 = Board.Board(4, 4, reader.parseFromFile("uklad"))
# p1.testprint()
# solver = dfs()
# start = time.time()
# solver.solve(p1, 0, 20, "", "", ['L', 'U', 'R', 'D'])
# #print(solver.solution)
# solvingtime = time.time() - start
# f1 = 'dfsSollution'
# f2 = 'dfsAdditional'
# saver.saveToFile(solver.found, f1, f2, solver.solution, solver.visited.__len__(), solver.counter, solver.reachedDepth, solvingtime)
# print("Czas dzialania:", solvingtime, "s")
# print("Stany odwiedzone: ", solver.counter)
# print("Stany preztworzone: ", solver.visited.__len__())
# print("Maksymalna glebokosc: ", solver.reachedDepth)
