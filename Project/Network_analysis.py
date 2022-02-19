import random
import numpy as np
import sys
import math
from matplotlib import pyplot as plt
import networkx as nx
import statistics as st
from scipy import stats as s



INF = 9999
G = nx.DiGraph()
Node_map_dic = {}





def read_top_list(step):
    ftop = open("Output/Top_node_list.txt", "r")
    Page_rank_top = []
    WPR_top = []
    HITS_hub_top = []
    HITS_auth_top = []
    
    while(True):
        line = ftop.readline()
        if line == '':
            break
        if line[0:3] == 'Pag':
            pg_list = ftop.readline()
            pg_list = pg_list.strip('\n').lstrip('[')
            pg_list = pg_list.replace("),", ";")
            pg_list = pg_list.split(";")
        
            for p in range(step):
                page = pg_list[p].split(",")[0]
                page = page.strip(" ").strip("(")
                Page_rank_top.append(int(page))
                
        elif line[0:3] == 'Wei':
            pg_list = ftop.readline()
            pg_list = pg_list.strip('\n').lstrip('[')
            pg_list = pg_list.replace("),", ";")
            pg_list = pg_list.split(";")
            
            for p in range(step):
                page = pg_list[p].split(",")[0]
                page = page.strip(" ").strip("(")
                WPR_top.append(int(page))
                
        elif line[0:3] == 'Hub':
            pg_list = ftop.readline()
            pg_list = pg_list.strip('\n')
            HITS_hub_top = pg_list.strip('][').split(', ')
            HITS_hub_top = list(map(int, HITS_hub_top))
            
        elif line[0:3] == 'Aut':
            pg_list = ftop.readline()
            pg_list = pg_list.strip('\n')
            HITS_auth_top = pg_list.strip('][').split(', ')
            HITS_auth_top = list(map(int, HITS_auth_top))
        
    ftop.close()

    return Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top
    



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




