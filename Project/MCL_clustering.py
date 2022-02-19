import random
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import networkx as nx
import markov_clustering as mc

G = nx.DiGraph()



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

    G.add_edges_from(edge_list)
    nodes = len(list(G.nodes()))
    fin.close()
    return nodes




def MCL_cluster(G, n):
    # Build adjacency matrix
    A = nx.to_numpy_matrix(G)
    A = np.asarray(A)

    # Run MCL algorithm
    result = mc.run_mcl(A)
    clusters = mc.get_clusters(result)

    clus_mem_list = []

    fout = open("Output/Cluster_output.txt", "w")
    fout.write("No of nodes: " + str(n) + "\n")
    fout.write("No of Clusters: " + str(len(clusters)) + "\n")
    for clus in range(0, len(clusters)):
        fout.write("Cluster no: " + str(clus+1) + "\t\t\tNo of Members: " + str(len(clusters[clus])) + "\n")
        clus_mem_list.append(len(clusters[clus]))
    fout.write("\n\n\n")
    fout.write(str(clusters))
    fout.close()

    plt.figure()
    plt.figure(figsize=(10, 7))
    plt.xticks(np.arange(0, 440, 20))
    plt.yticks(np.arange(0, 117, 3))
    plt.hist(clus_mem_list, bins=84, range = [0, 420], edgecolor="yellow", color="orange")
    plt.xlabel("Number of nodes")
    plt.ylabel("Cluster frquency")
    plt.title("Histogram showing distribution of nodes in clusters")
    plt.savefig("Output/Cluster_histogram.png")
    
    # Draw clusters
    plt.figure(figsize=(15, 15))
    mc.draw_graph(A, clusters, node_size=10, with_labels=False, edge_color="silver")
    plt.savefig("Output/Cluster.png")
    

if __name__ == "__main__":

    ### User Input 
    input_file_name = sys.argv[1]

    ### Reading adjacency matrix from input file
    Node_no = read_input(input_file_name)
    
    ### Running MCL Algorithm
    MCL_cluster(G, Node_no)
