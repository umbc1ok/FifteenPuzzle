import subprocess, sys



tab = ["RDUL", "RDLU", "DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]
#tab = ["RDLU", "DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]



for i in tab:

    p = subprocess.Popen(["powershell.exe", f"C:\\Users\\Hubert\\source\\repos\\FifteenPuzzle\\files\\uklady\\przeszukiwania.ps1 -strategy bfs -param {i}"], stdout=sys.stdout)
    p.communicate()

