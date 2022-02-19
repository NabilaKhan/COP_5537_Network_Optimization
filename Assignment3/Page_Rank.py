import random
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import networkx as nx


A = []                              ### Will hold the adjacency matrix
Node_no = 0


##def show_graph_with_labels(adjacency_matrix, mylabels, n):
##    edges = []
##
##    for row in range(n):
##        for col in range(n):
##            if adjacency_matrix[row][col] == 1:
##                edges.append((row,col))
##
##   
##    gr = nx.DiGraph()
##    gr.add_edges_from(edges)
##    rank_list = nx.pagerank(gr)
##    rank_list = sorted(rank_list.items(), key=lambda item: item[1], reverse = True)
##    print(rank_list)
    

### Read input (webpage list and adjacency matrix)
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



### Returns the list of neighbor nodes having directed edge to (indegree) and from (outdegree) each webpage node
def Digraph_degree_generate(n):
    indegree = [[] for i in range(n)]
    outdegree = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                outdegree[i].append(j)
                indegree[j].append(i)

    return indegree, outdegree
    


### PageRank Algorithm
def Page_rank_iter(n, d, e, max_iter):
    R_cur = [(i, 1.0/n) for i in range(n)]
    cons_D = (1 - d) / n
    indegree, outdegree = Digraph_degree_generate(n)

    for iter_no in range(1, max_iter):
        
        R_next = [(i, 0) for i in range(n)]
        
        for page in range(0, n):
            PR_sum = 0
            for page_index in indegree[page]:
                PR_sum += R_cur[page_index][1]/len(outdegree[page_index])
            R_next[page] = (page, cons_D + d * PR_sum)

        ### Check for convergence
        R_diff = sum([abs(r1[1] - r2[1]) for (r1, r2) in zip(R_cur, R_next)])
        
        if R_diff < e:
            break
        R_cur = R_next

    return iter_no, R_next
        


### Prints and writes final output        
def write_output(iter_no, R):
    fout = open("New_Results/Output.txt", "w")
    R.sort(key=lambda x:x[1], reverse = True)
    
    print("number of iterations: ", iter_no, "\n")
    print("ranking: " + ', '.join(str(x) + ' (' + str(round(y, 4)) + ")" for x, y in R) + '.')
    
    fout.write("number of iterations: " + str(iter_no) + "\n\n")
    fout.write("ranking: " + str(', '.join(str(x) + ' (' + str(round(y, 4)) + ")" for x, y in R)) + '.')
    fout.close()

        
    

if __name__ == "__main__":

    ### User Input 
    input_file_name = sys.argv[1]
    d = float(sys.argv[2])
    e = float(sys.argv[3])
    max_iter = int(sys.argv[4])

##    input_file_name = "A"
##    d = 0.85
##    e = 0.000001
##    max_iter = 100
    
    Node_no = read_input(input_file_name)                   ### Reading adjacency matrix from input file
    iter_no, R = Page_rank_iter(Node_no, d, e, max_iter)    ### Running PageRank Algorithm
    write_output(iter_no, R)                                ### Writing output to file

    ### Verifying output using PageRank function in python networkx module
##    node_list = [i for i in range(Node_no)]
##    show_graph_with_labels(A, node_list, Node_no)

    
