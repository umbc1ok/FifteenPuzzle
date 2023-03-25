import sys

import Board
import bfs
import dfs
import astar
import saver
import reader
import time

#START ARGUMENTS
algorithmType = sys.argv[1]
moveSequence = sys.argv[2]
readFilePath = sys.argv[3]
solutionFilePath = sys.argv[4]
statsFilePath = sys.argv[5]


boardArray = reader.parseFromFile(readFilePath)
boardW = reader.parseWidth(readFilePath)
boardH = reader.parseHeight(readFilePath)
board = Board.Board(boardW,boardH,boardArray)


if algorithmType == "bfs":
    solver = bfs.bfs()
    solvingStartTime = time.time_ns()                      #czas ma byc w nano
    solutionSequence = solver.solve(board,moveSequence)
    solvingTime = time.time_ns()-solvingStartTime
    solvingTime = solvingTime / 1000000
    saver.saveToFile(solver.found, solutionFilePath, statsFilePath, solver.solution, solver.visited.__len__(), solver.counter,
                     solver.reachedDepth, solvingTime)
elif algorithmType == "dfs":
    solver = dfs.dfs()
    solvingStartTime = time.time_ns()
    solutionSequence = solver.solve(board,0,20,"","", moveSequence)
    solvingTime = time.time_ns() - solvingStartTime
    solvingTime = solvingTime / 1000000
    saver.saveToFile(solver.found, solutionFilePath, statsFilePath, solver.solution, solver.counter, solver.visited.__len__(),

                     solver.reachedDepth, solvingTime)
elif algorithmType == "astar":
    solver = astar.astar(moveSequence)
    solvingStartTime = time.time_ns()
    solutionSequence = solver.solve(board,"","")
    solvingTime = time.time_ns() - solvingStartTime
    solvingTime = solvingTime / 1000000
    saver.saveToFile(solver.found, solutionFilePath, statsFilePath, solver.solution, solver.counter, solver.visited.__len__(),

                     solver.reachedDepth, solvingTime)





