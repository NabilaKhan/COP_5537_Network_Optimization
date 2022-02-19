import random
import numpy as np
import sys
import math


A = []                              ### Will hold the weighted adjacency matrix
path_list = []                      ### Will hold shortest path reported by the Dijkstra algorithm
positive_infinity = math.inf        ### Define positive infinite value


### Read input (vertex list and adjacency matrix)
def read_input(input_file_name):
    fin = open(input_file_name + ".txt", "r")
    vetex_list = []
      
    while(True):
        line = fin.readline()
        if line == "":
            break
        line = line.split("\t")
        vetex_list.append(line[0])
        weight_list = line[1].strip("\n").split(",")
        weight_list = list(map(int, weight_list))
        A.append(weight_list)
        
    fin.close()
    return vetex_list


        
### Returns the non-visited vertex v with minimum distance
def Min_dis_vertex(n, color, distance):

    min_val = positive_infinity
    index = -1

    ### If vertex v not visited and distance assigned to it is minimum then return v for next visit
    for v in range(0,n):
        if color[v] == 0 and distance[v] < min_val:
            min_val = distance[v]
            index = v
    return index
        
    

### Dijkstra's Algorithm    
def dijkstra(s, e, n, distance, parent, color):
    ### Initialize all the vertices
    for v in range(0,n):
        parent[v] = -1                                  ### Parent of vertices not assigned yet
        color[v] = 0                                    ### Vertices not visited yet
        distance[v] = positive_infinity                 ### Distance of vertices from source not calculated yet

    distance[s] = 0                                     ### Starting traversing the graph from the source

    for i in range(0,n):
        v = Min_dis_vertex(n, color, distance)                       ### Returning the vertex with minimum distance
        color[v] = 1                                    ### Marking vertex v as visited

        for u in range(0, n):
            if A[v][u] > 0 and color[u] == 0 and distance[u] > distance[v] + A[v][u]:
                distance[u] =  distance[v] + A[v][u]    ### Updating distance of u
                parent[u] = v                           ### Assigning v as u's parent

    return distance[e], distance, parent, color



### Print Shorted path between source and destination using recursion
def Print_shortest_path(parent, j):

    if parent[j] == -1:
        path_list.append(j)
        return
    else:
        Print_shortest_path(parent, int(parent[j]))
    path_list.append(j)



### Calculates shortest path reported by the Dijkstra algorithm
def output_print(source, destination, minimum_distance, path_list):

    fresult = open("New_Results/" + str(source) + "_" + str(destination) + ".txt", "w")   ### Print output in Results folder
    
    fout.write("%d, %d\n" %(source, destination))
    fresult.write("%d, %d\n" %(source, destination))
    print("%d, %d" %(source, destination))
    
    if source == destination:
        path_list.append(source)    
   
    for p in range(0, len(path_list)):
        if p < len(path_list) - 1:
            fout.write("%d, " %(path_list[p]))
            fresult.write("%d, " %(path_list[p]))
            print("%d," %(path_list[p]), end=' ')
        else:
            fout.write("%d" %(path_list[p]))
            fresult.write("%d" %(path_list[p]))
            print("%d" %(path_list[p]))
    fout.write("\n")
    fresult.write("\n")

    fout.write("%d\n" %(int(minimum_distance)))
    fresult.write("%d\n" %(int(minimum_distance)))
    print("%d\n" %(int(minimum_distance)))

    fresult.close()

    
### Running Dijkstra for PID   
def Dijkstra_with_PID(PID, input_file_name):
    ### Reporting the results of five pairs of starting and ending vertices based on seven-digit PID 
    for i in range(0, len(PID)-2):
        s = int(PID[i:i+2])         ### Source node
        e = int(PID[i+1:i+3])       ### Destination node

        ### Initialization
        distance = np.zeros(100)    ### Holds the distance of vertices from source
        parent = np.zeros(100)      ### Stores parents nodes of all the nodes
        color = np.zeros(100)       ### Indicates if the node has already been visited or not
        V = []                      ### List of vertices

        ### Calling the functions
        V = read_input(input_file_name)
        n = len(V)                  ### Total number of Vertex

        minimum_distance, distance, parent, color = dijkstra(s, e, n, distance, parent, color)
        Print_shortest_path(parent, e)
        
        output_print(s, e, minimum_distance, path_list)

        A.clear()
        path_list.clear()
        fout.write("\n\n\n")


### Running Dijkstra for user given source and destination   
def Dijkstra_without_PID(s, e, input_file_name):

    ### Initialization
    distance = np.zeros(100)    ### Holds the distance of vertices from source
    parent = np.zeros(100)      ### Stores parents nodes of all the nodes
    color = np.zeros(100)       ### Indicates if the node has already been visited or not
    V = []                      ### List of vertices

    ### Calling the functions
    V = read_input(input_file_name)
    n = len(V)                  ### Total number of Vertex

    minimum_distance, distance, parent, color = dijkstra(s, e, n, distance, parent, color)
    Print_shortest_path(parent, e)
    
    output_print(s, e, minimum_distance, path_list)

          
        
    
    

if __name__ == "__main__":

    fout = open("Output.txt", "w")
    
    ### Handling input arguments
    if(len(sys.argv) == 3):     ### Argument 1 = PID, Argument 2 = File name
        PID = sys.argv[1]
        input_file_name = sys.argv[2]
        print("Given 2 arguments. Please check the file Output.txt for output")
        print("\nOutput:")
        Dijkstra_with_PID(PID, input_file_name)
        
    elif(len(sys.argv) == 4):   ### Argument 1 = source, Argument 2 = destination, Argument 3 = File name
        s = int(sys.argv[1])
        e = int(sys.argv[2])
        input_file_name = sys.argv[3]
        print("Given 3 arguments. Please check the file Output.txt for output")
        print("\nOutput:")
        Dijkstra_without_PID(s, e, input_file_name)
        
    else:                       ### No Arguments
        print("Not enough number of arguments! Running for default values: PID = '5067496', input_file = 'Data.txt'")
        PID = '5067496'
        input_file_name = "Data"
        print("Please check the file Output.txt for output")
        print("\nOutput:")
        Dijkstra_with_PID(PID, input_file_name)
        
    fout.close()
