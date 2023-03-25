def saveSollutionToFile(solved, filename, sollution):
    f = open("./files/zapisane/"+filename, 'w')
    if solved is True:
        f.write(str(len(sollution)))
        f.write('\n'+sollution)
        f.close()
    else:
        f.write('-1')
        f.close()


def saveAdditionalInfoToFile(solved, filename, sollution, visited, processed, maxDepth, execTime):
    f = open("./files/zapisane/"+filename, 'w')
    if solved is True:
        f.write(str(len(sollution)))
    else:
        f.write('-1')

    f.write('\n' + str(visited))
    f.write('\n' + str(processed))
    f.write('\n' + str(maxDepth))
    time = round(execTime, 3)
    f.write('\n' + str(time))
    f.close()

def saveToFile(solved, f1, f2, sollution, visited, processed, maxDepth, execTime):
    saveSollutionToFile(solved, f1, sollution)
    saveAdditionalInfoToFile(solved, f2, sollution, visited, processed, maxDepth, execTime)