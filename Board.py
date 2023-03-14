import copy

import reader


class Board:
    w = 1
    h = 1
    tab = []

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def readFromFile(self):
        self.tab = reader.parseFromFile()
    def testprint(self):
        print(self.tab)

    def checkBoard(self):
        size = self.w * self.h
        if int(self.tab[size - 1]) != 0:
            return False
        for i in range(0, size - 2):
            if int(self.tab[i]) != i + 1:
                return False
        return True


    def __deepcopy__(self, memodict={}):
        new = Board(self.w, self.h)
        new.tab = copy.deepcopy(self.tab)
        return new
