import reader


class Board:
    w = 1
    h = 1
    tab = []

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tab = reader.parseFromFile()

    def testprint(self):
        print(self.tab)
