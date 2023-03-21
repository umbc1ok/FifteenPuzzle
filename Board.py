import copy
import utilities as ut

class Board:

    def __init__(self, w, h, tab):
        self.w = w
        self.h = h
        self.tab = tab
        self.lastmove = None
        self.solution = ""
        self.metric = "hamm"
        self.depth = 0

    def testprint(self):
        i = 0
        for n in range(0, self.h):
            for m in range(0, self.w):
                print(self.tab[i], end=" ")
                i += 1
            print("\n")



    def checkBoard(self):
        size = self.w * self.h
        if int(self.tab[size - 1]) != 0:
            #print("checking last place")
            return False
        for i in range(0, size - 2):
            if int(self.tab[i]) != i + 1:
                #print("something at wrong place")
                return False
        return True
    def getXYposition(self,index):
        x = int(index % self.w)
        y = int(index / self.w)
        return [x,y]



    def __deepcopy__(self, memodict={}):
        tabcopy = copy.deepcopy(self.tab)
        new = Board(self.w, self.h, tabcopy)
        new.solution = copy.deepcopy(self.solution)
        new.depth = self.depth
        return new

    def __hash__(self):
        return hash(tuple(self.tab))

    def hammingsMetric(self):  #mowi ile kafelkow jest na swoim miejscu
        counter = 0
        for i in range(0,self.w*self.h):
            if self.tab[i]==str(i+1) and self.tab[i]!="0":
                counter = counter + 1
        return counter

    def manhattansMetric(self):   #mowi ile kazdy kafelek jest od idealnego polozenia
        result = 0
        for i in range(0,self.w*self.h):
            if self.tab[i]!="0":
                x1,y1 = self.getXYposition(i)                       # to jest pozycja danego elementu w tablicy
                x2,y2 = self.getXYposition(int(self.tab[i])-1)     # to jest pozycja IDEALNA danego elementu w tablicy (board[i] daje nam liczbe, a index
                                                                     # takiej liczby (idealny) powinien byc o 1 wiekszy
                result = result + abs(x1-x2) + abs(y1-y2)
        return result

    def __lt__(self, obj):
        if self.metric == "hamm":
            return ((self.hammingsMetric()) > (obj.hammingsMetric()))
        else:
            return ((self.manhattansMetric()) > (obj.manhattansMetric()))