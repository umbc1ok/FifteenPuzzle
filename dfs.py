import time

import Board
import reader
import saver
import utilities as u

class dfs:

    def __init__(self):
        self.counter = 1            #odwiedzone
        self.reachedDepth = 0
        self.found = False
        self.visited = {}           #przetworzone
        self.solution = ''

    def solve(self, board, depth, maxdepth, lastmove, solution, order):

        if depth > maxdepth:
            return
        # dane statystyczne
        if self.reachedDepth < depth:
            self.reachedDepth = depth
        solution += lastmove


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
            u.makeMove(newState, move, u.findZero(newState))   #index funkcja (argument to wartosc z listy, w tym przypadku 0)
            newState.depth += 1
            if ( (newState.__hash__() in self.visited) and (self.visited[newState.__hash__()] > depth)) or newState.__hash__() not in self.visited:
                self.visited[newState.__hash__()] = newState.depth
                self.solve(newState, depth + 1, maxdepth, move, solution, order)
            if self.found is True:
                return
        return

