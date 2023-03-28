import utilities as u

class dfs:

    def __init__(self):
        self.visitedStates = 1            #odwiedzone
        self.reachedDepth = 0
        self.found = False
        self.processedStates = {}           #przetworzone
        self.solution = ''

    def solve(self, board, maxdepth, lastmove, solution, order):

        if board.depth > maxdepth:
            return
        # dane statystyczne
        if self.reachedDepth < board.depth:
            self.reachedDepth = board.depth
        solution += lastmove


        #ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            #print(solution)
            self.solution = solution
            return solution


        moves = u.next_in_order(order, board)
        self.visitedStates = self.visitedStates + len(moves)
        for move in moves:
            newState = board.__deepcopy__()
            u.makeMove(newState, move, u.findZero(newState))   #index funkcja (argument to wartosc z listy, w tym przypadku 0)
            newState.depth += 1
            if ((newState.__hash__() in self.processedStates) and (self.processedStates[newState.__hash__()] > newState.depth))\
                    or newState.__hash__() not in self.processedStates:
                self.processedStates[newState.__hash__()] = newState.depth
                self.solve(newState, maxdepth, move, solution, order)
            if self.found is True:
                return
        return

