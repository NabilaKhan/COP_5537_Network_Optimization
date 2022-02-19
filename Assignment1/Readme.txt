Course Code: COP 5537 (Network Optimization)
Assignment 1: Implementing Dijkstra's Algorithm
PID: 5067496

####################################################################################
Assignment Contents:
(1) Pseudo code of the Dijkstra's Algorithm (PDF) -> File "Pseudocode.pdf"
(2) Source file -> File "Dijkstra_code.py"
(3) Readme file -> File "Readme.txt"
(4) Results of running the algorithm -> Results provided within "Results" folder; If the code is run again, new result files will be generated within folder "New_Results". "Output.txt" contains the overall result
(5) Screenshot of running the program -> Files "Case1_Screenshot.png", "Case2_Screenshot.png", "Case3_Screenshot.png"
####################################################################################


####################################################################################
Command lines for running the program in Windows Environment (python version 3):


### Case (1): With 2 Arguments: "python Dijkstra_code.py 5067496 Data" 
Here, Argument 1 is PID and Argument 2 is name of the input data file

		***Example***
>python Dijkstra_code.py 5067496 Data
Please check the file Output.txt for output

Output:
50, 6
50,  13,  52,  6
10

6, 67
6,  3,  85,  5,  91,  21,  19,  83,  55,  67
20

67, 74
67,  74
2

74, 49
74,  67,  55,  83,  19,  21,  91,  5,  2,  12,  75,  49
24

49, 96
49,  13,  50,  96
16


### Case (2): With 3 Arguments: "python Dijkstra_code.py 50 6 Data"
Here, Argument 1 is source, Argument 2 is destination and Argument 3 is name of the input data file

		***Example***
>python Dijkstra_code.py 50 6 Data
Given 3 arguments. Please check the file Output.txt for output

Output:
50, 6
50,  13,  52,  6
10 



### Case (3): Without Argument: "python Dijkstra_code.py"
Uses default value; PID = "5067496", Input file name = "Data"

		***Example***
> python Dijkstra_code.py
Not enough number of arguments! Running for default values: PID = '5067496', input_file = 'Data.txt'
Please check the file Output.txt for output

Output:
50, 6
50,  13,  52,  6
10

6, 67
6,  3,  85,  5,  91,  21,  19,  83,  55,  67
20

67, 74
67,  74
2

74, 49
74,  67,  55,  83,  19,  21,  91,  5,  2,  12,  75,  49
24

49, 96
49,  13,  50,  96
16
####################################################################################




####################################################################################
Command lines for running the program in Linus Environment (python version 3):

### Case (1): With 2 Arguments: "python3 Dijkstra_code.py 5067496 Data" 
Here, Argument 1 is PID and Argument 2 is name of the input data file

### Case (2): With 3 Arguments: "python3 Dijkstra_code.py 50 6 Data"
Here, Argument 1 is source, Argument 2 is destination and Argument 3 is name of the input data file

### Case (3): Without Argument: "python3 Dijkstra_code.py"
Uses default value; PID = "5067496", Input file name = "Data"
####################################################################################
