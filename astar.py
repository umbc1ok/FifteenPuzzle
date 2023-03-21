import Board
import reader
import utilities as ut


class astar:

    def __init__(self):
        self.counter = 0
        self.reachedDepth = 0
        self.found = False
        self.visited = set()

    def hammingsMetric(self,board):  #mowi ile kafelkow jest na swoim miejscu
        counter = 0
        for i in range(0,board.w*board.h):
            if board.tab[i]==str(i+1) and board.tab[i]!="0":
                counter = counter + 1
        return counter

    def manhattansMetric(self,board):   #mowi ile kazdy kafelek jest od idealnego polozenia
        result = 0
        for i in range(0,board.w*board.h):
            if board.tab[i]!="0":
                x1,y1 = board.getXYposition(i)                       # to jest pozycja danego elementu w tablicy
                x2,y2 = board.getXYposition(int(board.tab[i])-1)     # to jest pozycja IDEALNA danego elementu w tablicy (board[i] daje nam liczbe, a index
                                                                     # takiej liczby (idealny) powinien byc o 1 wiekszy
                result = result + abs(x1-x2) + abs(y1-y2)
        return result



    def solve(self,board, depth, maxdepth, lastmove, solution):
        return

p1 = Board.Board(4, 4, reader.parseFromFile())
p1.testprint()
example = astar
print("Manhattan:")
print(example.manhattansMetric(example,p1))
print("Hamming:")
print(example.hammingsMetric(example,p1))


