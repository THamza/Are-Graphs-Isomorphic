#Find the root if it exists then run dfs
def findRoot(AdjList):
    #count of vertices that are connected to exactly 3 other vertices
    count = 0
    index = -1
    #This assures that there is only 1 vertex of degree 3 which is the root of
    #this tree
    for i in range(0,len(AdjList)):
        if(len(AdjList[i])==3):
            index = i
            count +=1

    if(count==1):
        #Handling the case where one of the 3 edges goes to the same vertex
        #Or that one of the edges leads to the root itself
        if (AreAllElementsUnique(AdjList[index])) and (index not in AdjList[index]):
            return index

    return -1

def AreAllElementsUnique(list):
    flag = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                if list[i] == list[j]:
                    flag = 1
    if(flag) :
        return False
    return True

def BuildAdjList(numberOfVertices,numberOfEdges):
    AdjList = []
    for i in range(numberOfVertices):
        AdjList.append([])

    for i in range(0,numberOfEdges):
    	vertex1, vertex2 = map(int, input().split())
    	AdjList[vertex1-1].append(vertex2)
    return AdjList

def getDegrees(AdjList):
    deg = []
    for i in range(len(AdjList)):
        deg.append(len(AdjList[i]))
    return deg

def isDegreeMatch(degreesOriginal,degrees):
    if(len(degreesOriginal) != len(degrees)):
        return False

    length = len(degreesOriginal)
    degreesCopy = degrees.copy()

    for i in range(0,length):
        for j in range(0,length):
            if(degreesOriginal[i] == degreesCopy[j]):
                degreesCopy[j] = -1
                break
    #Check if all the elements are equal and that one of them is equal to -1
    #This means that all the degrees are equal to -1
    return ((degreesCopy[1:] == degreesCopy[:-1]) and degreesCopy[0]==-1)