def Print_Degree_List(indegree, outdegree, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top):
    in_dic = {}
    out_dic = {}
    len_in = [len(indegree[ain]) for ain in range(0, len(indegree))]
    len_out = [len(outdegree[aout]) for aout in range(0, len(outdegree))]
    
    for x in range(0, len(len_in)):
       in_dic[Node_map_dic[x+1]] = len_in[x]
       out_dic[Node_map_dic[x+1]] = len_out[x]

    sorted_indic = sorted(in_dic.items(), key=lambda kv: kv[1], reverse=True)
    sorted_outdic = sorted(out_dic.items(), key=lambda kv: kv[1], reverse=True)
    
    print("Indegree: ")
    print([sorted_indic[x] for x in range(0, top_no)])
    print("Outdegree: ")
    print([sorted_outdic[x] for x in range(0, top_no)])
    print("\n\n")
        
    fout.write("Indegree: \n")
    fout.write(str([sorted_indic[x] for x in range(0, top_no)]) + "\n")
    fout.write("Outdegree: \n")
    fout.write(str([sorted_outdic[x] for x in range(0, top_no)]) + "\n")


    ### PageRank Top
    PR_tuple = []
    for p in Page_rank_top:
        PR_tuple.append((p, in_dic[p]))
    ### Weighed PageRank Top
    WPR_tuple = []
    for p in WPR_top:
        WPR_tuple.append((p, in_dic[p]))
    ### HITS Hub Top
    Hub_tuple = []
    for p in HITS_hub_top:
        Hub_tuple.append((p, in_dic[p]))
    ### HITS Authority Top
    Auth_tuple = []
    for p in HITS_auth_top:
        Auth_tuple.append((p, in_dic[p]))
    
    fout.write("Indegree of PageRank: \n")
    fout.write(str([PR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Indegree of Weighted PageRank: \n")
    fout.write(str([WPR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Indegree of HITS-Hub: \n")
    fout.write(str([Hub_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Indegree of HITS-Auth: \n")
    fout.write(str([Auth_tuple[x] for x in range(0, top_no)]) + "\n\n\n")




# Floyd Warshall Algorithm 
def Floyd_Warshall(G, nV):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                if p == q:
                    dist[p][q] = 0
                else:
                    dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    return dist

    


def Degree_of_Separation(A, n, dist):
    distances = []
    for i in range(n):
        for j in range(n):
            if dist[i][j] < INF and dist[i][j] > 0:
                distances.append(dist[i][j])
    
    print('Maximum degrees of separation: ' + str(max(distances)))
    print('Minimum degrees of separation: ' + str(min(distances)))
    print('Median for degrees of separation: ' + str(st.median(distances)))
    print('Mode for degrees of separation: ' + str(s.mode(distances)[0]))
    print('Avg for degrees of separation: ' + str(round(sum(distances)/len(distances),4)))
    print("\n\n")

    fout.write("Maximum degrees of separation: " + str(max(distances)) + "\n")
    fout.write("Minimum degrees of separation: " + str(min(distances)) + "\n")
    fout.write("Median for degrees of separation: " + str(st.median(distances)) + "\n")
    fout.write("Mode for degrees of separation: " + str(s.mode(distances)[0]) + "\n")
    fout.write("Avg for degrees of separation: " + str(round(sum(distances)/len(distances),4)) + "\n\n\n")




def Closeness_Centrality(dist, n, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top):
    sum_dis = []
    avg_dis = []
    closeness_centrality_list = []
    sum_dic = {}
    avg_dic = {}
    closeness_centrality_dic = {}
    
    for i in range(0, n):
        count = 0
        summ = 0
        for j in range(0, n):
            if dist[i][j] != INF:
                summ = summ + dist[i][j]
                count += 1

        if count != 0 and summ != 0:
            sum_dis.append(summ)
            avg_dis.append(sum_dis[i]/count)
            closeness_centrality_list.append(1/summ)
        else:
            sum_dis.append(-999)
            avg_dis.append(-999)
            closeness_centrality_list.append(-999)

    for x in range(0, len(sum_dis)):
        if sum_dis[x] != -999 and avg_dis[x] != -999 and closeness_centrality_list[x] != -999:
            sum_dic[Node_map_dic[x+1]] = sum_dis[x]
            avg_dic[Node_map_dic[x+1]] = avg_dis[x]
            closeness_centrality_dic[Node_map_dic[x+1]] = closeness_centrality_list[x]
        else:
            sum_dic[Node_map_dic[x+1]] = 0
            avg_dic[Node_map_dic[x+1]] = 0
            closeness_centrality_dic[Node_map_dic[x+1]] = 0

        
    sorted_sum_dic = sorted(sum_dic.items(), key=lambda kv: kv[1])
    sorted_avg_dic = sorted(avg_dic.items(), key=lambda kv: kv[1])
    sorted_closeness_centrality_dic = sorted(closeness_centrality_dic.items(), key=lambda kv: kv[1], reverse=True)
    print("Summation of distances of each node from other nodes: ", [sorted_sum_dic[x] for x in range(0, top_no)])
    print("Avg. of distances of each node from other nodes: ", [sorted_avg_dic[x] for x in range(0, top_no)])
    print("Closeness centrality of each node: ", [sorted_closeness_centrality_dic[x] for x in range(0, top_no)])
    print("\n\n")

    fout.write("Summation of distances of each node from other nodes: " + str([sorted_sum_dic[x] for x in range(0, top_no)]) + "\n")
    fout.write("Avg. of distances of each node from other nodes: " + str([sorted_avg_dic[x] for x in range(0, top_no)]) + "\n")
    fout.write("Closeness centrality of each node: " + str([sorted_closeness_centrality_dic[x] for x in range(0, top_no)]) + "\n")

    ### PageRank Top
    PR_tuple = []
    for p in Page_rank_top:
        PR_tuple.append((p, closeness_centrality_dic[p]))
    ### Weighed PageRank Top
    WPR_tuple = []
    for p in WPR_top:
        WPR_tuple.append((p, closeness_centrality_dic[p]))
    ### HITS Auth Top
    Hub_tuple = []
    for p in HITS_hub_top:
        Hub_tuple.append((p, closeness_centrality_dic[p]))
    ### HITS Hub Top
    Auth_tuple = []
    for p in HITS_auth_top:
        Auth_tuple.append((p, closeness_centrality_dic[p]))

    fout.write("Closeness Centrality of PageRank: \n")
    fout.write(str([PR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Closeness Centrality of Weighted PageRank: \n")
    fout.write(str([WPR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Closeness Centrality of HITS-Hub: \n")
    fout.write(str([Hub_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Closeness Centrality of HITS-Auth: \n")
    fout.write(str([Auth_tuple[x] for x in range(0, top_no)]) + "\n\n\n")


    

def Diameter(dist, n):
    max_distance = -999
    max_i = -1
    max_j = -1
    
    for i in range(0, n):
        for j in range(0, n):
            if dist[i][j] != INF and dist[i][j] > max_distance:
                max_distance = dist[i][j]
                max_i = i
                max_j = j
    print("Max_distance is " + str(max_distance) + " between node pairs (" + str(Node_map_dic[max_i+1]) + ", " + str(Node_map_dic[max_j+1]) + ")")
    print("\n\n")
    fout.write("Max_distance is " + str(max_distance) + " between node pairs (" + str(Node_map_dic[max_i+1]) + ", " + str(Node_map_dic[max_j+1]) + ")" + "\n\n\n")

    


def Eccentricity_Centrality(dist, n, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top):
    eccentricity_centrality = []
    eccentricity_dic = {}
    
    for i in range(0, n):
        max_dis = -999
        for j in range(0, n):
            if dist[i][j] != INF and dist[i][j] != 0 and dist[i][j] > max_dis:
                max_dis = dist[i][j]
        if max_dis != -999:
            eccentricity_centrality.append(1/max_dis)
        else:
            eccentricity_centrality.append(0)

    for x in range(0, len(eccentricity_centrality)):
        eccentricity_dic[Node_map_dic[x+1]] = eccentricity_centrality[x]
        
    sorted_eccentricity = sorted(eccentricity_dic.items(), key=lambda kv: kv[1], reverse=True)
    print([sorted_eccentricity[x] for x in range(0, top_no)])
    print("\n\n")
    fout.write(str([sorted_eccentricity[x] for x in range(0, top_no)]) + "\n")
     
    ### PageRank Top
    PR_tuple = []
    for p in Page_rank_top:
        PR_tuple.append((p, eccentricity_dic[p]))
    ### Weighed PageRank Top
    WPR_tuple = []
    for p in WPR_top:
        WPR_tuple.append((p, eccentricity_dic[p]))
    ### HITS Auth Top
    Hub_tuple = []
    for p in HITS_hub_top:
        Hub_tuple.append((p, eccentricity_dic[p]))
    ### HITS Hub Top
    Auth_tuple = []
    for p in HITS_auth_top:
        Auth_tuple.append((p, eccentricity_dic[p]))

    fout.write("Eccentricity Centrality of PageRank: \n")
    fout.write(str([PR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Eccentricity Centrality of Weighted PageRank: \n")
    fout.write(str([WPR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Eccentricity Centrality of HITS-Hub: \n")
    fout.write(str([Hub_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Eccentricity Centrality of HITS-Auth: \n")
    fout.write(str([Auth_tuple[x] for x in range(0, top_no)]) + "\n\n\n")
    


                
def Shortest_Path_Betweenness_Centrality(G, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top):
    between_values = nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None) 
    sorted_between = sorted(between_values.items(), key=lambda kv: kv[1], reverse=True)
    print([sorted_between[x] for x in range(0, top_no)])
    print("\n\n")
    fout.write(str([sorted_between[x] for x in range(0, top_no)]) + "\n")

    
    ### PageRank Top
    PR_tuple = []
    for p in Page_rank_top:
        PR_tuple.append((p, between_values[p]))
    ### Weighed PageRank Top
    WPR_tuple = []
    for p in WPR_top:
        WPR_tuple.append((p, between_values[p]))
    ### HITS Auth Top
    Hub_tuple = []
    for p in HITS_hub_top:
        Hub_tuple.append((p, between_values[p]))
    ### HITS Hub Top
    Auth_tuple = []
    for p in HITS_auth_top:
        Auth_tuple.append((p, between_values[p]))

    fout.write("Betweenness Centrality of PageRank: \n")
    fout.write(str([PR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Betweenness Centrality of Weighted PageRank: \n")
    fout.write(str([WPR_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Betweenness Centrality of HITS-Hub: \n")
    fout.write(str([Hub_tuple[x] for x in range(0, top_no)]) + "\n")
    fout.write("Betweenness Centrality of HITS-Auth: \n")
    fout.write(str([Auth_tuple[x] for x in range(0, top_no)]) + "\n\n\n")    



    
### Implemented, takes too long to run for the given input graph. Works for smaller graphs
def Katz_status_index(G, top_no):
    node_index = nx.katz_centrality(G, alpha=0.1, beta=1.0, max_iter=1000, tol=1e-06, nstart=None, normalized=True, weight=None)

    sorted_index = sorted(node_index.items(), key=lambda kv: kv[1], reverse=True)
    print([sorted_index[x] for x in range(0, top_no)])
    print("\n\n")
    fout.write(str([sorted_index[x] for x in range(0, top_no)]) + "\n\n\n")




def plot_degree_dist(G, top_no):
    indegree, outdegree = Generate_Degree_List(A, Node_no, top_no)

    len_in = [len(indegree[ain]) for ain in range(0, len(indegree))]
    len_out = [len(outdegree[aout]) for aout in range(0, len(outdegree))]
    indeg_max = max(len_in)
    outdeg_max = max(len_out)

    indeg_count = [0 for i in range(indeg_max + 1)]
    outdeg_count = [0 for i in range(outdeg_max + 1)]
    indeg_prob = [0 for i in range(indeg_max + 1)]
    outdeg_prob = [0 for i in range(outdeg_max + 1)]
    indeg_count_plt = []
    outdeg_count_plt = []
    indeg_prob_plt = []
    outdeg_prob_plt = []
    xin = []
    xout = []
    prob_yticks = np.arange(0, 1.1, 0.1)

    
    for i in range(len(len_in)):
        deg = len_in[i]
        indeg_count[deg] += 1
    
    for i in range(len(len_out)):
        deg = len_out[i]
        outdeg_count[deg] += 1

    in_sum = sum(indeg_count)
    out_sum = sum(outdeg_count)

        
    for i in range(indeg_max + 1):
        if indeg_count[i] != 0:
            indeg_count_plt.append(indeg_count[i])
            indeg_prob_plt.append(indeg_count[i]/in_sum)
            xin.append(str(i))

    for i in range(outdeg_max + 1):
        if outdeg_count[i] != 0:
            outdeg_count_plt.append(outdeg_count[i])
            outdeg_prob_plt.append(outdeg_count[i]/out_sum)
            xout.append(str(i))


    plt1 = plt.figure(1)
    plt.figure(figsize=(15,6))
    plt.bar(xin, indeg_count_plt, color = "g")
    plt.xlabel("Degree, k")
    plt.ylabel("Frequency, f(k)")
    plt.title("Degree Distribution of Indegree")
    plt.xticks(fontsize= "7")
    plt.yticks(fontsize= "6")
    plt.savefig("Output/Indegree_freq.png")

    plt2 = plt.figure(2)
    plt.figure(figsize=(15,6))
    plt.bar(xout, outdeg_count_plt)
    plt.xlabel("Degree, k")
    plt.ylabel("Frequency, f(k)")
    plt.title("Degree Distribution of Outdegree")
    plt.xticks(fontsize= "7")
    plt.yticks(fontsize= "5")
    plt.savefig("Output/Outdegree_freq.png")

    plt1 = plt.figure(3)
    plt.figure(figsize=(15,6))
    plt.bar(xin, indeg_prob_plt, color = "g")
    plt.xlabel("Degree, k")
    plt.ylabel("Probability, p(k)")
    plt.yticks(prob_yticks)
    plt.title("Degree Distribution of Indegree")
    plt.xticks(fontsize= "7")
    plt.yticks(fontsize= "6")
    plt.savefig("Output/Indegree_prob.png")

    plt2 = plt.figure(4)
    plt.figure(figsize=(15,6))
    plt.bar(xout, outdeg_prob_plt)
    plt.xlabel("Degree, k")
    plt.ylabel("Probablity, p(k)")
    plt.title("Degree Distribution of Outdegree")
    plt.yticks(prob_yticks)
    plt.xticks(fontsize= "7")
    plt.yticks(fontsize= "5")
    plt.savefig("Output/Outdegree_prob.png")



    

    
if __name__ == "__main__":

    
    input_file_name = sys.argv[1]
    top_no = int(sys.argv[2])

    Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top = read_top_list(top_no)
    
    fout = open("Output/Network_analysis.txt", "w")
   
    Node_no = read_input(input_file_name)
    Node_no = len(list(G.nodes()))
    print('Total number of nodes: ' + str(Node_no))
    print('Total number of edges: ' + str(len(G.edges())))
    print("\n\n")
    fout.write("Total number of nodes: " + str(Node_no) + "\n")
    fout.write("Total number of edges: " + str(len(G.edges())) + "\n\n\n")

    
    Node_list = list(G.nodes())
    for i in range(1, Node_no+1):
        Node_map_dic[i] = int(Node_list[i-1])
        
    A = nx.adjacency_matrix(G).A
    A[A == 0] = INF

    dist = Floyd_Warshall(A, Node_no)

    print("Degree of Separation:")
    fout.write("Degree of Separation: \n")
    Degree_of_Separation(A, Node_no, dist)
    print("Diameter:")
    fout.write("Diameter: \n")
    Diameter(dist, Node_no)
    print("Degree Centrality:")
    fout.write("Degree Centrality: \n")
    indegree, outdegree = Generate_Degree_List(A, Node_no, top_no)
    Print_Degree_List(indegree, outdegree, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top)
    print("Closeness Centrality:")
    fout.write("Closeness Centrality: \n")
    Closeness_Centrality(dist, Node_no, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top)
    print("Eccentricity Centrality:")
    fout.write("Eccentricity Centrality: \n")
    Eccentricity_Centrality(dist, Node_no, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top)
    print("Shortest Path Betweenness Centrality:")
    fout.write("Shortest Path Betweenness Centrality: \n")
    Shortest_Path_Betweenness_Centrality(G, top_no, Page_rank_top, WPR_top, HITS_hub_top, HITS_auth_top)
    
##    print("Katzs Status Index")
##    fout.write("Katzs Status Index: \n")
##    Katz_status_index(G, top_no)
    
    plot_degree_dist(G, top_no)
    
    fout.close()
