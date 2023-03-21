import copy


class Board:

    def __init__(self, w, h, tab):
        self.w = w
        self.h = h
        self.tab = tab
        self.lastmove = None

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
        return new

    def __hash__(self):
        return hash(tuple(self.tab))
