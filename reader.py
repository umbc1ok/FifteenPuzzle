import Board

def parseFromFile(fileName):
    f = open("./files/uklady/"+fileName, "r")
    tab = []
    i = 0
    for i, line in enumerate(f.readlines()):
        if i > 0:
            row = line.strip().split(" ")
            for element in row:
                tab.append(element)
    f.close()
    return tab
def parseHeight(fileName):
    f = open("./files/uklady/"+fileName, "r")
    line = f.readline().strip().split(" ")
    height = line[0]

    f.close()
    return int(height)
def parseWidth(fileName):
    f = open("./files/uklady/" + fileName, "r")
    line = f.readline().strip().split(" ")
    width = line[1]

    f.close()
    return int(width)
