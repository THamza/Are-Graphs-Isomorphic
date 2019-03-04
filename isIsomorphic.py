#Important Assumption: -The input graph is directed.
#                      -For the input graph to be similar to the one I received by email,
#                        ALL the edges must be similar; in other words, having
#                        a single directional edge to a vertex is not enough
import OriginalGraph as o
import functions as fun

#Building the adjacency list of the input graph
#Given the number of vertices and edges + the edges
numberOfVertices = eval(input("Number of vertices> "))
numberOfEdges = eval(input("Number of edges> "))


print("Please enter all of the ",numberOfEdges," edges:")
AdjList = fun.BuildAdjList(numberOfVertices,numberOfEdges)

def isIso():
    #First we check if the number of vertices match
    if(numberOfVertices!=o.numberOfVerticesOriginal):
        return False
    #Then we check if the number of edges match
    if(numberOfEdges!=o.numberOfEdgesOriginal):
        return False
    degrees = fun.getDegrees(AdjList)
    if not fun.isDegreeMatch(o.degreesOriginal,degrees):
        return False

    root = fun.findRoot(AdjList)
    if(root == -1):#In case there is no unique vertex with exactly 3 edges
        return False
    #check degree of the second level
    secondLevel = []
    #This is equivalent to running a BFS to get the second level only
    #degrees[root] is supposed to be 3
    for i in range(0,degrees[root]):
        secondLevel.append(AdjList[root][i])
        #From the graph drawn in OriginalGraph.py this is equivalent to checking
        #if the vertices 2,3, and 4 are of degree 4 (1 edge with which they are
        #connected to the root and 3 others connected to their 3 children respectively)
        if (degrees[AdjList[root][i]-1]!=4):
            return False

    #Let's check if the third level is correct
    #all the vertices in the third level must have a degree of 1 as they are
    #connected to their parents only
    #Lets check the degree of each element in the third level using the secondLevel[]
    #and make sure that every leaf is connected to the correct parent
    count3degree = 0
    for i in range(0, len(secondLevel)):
        edges = AdjList[secondLevel[i]-1]
        for j in range(0,len(edges)):
            #on degree shoudl be 3 (the root) while the remaining should be 1
            if (degrees[edges[j]-1] == 1) or (degrees[edges[j]-1] == 3):
                if(degrees[edges[j]-1] == 3):
                    count3degree += 1
                if count3degree > 1:
                    return False
                #Making sure that every leaf is connected to the correct parent
                if(degrees[edges[j]-1] == 1):
                    if(AdjList[edges[j]-1][0] != secondLevel[i]):
                        return False
            else:
                return False
        count3degree = 0



    #If it has passed all those tests; then the input graph is isomorphic to the
    #one in OriginalGraph (The one sent by e-mail)
    return True


if(isIso()):
    print("This graph is SIMILAR to the one I received by E-mail")
else:
    print("This graph is DIFFERENT to the one I received by E-mail")
