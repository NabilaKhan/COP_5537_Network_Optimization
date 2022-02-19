import random
import numpy as np
import sys
import math



A = []                              ### Will hold the weighted adjacency matrix
positive_infinity = math.inf        ### Define positive infinite value
Node_no = 0


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
        
    node_no = len(vetex_list)
    fin.close()
    return node_no


### Returns the vertex with minimum distance
def Min_dis(distance, color):
    
    mn_val = positive_infinity
    min_ind = -1

    for v in range(0, Node_no):
        if color[v] == 0 and distance[v] < mn_val:
            mn_val = distance[v]
            min_ind = v

    return min_ind


### Returns the number of visited nodes
def Prims(source, visited_nodes):
    
    distance = np.zeros(Node_no)
    parent = np.zeros(Node_no)
    
    for i in range(0, Node_no):
        distance[i] = positive_infinity
        parent[i] = -1

    count = 0
    distance[source] = 0

    for k in range(0, Node_no):
        
        u = Min_dis(distance, visited_nodes)
        if u != -1: # If vertex not connected in graph, then distance of that vertex will be infinity and Min_dis(distance, visited_nodes) function will return index -1
            visited_nodes[u] = 1
            count += 1
        
            for v in range(0, Node_no):
                if visited_nodes[v] == 0 and A[u][v] > 0 and A[u][v] < distance[v]:
                    distance[v] = A[u][v]
                    parent[v] = u
    return count
    
        

### Determines if an edge is a bridge edge
def Bridge_edge(u, v):
    
    degree_v = 0
    for e in range(0, Node_no):
        
        if A[v][e]:
            degree_v += 1

    if degree_v >= 1:
        return 0
    return 1
            
          
### Fleury's Algorithm        
def FleuryAlgo(start, node_count):
    
    vertex_count = node_count

    for v in range(0, Node_no):
        if A[start][v]:
            
            visited_nodes = np.zeros(Node_no)
            # Temporarily removing edge to check if graph gets disconnected
            A[start][v] = 0
            A[v][start] = 0
            
            visited_count = Prims(v, visited_nodes)

            # Check if Graph gets separated into two sets of disconnected edges after removing edge (start,v)
            if abs(vertex_count - visited_count) <= 1:
                print(", ", v, end = '')
                fout.write(", %d" %(v))
                
                if Bridge_edge(start, v):
                    vertex_count -= 1                
                if Bridge_edge(v, start):
                    vertex_count -= 1

                # Remove edge (start, v)
                A[start][v] = 0
                A[v][start] = 0
                
                FleuryAlgo(v, vertex_count)
            else:
                # Not removing edge (start, v)
                A[start][v] = 1
                A[v][start] = 1                
                
    
    

if __name__ == "__main__":

    fout = open("New_Results/Output.txt", "w")
    input_file_name = sys.argv[1]
    start = int(sys.argv[2])
    
    Node_no = read_input(input_file_name)
  
    print(start, end = '')
    fout.write("%d" %(start))
    FleuryAlgo(start, Node_no)
    
    fout.close()
