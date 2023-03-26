from _csv import reader

import chardet as chardet
import matplotlib.pyplot as plt
import pandas as pd

def summaryGraph(data, criterion_nr, criterion_name):
    plt.clf()

    sum_astar = []  # pierwsze dla ilości zliczonych obiektów, reszta to głębokość rozwiązania = index
    sum_bfs = []
    sum_dfs = []
    for i in range(0, 8):
        sum_astar[i] = 0.0
        sum_bfs[i] = 0.0
        sum_dfs[i] = 0.0
    avg_astar_table = []
    avg_bfs_table = []
    avg_dfs_table = []

    for d in data:
        if d[0] == 'astar':
            sum_astar[d[2] - 1] += float(d[criterion_nr + 1])
            # indeks kryterium bo kryteria zaczynają się od data[2] a kryteria numerujemy od 1
            sum_astar[0] += 1
        if d[0] == 'bfs':
            sum_bfs[d[2] - 1] += float(d[criterion_nr + 1])
            sum_bfs[0] += 1
        if d[0] == 'dfs':
            sum_dfs[d[2] - 1] += float(d[criterion_nr + 1])
            sum_dfs[0] += 1

    for i in range(0, 7):
        avg_astar_table[i] = sum_astar[i + 1] / sum_astar[0]
        avg_bfs_table[i] = sum_bfs[i + 1] / sum_bfs[0]
        avg_dfs_table[i] = sum_dfs[i + 1] / sum_dfs[0]

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x], weights=[avg_astar_table, avg_bfs_table, avg_dfs_table], label=['A*', 'BFS', 'DFS'],
             color=['blue', 'purple', 'green'])
    plt.title('Ogólne')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.savefig('ogolne_' + criterion_name)


def astarGraph(data, criterion_nr, criterion_name):
    plt.clf()

    sum_manh = []
    sum_hamm = []
    for i in range(0, 8):
        sum_manh[i] = 0.0
        sum_hamm[i] = 0.0
    avg_manh_table = []
    avg_hamm_table = []

    for d in data:
        if d[0] == 'astar':
            if d[1] == 'manh':
                sum_manh[d[2] - 1] += float(d[criterion_nr + 1])
                sum_manh[0] += 1
            if d[1] == 'hamm':
                sum_hamm[d[2] - 1] += float(d[criterion_nr + 1])
                sum_hamm[0] += 1

    for i in range(0, 7):
        avg_manh_table[i] = sum_manh[i + 1] / sum_manh[0]
        avg_hamm_table[i] = sum_hamm[i + 1] / sum_hamm[0]

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x], weights=[avg_manh_table, avg_hamm_table], label=['Manhattan', 'Hamming'], color=['blue', 'purple'])
    plt.title('A*')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.savefig('astar_' + criterion_name)


def dfsGraph(data, criterion_nr, criterion_name):
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
        sum_RDUL[i] = 0.0
        sum_RDLU[i] = 0.0
        sum_DRUL[i] = 0.0
        sum_DRLU[i] = 0.0
        sum_LUDR[i] = 0.0
        sum_LURD[i] = 0.0
        sum_ULDR[i] = 0.0
        sum_ULRD[i] = 0.0
    avg_RDUL_table = []
    avg_RDLU_table = []
    avg_DRUL_table = []
    avg_DRLU_table = []
    avg_LUDR_table = []
    avg_LURD_table = []
    avg_ULDR_table = []
    avg_ULRD_table = []

    for d in data:
        if d[0] == 'dfs':
            if d[1] == 'RDUL':
                sum_RDUL[d[2] - 1] += float(d[criterion_nr + 1])
                sum_RDUL[0] += 1
            if d[1] == 'RDLU':
                sum_RDLU[d[2] - 1] += float(d[criterion_nr + 1])
                sum_RDLU[0] += 1
            if d[1] == 'DRUL':
                sum_DRUL[d[2] - 1] += float(d[criterion_nr + 1])
                sum_DRUL[0] += 1
            if d[1] == 'DRLU':
                sum_DRLU[d[2] - 1] += float(d[criterion_nr + 1])
                sum_DRLU[0] += 1
            if d[1] == 'LUDR':
                sum_LUDR[d[2] - 1] += float(d[criterion_nr + 1])
                sum_LUDR[0] += 1
            if d[1] == 'LURD':
                sum_LURD[d[2] - 1] += float(d[criterion_nr + 1])
                sum_LURD[0] += 1
            if d[1] == 'ULDR':
                sum_ULDR[d[2] - 1] += float(d[criterion_nr + 1])
                sum_ULDR[0] += 1
            if d[1] == 'ULRD':
                sum_ULRD[d[2] - 1] += float(d[criterion_nr + 1])
                sum_ULRD[0] += 1

    for i in range(0, 7):
        avg_RDUL_table[i] = sum_RDUL[i+1] / sum_RDLU[0]
        avg_RDLU_table[i] = sum_RDLU[i+1] / sum_RDLU[0]
        avg_DRUL_table[i] = sum_DRUL[i+1] / sum_DRUL[0]
        avg_DRLU_table[i] = sum_DRLU[i+1] / sum_DRLU[0]
        avg_LUDR_table[i] = sum_LUDR[i+1] / sum_LUDR[0]
        avg_LURD_table[i] = sum_LURD[i+1] / sum_LURD[0]
        avg_ULDR_table[i] = sum_ULDR[i+1] / sum_ULDR[0]
        avg_ULRD_table[i] = sum_ULRD[i+1] / sum_ULRD[0]

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x, x, x, x, x, x],
             weights=[avg_RDLU_table, avg_RDUL_table, avg_DRUL_table, avg_DRLU_table,
                      avg_LUDR_table, avg_LURD_table, avg_ULDR_table, avg_ULRD_table],
             label=['RDLU', 'RULD', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'],
             color=['grey', 'purple', 'blue', 'green', 'yelow', 'orange', 'red'])
    plt.title('DFS')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.savefig('dfs_' + criterion_name)


