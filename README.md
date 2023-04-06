# FifteenPuzzle

This is a repository for a **Artifficial Intelligence and Expert Systems** course taught at **Technical University of Lodz**.

The goal was to make a Fifteen Puzzle solver using 3 different alogrithms:
* DFS (Depth First Search)
* BFS (Breadth First Search)
* A* (A star)

On top of that, we were supposed to gather and analyze a bunch of statistics including program's runtime and number of processed states.

The program can be run in commandline:  

*py main.py strategy heuristic/order puzzleSourceFile solutionFile statsFile*

**Strategy**: bfs, dfs, astr  
**Heurisitc:** manh, hamm (use with **astr**)  
**Order:** Any permutation of **RDUL** letters (it is the order in which the algorithm adds moves to the queue)  
**puzzleSourceFile:** File, where the puzzle you want solved is. (look at **uklad** file to see the pattern)  
**solutionFile:** file in which you want the solution solved  
**statsFile:** file in which additional stats will be saved  
