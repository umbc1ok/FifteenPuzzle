import copy

import reader


class Board:

    def __init__(self, w, h, tab):
        self.w = w
        self.h = h
        self.tab = tab

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
        tabcopy = copy.deepcopy(self.tab)
        new = Board(self.w, self.h, tabcopy)
        return new
