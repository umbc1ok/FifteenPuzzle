from _csv import reader

import chardet as chardet
import matplotlib.pyplot as plt
#import pandas as pd
import csv as csv


def summaryGraph(data, criterion_nr, criterion_name, filename, strange_numbers):
    plt.clf()

    sum_astar = []  # pierwsze dla ilości zliczonych obiektów, reszta to głębokość rozwiązania = index
    sum_bfs = []
    sum_dfs = []
    for i in range(0, 8):
        sum_astar.append(0.0)
        sum_bfs.append(0.0)
        sum_dfs.append(0.0)
    avg_astar_table = []
    avg_bfs_table = []
    avg_dfs_table = []

    astar = [0.0]*7
    bfs = [0.0]*7
    dfs = [0.0]*7

    for d in data:
        print(d[2])
        if d[2] == 'astr':
            sum_astar[int(d[0])] += float(d[criterion_nr + 3])
            # indeks kryterium bo kryteria zaczynają się od data[2] a kryteria numerujemy od 1
            sum_astar[0] = sum_astar[0] + 1.0
            astar[int(d[0])-1] += 1.0
        if d[2] == 'bfs':
            sum_bfs[int(d[0])] += float(d[criterion_nr + 3])
            sum_bfs[0] = sum_bfs[0] + 1.0
            bfs[int(d[0])-1] += 1.0
        if d[2] == 'dfs':
            sum_dfs[int(d[0])] += float(d[criterion_nr + 3])
            sum_dfs[0] = sum_dfs[0] + 1.0
            dfs[int(d[0])-1] += 1.0

    for i in range(0, 7):
        avg_astar_table.append(sum_astar[i + 1] / astar[i])
        avg_bfs_table.append(sum_bfs[i + 1] / bfs[i])
        avg_dfs_table.append(sum_dfs[i + 1] / dfs[i])

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x], weights=[avg_astar_table, avg_bfs_table, avg_dfs_table], label=['A*', 'BFS', 'DFS'],
             color=['blue', 'purple', 'green'], bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])
    plt.title('Ogólne')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.legend(('A*', 'BFS', 'DFS'), loc='upper left')
    if strange_numbers is True:
        plt.yscale("log")
    #plt.savefig('ogolne_' + criterion_name)
    plt.savefig('./graphs/'+filename)
    #plt.show()


def astarGraph(data, criterion_nr, criterion_name, filename, strange_numbers):
    plt.clf()

    sum_manh = []
    sum_hamm = []
    for i in range(0, 8):
        sum_manh.append(0.0)
        sum_hamm.append(0.0)
    avg_manh_table = []
    avg_hamm_table = []

    manh = [0.0]*7
    hamm = [0.0]*7

    for d in data:
        if d[2] == 'astr':
            if d[3] == 'manh':
                sum_manh[int(d[0])] += float(d[criterion_nr + 3])
                sum_manh[0] += 1
                manh[int(d[0])-1] += 1.0
            if d[3] == 'hamm':
                sum_hamm[int(d[0])] += float(d[criterion_nr + 3])
                sum_hamm[0] += 1
                hamm[int(d[0])-1] += 1.0

    for i in range(0, 7):
        avg_manh_table.append(sum_manh[i + 1] / manh[i])
        avg_hamm_table.append(sum_hamm[i + 1] / hamm[i])

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x], weights=[avg_manh_table, avg_hamm_table], label=['Manhattan', 'Hamming'], color=['blue', 'purple'],
             bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])
    plt.title('A*')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.legend(('Manhattan', 'Hamming'), loc='upper left')
    if strange_numbers is True:
        plt.yscale("log")
    plt.savefig('./graphs/'+filename)
    #plt.show()


