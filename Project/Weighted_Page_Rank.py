import random
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import networkx as nx


A = nx.DiGraph() 


### Read input (webpage list and adjacency matrix)
def read_input(input_file_name):
    fin = open(input_file_name + ".txt", "r")
    edge_list = []

    for l in range(0,3):
        line = fin.readline()

    line = line.split(" ")
    nodes, edges = int(line[2]), int(line[4])
    line = fin.readline()
    
    while(True):
        line = fin.readline()
        line = line.strip('\n')
        if line == "":
            break
        node1, node2 = line.split("\t")
        edge_list.append((int(node1), int(node2)))

    A.add_edges_from(edge_list)
    fin.close()
    return nodes



### Returns the list of neighbor nodes having directed edge to (indegree) and from (outdegree) each webpage node
def Digraph_degree_generate(n):
    indegree = [[] for i in range(n+1)]
    outdegree = [[] for i in range(n+1)]

    for edge in list(A.edges()):
        (node1, node2) = edge
        outdegree[node1].append(node2)
        indegree[node2].append(node1)

    return indegree, outdegree
    


def Win(page_index, page, n):
    sum_in = 0
    indegree, outdegree = Digraph_degree_generate(n)
    indeg_page = len(indegree[page])
    outdeg_pageindex = outdegree[page_index]

    for k in range(0, len(outdeg_pageindex)):
        node_ref = outdeg_pageindex[k]
        sum_in = sum_in + len(indegree[node_ref])

    if sum_in != 0:
        return indeg_page / sum_in
    else:
        return 1



def Wout(page_index, page, n):
    sum_out = 0
    indegree, outdegree = Digraph_degree_generate(n)
    outdeg_page = len(outdegree[page])
    outdeg_pageindex = outdegree[page_index]

    for k in range(0, len(outdeg_pageindex)):
        node_ref = outdeg_pageindex[k]
        sum_out = sum_out + len(outdegree[node_ref])


    if sum_out == 0:
        for k in range(0, len(outdeg_pageindex)):
            node_ref = outdeg_pageindex[k]
            sum_out = sum_out + len(outdegree[node_ref])
            
    if sum_out != 0:
        return outdeg_page / sum_out
    else:
        return 1


    
### PageRank Algorithm
def Page_rank_iter(n, d, e, max_iter):
    R_cur = [(i, 1.0/n) for i in range(n+1)]
    cons_D = (1 - d) / n
    indegree, outdegree = Digraph_degree_generate(n)

    for iter_no in range(1, max_iter):
        
        R_next = [(i, 0) for i in range(n+1)]
        
        for page in range(0, n+1):
            if page == 0:
                continue
            PR_sum = 0
            for page_index in indegree[page]:
                PR_sum += R_cur[page_index][1] * Win(page_index, page, n) * Wout(page_index, page, n)
            R_next[page] = (page, cons_D + d * PR_sum)

        ### Check for convergence
        R_diff = sum([abs(r1[1] - r2[1]) for (r1, r2) in zip(R_cur, R_next)])
        
        if R_diff < e:
            break
        R_cur = R_next

    return iter_no, R_next
        


### Prints and writes final output        
def write_output(iter_no, R, Step):
    fout = open("Output/Weighted_output.txt", "w")
    R.sort(key=lambda x:x[1], reverse = True)
    
    print("number of iterations: ", iter_no, "\n")
    print("ranking: ")
    for r in range(0, Step):
        print(R[r], end = ',')

        
    Weightd_Pagerank = []
    fout.write("number of iterations: " + str(iter_no) + "\n\n")
    for r in range(0, Step):
        if r == Step - 1:
            fout.write(str(R[r])+ ".")
        else:
            fout.write(str(R[r])+ ", ")
        Weightd_Pagerank.append(R[r])
    fout.close()
    
    ### Printing list of top nodes
    f_top = open('Output/Top_node_list.txt', 'a')
    f_top.write("Weighted PageRank Nodes:\n")
    f_top.write(str(Weightd_Pagerank) + "\n")
    f_top.close()
        
    

if __name__ == "__main__":

    ### User Input 
    input_file_name = sys.argv[1]
    d = float(sys.argv[2])
    e = float(sys.argv[3])
    max_iter = int(sys.argv[4])
    Step = int(sys.argv[5])
    
    Node_no = read_input(input_file_name)                   ### Reading adjacency matrix from input file
    iter_no, R = Page_rank_iter(Node_no, d, e, max_iter)    ### Running PageRank Algorithm
    write_output(iter_no, R, Step)                                ### Writing output to file


    