def bfsGraph(data, criterion_nr, criterion_name):
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
        sum_RDUL[i] = 0.0
        sum_RDLU[i] = 0.0
        sum_DRUL[i] = 0.0
        sum_DRLU[i] = 0.0
        sum_LUDR[i] = 0.0
        sum_LURD[i] = 0.0
        sum_ULDR[i] = 0.0
        sum_ULRD[i] = 0.0
    avg_RDUL_table = []
    avg_RDLU_table = []
    avg_DRUL_table = []
    avg_DRLU_table = []
    avg_LUDR_table = []
    avg_LURD_table = []
    avg_ULDR_table = []
    avg_ULRD_table = []

    for d in data:
        if d[0] == 'bfs':
            if d[1] == 'RDUL':
                sum_RDUL[d[2] - 1] += float(d[criterion_nr + 1])
                sum_RDUL[0] += 1
            if d[1] == 'RDLU':
                sum_RDLU[d[2] - 1] += float(d[criterion_nr + 1])
                sum_RDLU[0] += 1
            if d[1] == 'DRUL':
                sum_DRUL[d[2] - 1] += float(d[criterion_nr + 1])
                sum_DRUL[0] += 1
            if d[1] == 'DRLU':
                sum_DRLU[d[2] - 1] += float(d[criterion_nr + 1])
                sum_DRLU[0] += 1
            if d[1] == 'LUDR':
                sum_LUDR[d[2] - 1] += float(d[criterion_nr + 1])
                sum_LUDR[0] += 1
            if d[1] == 'LURD':
                sum_LURD[d[2] - 1] += float(d[criterion_nr + 1])
                sum_LURD[0] += 1
            if d[1] == 'ULDR':
                sum_ULDR[d[2] - 1] += float(d[criterion_nr + 1])
                sum_ULDR[0] += 1
            if d[1] == 'ULRD':
                sum_ULRD[d[2] - 1] += float(d[criterion_nr + 1])
                sum_ULRD[0] += 1

    for i in range(0, 7):
        avg_RDUL_table[i] = sum_RDUL[i + 1] / sum_RDLU[0]
        avg_RDLU_table[i] = sum_RDLU[i + 1] / sum_RDLU[0]
        avg_DRUL_table[i] = sum_DRUL[i + 1] / sum_DRUL[0]
        avg_DRLU_table[i] = sum_DRLU[i + 1] / sum_DRLU[0]
        avg_LUDR_table[i] = sum_LUDR[i + 1] / sum_LUDR[0]
        avg_LURD_table[i] = sum_LURD[i + 1] / sum_LURD[0]
        avg_ULDR_table[i] = sum_ULDR[i + 1] / sum_ULDR[0]
        avg_ULRD_table[i] = sum_ULRD[i + 1] / sum_ULRD[0]

    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x, x, x, x, x, x],
             weights=[avg_RDLU_table, avg_RDUL_table, avg_DRUL_table, avg_DRLU_table,
                      avg_LUDR_table, avg_LURD_table, avg_ULDR_table, avg_ULRD_table],
             label=['RDLU', 'RULD', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'],
             color=['grey', 'purple', 'blue', 'green', 'yelow', 'orange', 'red'])
    plt.title('BFS')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(criterion_name)
    plt.savefig('bfs_' + criterion_name)


# method, order/heuristic, solution length, amount visited, amount processed, max depth, execution time

with open('./data/data.csv', 'rb') as f:
    enc = chardet.detect(f.read())
#contents = f.read()
headlines = ("RuchyOdRozwiazania", "numer_ukladanki", "strategia", "piorytet", "dlugosc_rozw", "odwiedzone", "przetworzone", "max_rekurencja", "czas")
df = pd.read_csv("./data/data.csv", encoding=enc['encoding'], sep=" ", decimal=".", names=headlines)
pd.set_option('display.max_columns', None)
#print(df)
df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["dlugosc_rozw"].mean()
print(df2)
df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["odwiedzone"].mean()
print(df2)
df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["przetworzone"].mean()
print(df2)
df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["max_rekurencja"].mean()
print(df2)
df2 = df.groupby(["RuchyOdRozwiazania","strategia"])["czas"].mean()
print(df2)

