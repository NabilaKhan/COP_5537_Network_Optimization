import os
import sys
import copy
import argparse
import math
import statistics as st
import networkx as nx

INF = 9999
G = nx.DiGraph()
Node_map_dic = {}


### Read input (webpage list and adjacency matrix)
def read_input(input_file_name):
    fin = open(input_file_name + ".txt", "r")
    edge_list = []

    for l in range(0,3):
        line = fin.readline()

    line = line.split(" ")
    nodes, edges = int(line[2]), int(line[4])
    line = fin.readline()
    input_dic = {}
    
    while(True):
        line = fin.readline()
        line = line.strip('\n')
        if line == "":
            break
        node1, node2 = line.split("\t")
        
        edge_list.append((int(node1), int(node2)))

    G.add_edges_from(edge_list)
    fin.close()
    return nodes



### HITS Algorithm
def HITS_algo(A, n, indegree, outdegree, max_iter, e):
    authority_t1 = [1.0/math.sqrt(n) for i in range(n)]
    hub_t1 = [1.0/math.sqrt(n) for i in range(n)]

    for iter_no in range(max_iter):
        
        authority_t2 = []
        hub_t2 = []

        for i in range(n):
            tot_hub = 0
            for ind in indegree[i]:
                tot_hub += hub_t1[ind]
            authority_t2.append(tot_hub)
               
            tot_authority = 0
            for outd in outdegree[i]:
                tot_authority += authority_t1[outd]
            hub_t2.append(tot_authority)
                
        norm_auth = sum(authority_t2)
        norm_hub = sum(hub_t2)
            
        for i in range(n):
            authority_t2[i] = authority_t2[i] / norm_auth
            hub_t2[i] = hub_t2[i] / norm_hub

        authority_diff = [abs(x - y) ** 2 for (x, y) in zip(authority_t1, authority_t2)]
        hub_diff = [abs(x - y) ** 2 for (x, y) in zip(hub_t1, hub_t2)]

        if sum(authority_diff) < e and sum(hub_diff) < e:
            break

        authority_t1 = copy.deepcopy(authority_t2)
        hub_t1 = copy.deepcopy(hub_t2)

    
    authority_tuples = []
    hub_tuples = []
    for i in range(n):
      authority_tuples.append((Node_map_dic[i+1], float(authority_t2[i])))
      hub_tuples.append((Node_map_dic[i+1], float(hub_t2[i])))

    return iter_no+1, sorted(authority_tuples, key = lambda x: x[1], reverse=True), sorted(hub_tuples, key = lambda x: x[1], reverse=True)




### Generates input and output degree list of nodes
def Generate_Degree_List(A, n, top_no):
    indegree = [[] for i in range(n)]
    outdegree = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if A[i][j] != INF:
                outdegree[i].append(j)
                indegree[j].append(i)

    return indegree, outdegree




if __name__ == '__main__':

    ### User Input
    input_file_name = sys.argv[1]
    e = float(sys.argv[2])
    max_iter = int(sys.argv[3])
    top_no = int(sys.argv[4])
    
    Node_no = read_input(input_file_name)
    Node_no = len(list(G.nodes()))
    print('Total number of nodes: ' + str(Node_no))
    print('Total number of edges: ' + str(len(G.edges())))
    print("\n\n")
    
    Node_list = list(G.nodes())
    for i in range(1, Node_no+1):
        Node_map_dic[i] = int(Node_list[i-1])
      
    A = nx.adjacency_matrix(G).A
    A[A == 0] = INF

    indegree, outdegree = Generate_Degree_List(A, Node_no, top_no)
    iter_no, authority_score, hub_score = HITS_algo(A, Node_no, indegree, outdegree, max_iter, e)
   
    Hub_nodes = []
    Authority_nodes = []

    fout = open("Output/HIT_output.txt", "w")
    fout.write("Iteration no: " + str(iter_no) + "\n")
    fout.write("Hubs Score: ")
    for i in range(top_no):
        if i == (top_no - 1):
            fout.write(str(hub_score[i]) + ".")
        else:
            fout.write(str(hub_score[i]) + ", ")
        Hub_nodes.append(hub_score[i][0])
    fout.write("\n")
    fout.write("Authority Score: ")
    
    for i in range(top_no):
        if i == (top_no - 1):
            fout.write(str(authority_score[i]) + ".")
        else:
            fout.write(str(authority_score[i]) + ", ")
        Authority_nodes.append(authority_score[i][0])
    fout.write("\n")
    fout.close()

    ### Printing list of top nodes
    f_top = open('Output/Top_node_list.txt', 'a')
    f_top.write("Hub Nodes:\n")
    f_top.write(str(Hub_nodes) + "\n")
    f_top.write("Authority Nodes:\n")
    f_top.write(str(Authority_nodes) + "\n")
    f_top.close()

