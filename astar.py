import utilities as ut


class astar:

    def __init__(self,metric):
        self.visitedStates = 1        #odwiedzone
        self.reachedDepth = 0
        self.found = False
        self.processedStates = set()    #przetworzone
        self.metric = metric
        self.boards = list()
        self.solution = ''





    def solve(self,board, lastmove, solution):
        self.processedStates.add(board.__hash__())
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

        #POWIEKSZAMY ILOSC STANOW ODWIEDZONYCH O SASIADOW
        self.visitedStates = self.visitedStates + len(moves)

        for move in moves:
            newState = board.__deepcopy__()
            newState.depth += 1
            ut.makeMove(newState,move,ut.findZero(newState))
            if newState.__hash__() not in self.processedStates:
                self.boards.append(newState)

        self.boards.sort()
        bestState = self.boards.pop(0)
        self.solve(bestState, bestState.lastmove, solution)
        return







