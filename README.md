CS365_24
========

## Table of contents
* [Goal test function](#goal-test-function)
* [Run all single prizes](#run-algorithms-using-a-script-to-run-the-single-search)
* [Run individual algorithms](#run-individual-algorithms)


## Goal Test Function

The goal test function takes a list of tuples as an argument. The first tuple of the list contains the state representation of the agent (its current location), and the other tuples are the location of the prize(s). It returns True if the agent is at the location of prize.

### Here is the function
```
def goal_test(state):
    return state[0] == state[1]
```

### Here is an example of how to call it

In this example, there is only one prize and the agent location is the same as the prize, the function returns True. 

```
goal_true = [(0,5), (0,5)]
goal_test(goal_true)
```
### Here is another example

In this second example, there are several prizes, and the agent is at one of the prize locations. The function returns True.

```
goal_true_mult = [(0,5), (0,5), (3,1)]
goal_test(goal_true_mult)
```

We will make sure that we have collected all the prizes by removing collected prizes from the list


## Run algorithms using a script to run the single search

We have a script that automates the process of running single_bfs, single_dfs, single_gbfs and single_astar on each single prize maze then sending the output to their own text files in the folder algorithm results. In order to run this script this is the command you should run in the main directory:

```
$ ./single-prize-results.sh
```

## Run individual algorithms

### Depth-First Search

We use command line arguments to run the Depth-First Search algorithm from our main file v1.py. The command line takes two arguments, -a is the name of the algorithm (single_dfs) and -f is the name of the file (1prize-open.txt, 1prize-medium.txt or 1prize-large.txt). For instance, if we want to find the path found by the depth-first search in the medium maze we would write this in the command line:

```
$ python3 v1.py -a single_dfs -f 1prize-medium.txt
```

The output of this command is the original maze with '#' displayed in every square visited on the path. In addition, the path cost of the solution and the number of nodes expanded are printed. 

### Breadth-First Search

Similarly, we use command line arguments to run the Breadth-First Search algorithm from our main file v1.py. The command line takes two arguments, -a is the name of the algorithm (single_bfs) and -f is the name of the file (1prize-open.txt, 1prize-medium.txt or 1prize-large.txt). For instance, if we want to find the path found by the breadth-first search in the small maze we would write this in the command line:

```
$ python3 v1.py -a single_bfs -f 1prize-open.txt
```

The output of this command is the original maze with '#' displayed in every square visited on the path. In addition, the path cost of the solution and the number of nodes expanded are printed. 

### Greedy Best First Search 

Again, we use command line arguments to run the Greedy Best First Search algorithm from our main file v1.py. The command line takes two arguments, -a is the name of the algorithm (single_gbfs) and -f is the name of the file (1prize-open.txt, 1prize-medium.txt or 1prize-large.txt). For instance, if we want to find the path found by the greedy best first search in the small maze we would write this in the command line:

```
$ python3 v1.py -a single_gbfs -f 1prize-open.txt
```

The output of this command is the original maze with '#' displayed in every square visited on the path. In addition, the path cost of the solution and the number of nodes expanded are printed. 

### A* Search

We use command line arguments to run the A* Search algorithm from our main file v1.py. The command line takes two arguments, -a is the name of the algorithm (single_astar or multi_astar) and -f is the name of the file (1prize-open.txt, 1prize-medium.txt or 1prize-large.txt). For instance, if we want to find the path found by the A* search algorithm in the small maze we would write this in the command line:

```
$ python3 v1.py -a single_astar -f 1prize-open.txt
```

The output of this command is the original maze with '#' displayed in every square visited on the path. In addition, the path cost of the solution and the number of nodes expanded are printed.


The following command is to get the path found in the multiprize small maze.

```
$ python3 v1.py -a multi_astar -f multiprize-small.txt
```

The output is the original maze with numbers, and then letters, displayed in the order each prize was visited. In addition, the path cost of the solution and the number of nodes expanded are printed.



