import utilities as u


class bfs:

    def __init__(self):
        self.visitedStates = 1        #odwiedzone
        self.reachedDepth = 0
        self.found = False
        self.processedStates = set()    #przetworzone
        self.queue = []
        self.solution = ""

    def solve(self, board, order):
        self.processedStates.add(board.__hash__())

        if len(self.queue) > 0:
            self.queue.pop(0)
        if self.reachedDepth < board.depth:
            self.reachedDepth = board.depth



        if board.lastmove is not None:
            board.solution = board.solution + board.lastmove

        # ALGORYTM
        if board.checkBoard() is True:
            self.found = True
            self.solution = board.solution
            self.reachedDepth = len(board.solution)
            return board.solution


        moves = u.next_in_order(order, board)
        self.visitedStates = self.visitedStates + len(moves)
        for move in moves:
            newState = board.__deepcopy__()
            u.makeMove(newState, move,
                       u.findZero(newState))  # index funkcja (argument to wartosc z listy, w tym przypadku 0)
            newState.lastmove = move
            if newState.__hash__() not in self.processedStates:
                self.queue.append(newState)
        if self.found is False:
            self.solve(self.queue[0], order)
        return




