####################   List of Files inside folder "5067496"   #################### 

1. Five Python Codes: PageRank.py, Weighted_Page_Rank.py, HITS.py, Network_analysis.py, MCL_clustering.py
2. Input Data File: "web-Stanford-12000.txt"
3. Final Output Folder: "Output_Final" [It containts all the output files and output plots]
4. Output Folder: "Output" [Empty folder; For running the codes again, the new outputs will be generated here]
5. Project Report: "Network_Optimization_Project_Report.pdf"
6. Readme File



####################   Running PageRank Algorithm   #################### 

### Code: Page_Rank.py
### Linux Command Line: python3 Page_Rank.py web-Stanford-12000 0.85 0.000001 1000 20
### Windows Command Line: python Page_Rank.py web-Stanford-12000 0.85 0.000001 1000 20
### Parameter No: 5
### Parameter List: 
 * 1st Parameter -> Input file name
 * 2nd Parameter -> Damping factor
 * 3rd Parameter -> Convergence threshold
 * 4th Parameter -> Maximum iteration
 * 5th Parameter -> Number of web pages to be listed with top value 
 		    [Final Report shows only top 10 web pages]		    
### Output File: Output_Final/PageRank_Output.txt [For running the code again, the new output will be generated inside folder "Output"]



####################   Running Weighted PageRank Algorithm   #################### 

### Code: Weighted_Page_Rank.py
### Linux Command Line: python3 Weighted_Page_Rank.py web-Stanford-12000 0.85 0.000001 1000 20
### Windows Command Line: python Weighted_Page_Rank.py web-Stanford-12000 0.85 0.000001 1000 20
### Parameter No: 5
### Parameter List: 
 * 1st Parameter -> Input file name
 * 2nd Parameter -> Damping factor
 * 3rd Parameter -> Convergence threshold
 * 4th Parameter -> Maximum iteration
 * 5th Parameter -> Number of web pages to be listed with top value 
 		    [Final Report shows only top 10 web pages]		    
### Output File: Output_Final/Weighted_output.txt [For running the code again, the new output will be generated inside folder "Output"]



####################   Running HITS PageRank Algorithm   #################### 

### Code: HITS.py
### Linux Command Line: python3 HITS.py web-Stanford-12000 0.000001 1000 20
### Windows Command Line: python HITS.py web-Stanford-12000 0.000001 1000 20
### Parameter No: 4
### Parameter List: 
 * 1st Parameter -> Input file name
 * 2nd Parameter -> Convergence Threshold
 * 3rd Parameter -> Maximum Iteration
 * 4th Parameter -> Number of web pages to be listed with top value 
 		    [Final Report shows only top 10 web pages]		    
### Output File: Output_Final/HIT_output.txt [For running the code again, the new output will be generated inside folder "Output"]



####################   Network Centrality Analysis   #################### 

### Code: Network_analysis.py
### Linux Command Line: python3 Network_analysis.py web-Stanford-12000 20
### Windows Command Line: python Network_analysis.py web-Stanford-12000 20
### Parameter No: 2
### Parameter List: 
 * 1st Parameter -> Input file name
 * 2nd Parameter -> Number of web pages to be listed with top value 
 		    [Final Report shows only top 10 web pages] 		    
### Output File: Output_Final/Network_analysis.txt [For running the code again, the new output will be generated inside folder "Output"]
### Output Plot: Indegree_freq.png, Indegree_prob.png, Outdegree_freq.png, Outdegree_prob.png 


####################   Running MCL Clustering Algorithm   #################### 

### Code: MCL_clustering.py
### Linux Command Line: python3 MCL_clustering.py web-Stanford-12000
### Windows Command Line: python MCL_clustering.py web-Stanford-12000
### Parameter No: 1
### Parameter List: 
 * 1st Parameter -> Input file name		    
### Output File: Output_Final/Cluster_output.txt [For running the code again, the new output will be geenrated inside folder "Output"]
### Output Plot: Cluster.png, Cluster_histogram.png



####################   Sequence of Running the Codes   ####################

*** Can Run PageRank.py, Weighted_Page_Rank.py, HITS.py, MCL_clustering.py parallely. They don't have any dependency on other codes.

*** Must run Network_analysis.py after running the codes PageRank.py, Weighted_Page_Rank.py, HITS.py cause it reads input from the text file "Top_node_list.txt" which is written by (appended) all these three algorithms.



####################   Additional Comments   ####################

*** PageRank.py, Weighted_Page_Rank.py, HITS.py, all the three codes also writes their outputs in the file "Top_node_list.txt". This file is later used as input by code Network_analysis.py to generate network centrality values for the top 10 web pages determined by the three algorithms. 

*** All the Algorithms are kept and run separately in order to make the pipeline parallel and faster.

*** Finally, the whole pipeline was tested in a Linux environment. But should also work in Windows OS.

####################   ...END...   ####################
