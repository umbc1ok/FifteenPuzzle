import Board
##### KURDE TRZEBA POPRAWIC TO POTEM ZEBY NIE BYLO PROBLEMU ZE NIE CZYTA WYMIAROW Z PLIKU######

def parseFromFile():
    f = open("uklad", "r")
    tab = []
    i = 0
    for i, line in enumerate(f.readlines()):
        if i > 0:
            row = line.strip().split(" ")
            for element in row:
                tab.append(element)
    f.close()
    return tab