def dfsGraph(data, criterion_nr, criterion_name, filename, strange_numbers):
    plt.clf()

    sum_RDUL = []
    sum_RDLU = []
    sum_DRUL = []
    sum_DRLU = []
    sum_LUDR = []
    sum_LURD = []
    sum_ULDR = []
    sum_ULRD = []
    for i in range(0, 8):
        sum_RDUL.append(0.0)
        sum_RDLU.append(0.0)
        sum_DRUL.append(0.0)
        sum_DRLU.append(0.0)
        sum_LUDR.append(0.0)
        sum_LURD.append(0.0)
        sum_ULDR.append(0.0)
        sum_ULRD.append(0.0)
    avg_RDUL_table = []
    avg_RDLU_table = []
    avg_DRUL_table = []
    avg_DRLU_table = []
    avg_LUDR_table = []
    avg_LURD_table = []
    avg_ULDR_table = []
    avg_ULRD_table = []

    rdul = [0.0]*7
    rdlu = [0.0]*7
    drul = [0.0]*7
    drlu = [0.0]*7
    ludr = [0.0]*7
    lurd = [0.0]*7
    uldr = [0.0]*7
    ulrd = [0.0]*7

    for d in data:
        if d[2] == 'dfs':
            if d[3] == 'rdul':
                sum_RDUL[int(d[0])] += float(d[criterion_nr + 3])
                sum_RDUL[0] += 1
                rdul[int(d[0])-1] += 1
            if d[3] == 'rdlu':
                sum_RDLU[int(d[0])] += float(d[criterion_nr + 3])
                sum_RDLU[0] += 1
                rdlu[int(d[0])-1] += 1
            if d[3] == 'drul':
                sum_DRUL[int(d[0])] += float(d[criterion_nr + 3])
                sum_DRUL[0] += 1
                drul[int(d[0])-1] += 1
            if d[3] == 'drlu':
                sum_DRLU[int(d[0])] += float(d[criterion_nr + 3])
                sum_DRLU[0] += 1
                drlu[int(d[0])-1] += 1
            if d[3] == 'ludr':
                sum_LUDR[int(d[0])] += float(d[criterion_nr + 3])
                sum_LUDR[0] += 1
                ludr[int(d[0])-1] += 1
            if d[3] == 'ludr':
                sum_LURD[int(d[0])] += float(d[criterion_nr + 3])
                sum_LURD[0] += 1
                lurd[int(d[0])-1] += 1
            if d[3] == 'uldr':
                sum_ULDR[int(d[0])] += float(d[criterion_nr + 3])
                sum_ULDR[0] += 1
                uldr[int(d[0])-1] += 1
            if d[3] == 'ulrd':
                sum_ULRD[int(d[0])] += float(d[criterion_nr + 3])
                sum_ULRD[0] += 1
                ulrd[int(d[0])-1] += 1

    for i in range(0, 7):
        avg_RDUL_table.append(sum_RDUL[i+1] / rdul[i])
        avg_RDLU_table.append(sum_RDLU[i+1] / rdlu[i])
        avg_DRUL_table.append(sum_DRUL[i+1] / drul[i])
        avg_DRLU_table.append(sum_DRLU[i+1] / drlu[i])
        avg_LUDR_table.append(sum_LUDR[i+1] / ludr[i])
        avg_LURD_table.append(sum_LURD[i+1] / lurd[i])
        avg_ULDR_table.append(sum_ULDR[i+1] / uldr[i])
        avg_ULRD_table.append(sum_ULRD[i+1] / ulrd[i])

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x, x, x, x, x, x],
             weights=[avg_RDLU_table, avg_RDUL_table, avg_DRUL_table, avg_DRLU_table,
                      avg_LUDR_table, avg_LURD_table, avg_ULDR_table, avg_ULRD_table],
             label=['RDLU', 'RULD', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'],
             color=['grey', 'purple', 'blue', 'lightblue', 'green', 'yellow', 'orange', 'red'],
             bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])
    plt.title('DFS')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.legend(('RDLU', 'RULD', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'), loc='upper left')
    if strange_numbers is True:
        plt.yscale("log")
    plt.savefig('./graphs/'+filename)
    #plt.show()


def bfsGraph(data, criterion_nr, criterion_name, filename, strange_numbers):
    plt.clf()

    sum_RDUL = []
    sum_RDLU = []
    sum_DRUL = []
    sum_DRLU = []
    sum_LUDR = []
    sum_LURD = []
    sum_ULDR = []
    sum_ULRD = []
    for i in range(0, 8):
        sum_RDUL.append(0.0)
        sum_RDLU.append(0.0)
        sum_DRUL.append(0.0)
        sum_DRLU.append(0.0)
        sum_LUDR.append(0.0)
        sum_LURD.append(0.0)
        sum_ULDR.append(0.0)
        sum_ULRD.append(0.0)
    avg_RDUL_table = []
    avg_RDLU_table = []
    avg_DRUL_table = []
    avg_DRLU_table = []
    avg_LUDR_table = []
    avg_LURD_table = []
    avg_ULDR_table = []
    avg_ULRD_table = []

    rdul = [0.0] * 7
    rdlu = [0.0] * 7
    drul = [0.0] * 7
    drlu = [0.0] * 7
    ludr = [0.0] * 7
    lurd = [0.0] * 7
    uldr = [0.0] * 7
    ulrd = [0.0] * 7

    for d in data:
        if d[2] == 'bfs':
            if d[3] == 'rdul':
                sum_RDUL[int(d[0])] += float(d[criterion_nr + 3])
                sum_RDUL[0] += 1
                rdul[int(d[0]) - 1] += 1
            if d[3] == 'rdlu':
                sum_RDLU[int(d[0])] += float(d[criterion_nr + 3])
                sum_RDLU[0] += 1
                rdlu[int(d[0]) - 1] += 1
            if d[3] == 'drul':
                sum_DRUL[int(d[0])] += float(d[criterion_nr + 3])
                sum_DRUL[0] += 1
                drul[int(d[0]) - 1] += 1
            if d[3] == 'drlu':
                sum_DRLU[int(d[0])] += float(d[criterion_nr + 3])
                sum_DRLU[0] += 1
                drlu[int(d[0]) - 1] += 1
            if d[3] == 'ludr':
                sum_LUDR[int(d[0])] += float(d[criterion_nr + 3])
                sum_LUDR[0] += 1
                ludr[int(d[0]) - 1] += 1
            if d[3] == 'ludr':
                sum_LURD[int(d[0])] += float(d[criterion_nr + 3])
                sum_LURD[0] += 1
                lurd[int(d[0]) - 1] += 1
            if d[3] == 'uldr':
                sum_ULDR[int(d[0])] += float(d[criterion_nr + 3])
                sum_ULDR[0] += 1
                uldr[int(d[0]) - 1] += 1
            if d[3] == 'ulrd':
                sum_ULRD[int(d[0])] += float(d[criterion_nr + 3])
                sum_ULRD[0] += 1
                ulrd[int(d[0]) - 1] += 1

    for i in range(0, 7):
        avg_RDUL_table.append(sum_RDUL[i + 1] / rdul[i])
        avg_RDLU_table.append(sum_RDLU[i + 1] / rdlu[i])
        avg_DRUL_table.append(sum_DRUL[i + 1] / drul[i])
        avg_DRLU_table.append(sum_DRLU[i + 1] / drlu[i])
        avg_LUDR_table.append(sum_LUDR[i + 1] / ludr[i])
        avg_LURD_table.append(sum_LURD[i + 1] / lurd[i])
        avg_ULDR_table.append(sum_ULDR[i + 1] / uldr[i])
        avg_ULRD_table.append(sum_ULRD[i + 1] / ulrd[i])

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x, x, x, x, x, x],
             weights=[avg_RDLU_table, avg_RDUL_table, avg_DRUL_table, avg_DRLU_table,
                      avg_LUDR_table, avg_LURD_table, avg_ULDR_table, avg_ULRD_table],
             label=['RDLU', 'RULD', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'],
             color=['grey', 'purple', 'blue', 'lightblue', 'green', 'yellow', 'orange', 'red'],
             bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])
    plt.title('BFS')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.legend(('RDLU', 'RULD', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'), loc='upper left')
    if strange_numbers is True:
        plt.yscale("log")
    plt.savefig('./graphs/'+filename)
    #plt.show()


# method, order/heuristic, solution length, amount visited, amount processed, max depth, execution time

# with open('./data/data.csv', 'rb') as f:
#     enc = chardet.detect(f.read())
# #contents = f.read()
# headlines = ("RuchyOdRozwiazania", "numer_ukladanki", "strategia", "piorytet", "dlugosc_rozw", "odwiedzone", "przetworzone", "max_rekurencja", "czas")
# df = pd.read_csv("./data/data.csv", encoding=enc['encoding'], sep=" ", decimal=".", names=headlines)
# pd.set_option('display.max_columns', None)
# #print(df)
# df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["dlugosc_rozw"].mean()
# print(df2)
# df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["odwiedzone"].mean()
# print(df2)
# df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["przetworzone"].mean()
# print(df2)
# df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["max_rekurencja"].max()
# print(df2)
# df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["czas"].mean()
# print(df2)


with open('./data/data.csv', 'rb') as f:
    enc = chardet.detect(f.read())

with open("./data/data.csv", 'r', encoding=enc['encoding']) as csvfile:
    # Stwórz czytnik csv
    dataFrame = list()
    i=0
    for line in csvfile.readlines():
        array = line.split()
        dataFrame.append(array)

        i += 1
        #list.append(array)

    #print(dataFrame)

# Wyświetl tablicę_dwuwymiarową
for i in range(0,int(dataFrame.__sizeof__()/9)):
    print(dataFrame[i], '\n')



summaryGraph(dataFrame, 1, "Długość rozwiązania", "ogolne_dlugosc_rozwiazania", False)
astarGraph(dataFrame, 1, "Długość rozwiązania", "astr_dlugosc_rozwiazania", False)
bfsGraph(dataFrame, 1, "Długość rozwiązania", "bfs_dlugosc_rozwiazania", False)
dfsGraph(dataFrame, 1, "Długość rozwiązania", "dfs_dlugosc_rozwiazania", False)

summaryGraph(dataFrame, 2, "Liczba stanów odwiedzonych w skali logarytmicznej", "ogolne_odwiedzone", True)
astarGraph(dataFrame, 2, "Liczba stanów odwiedzonych", "astr_odwiedzone", False)
bfsGraph(dataFrame, 2, "Liczba stanów odwiedzonych", "bfs_odwiedzone", False)
dfsGraph(dataFrame, 2, "Liczba stanów odwiedzonych", "dfs_odwiedzone", False)

summaryGraph(dataFrame, 3, "Liczba stanów przetworzonych w skali logarytmicznej", "ogolne_przetworzone", True)
astarGraph(dataFrame, 3, "Liczba stanów przetworzonych", "astr_przetworzone", False)
bfsGraph(dataFrame, 3, "Liczba stanów przetworzonych", "bfs_przetworzone", False)
dfsGraph(dataFrame, 3, "Liczba stanów przetworzonych", "dfs_przetworzone", False)

summaryGraph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "ogolne_głębokość", False)
astarGraph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "astr_głębokość", False)
bfsGraph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "bfs_głębokość", False)
dfsGraph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "dfs_głębokość", False)

summaryGraph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms] w skali logarytmicznej", "ogolne_czas", True)
astarGraph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms]", "astr_czas", False)
bfsGraph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms]", "bfs_czas", False)
dfsGraph(dataFrame, 5, "Czas trwania procesu obliczeniowego [ms]", "dfs_czas", False)

