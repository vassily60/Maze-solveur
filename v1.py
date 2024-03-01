import argparse
import math
from util import Node, StackFrontier, QueueFrontier, PriorityQueueFrontier

# Global variables that represent the symbols in the maze
WALL = '%'
PRIZE = '.'
START_POINT = 'P'


def goal_test(state):
    '''
    Checks to see if the agent is at the coordinates of a prize
    Arguments: List of tuples
    Return: Boolean value
    '''
    # Agent position is the first element and the rest are prize positions
    return state[0] == state[1]
 

def transition_model(maze, state):
    '''
    Returns a list of all the possible moves the agent can make
    Arguments: A 2D array and a list of tuples
    Return: A list of tuples
    '''
    row, col = state[0]

    # Get coordinates of all possible actions: North, South, West and East
    possible_actions = [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]

    # Check to see if the actions are valid and if not remove them
    valid_action = []
    for action in possible_actions:
        new_row, new_col = action
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != WALL:
            valid_action.append(action)
    
    return valid_action
    


def find_symbol_coordinates(symbol, maze):
    '''
    Finds the coordinates of the symbols in the maze and add them in a list
    Arguments: A string and a 2D array
    Return: List of tuples
    '''
    coordinates = []

    # Store the indexs of the symbols location in the maze
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == symbol:
                coordinates.append((row_index, col_index))

    return coordinates

# Depth-first search for single prize
def single_dfs(maze):
    initial_state = find_symbol_coordinates(START_POINT, maze) + find_symbol_coordinates(PRIZE, maze)
    start_node = Node(state=initial_state)
    frontier = StackFrontier()
    frontier.add(start_node)
    visited = set()

    while not frontier.empty():
        curr_node = frontier.remove()
        visited.add(curr_node.state[0])

        if goal_test(curr_node.state):
            path = path_to_goal(curr_node)
            
            print(f"Length of path: {len(path)}\n")
            print(f"Number of nodes expanded: {len(visited)}\n")
            return path
        
        moves = transition_model(maze, curr_node.state)
        for move in moves:
            if move not in visited and not frontier_check(frontier, move):
                new_state = [move] + [curr_node.state[1]]
                new_node = Node(state=new_state, parent=curr_node)
                frontier.add(new_node)
    
    return None

# Breadth-first search for single prize
def single_bfs(maze):
    initial_state = find_symbol_coordinates(START_POINT, maze) + find_symbol_coordinates(PRIZE, maze)
    start_node = Node(state=initial_state)
    frontier = QueueFrontier()
    frontier.add(start_node)
    visited = set()

    while not frontier.empty():
        curr_node = frontier.remove()
        visited.add(curr_node.state[0])
        
        if goal_test(curr_node.state):
            path = path_to_goal(curr_node)
            print(f"Length of path: {len(path)}\n")
            print(f"Number of nodes expanded: {len(visited)}\n")
            return path
            
        moves = transition_model(maze, curr_node.state)
        for move in moves:
            if move not in visited and not frontier_check(frontier, move):
                new_state = [move] + [curr_node.state[1]]
                new_node = Node(state=new_state, parent=curr_node)
                frontier.add(new_node)
    return None

def frontier_check(frontier, state):
    for node in frontier.frontier:
        if node.state[0] == state:
            return True
    return False

def single_gbfs(maze):
    initial_state = find_symbol_coordinates(START_POINT, maze) + find_symbol_coordinates(PRIZE, maze)
    start_node = Node(state=initial_state)
    frontier = PriorityQueueFrontier()
    frontier.add(start_node)
    visited = set()

    while not frontier.empty():
        curr_node = frontier.remove()
        visited.add(curr_node.state[0])
        
        if goal_test(curr_node.state):
            path = path_to_goal(curr_node)
            print(f"Length of path: {len(path)}\n")
            print(f"Number of nodes expanded: {len(visited)}\n")
            return path
            
        moves = transition_model(maze, curr_node.state)
        for move in moves:
            if move not in visited and not priority_frontier_check(frontier, move):
                new_state = [move] + [curr_node.state[1]]
                hueristic_value = manhattan_distance(new_state)
                new_node = Node(state=new_state, parent=curr_node, heuristic_value=hueristic_value)
                frontier.add(new_node)
    return None

def single_astar(maze):
    initial_state = find_symbol_coordinates(START_POINT, maze) + find_symbol_coordinates(PRIZE, maze)
    start_node = Node(state=initial_state)
    frontier = PriorityQueueFrontier()
    frontier.add(start_node)
    visited = set()

    while not frontier.empty():
        curr_node = frontier.remove()
        visited.add(curr_node.state[0])
    
        if goal_test(curr_node.state):
            path = path_to_goal(curr_node)
            print(f"Length of path: {len(path)}\n")
            print(f"Number of nodes expanded: {len(visited)}\n")
            return path
            
        moves = transition_model(maze, curr_node.state)
        for move in moves:
            if move not in visited and not priority_frontier_check(frontier, move):
                new_state = [move] + [curr_node.state[1]]
                cost = curr_node.cost + 1
                heuristic_value = manhattan_distance(new_state)
                new_node = Node(state=new_state, parent=curr_node, cost=cost, heuristic_value=heuristic_value)
                frontier.add(new_node)
    return None

def manhattan_distance(state):
    agent_coords, prize_coords = state
    return abs(prize_coords[0] - agent_coords[0]) + abs(prize_coords[1] - agent_coords[1])


def multi_astar(maze):
    start_point = find_symbol_coordinates(START_POINT, maze)[0]
    prizes = find_symbol_coordinates(PRIZE, maze)
    closest_prize = find_best_prize(start_point, prizes)
    initial_state = [start_point, closest_prize]
    order_prizes_searched = []
    prizes.remove(closest_prize)
    order_prizes_searched.append(closest_prize)
    start_node = Node(state=initial_state)
    frontier = PriorityQueueFrontier()
    frontier.add(start_node)
    visited = set()
    total_visited = 0

    while not frontier.empty():
        curr_node = frontier.remove()
        visited.add(curr_node.state[0])
    
        if goal_test(curr_node.state) and len(prizes) == 0:
            path = path_to_goal(curr_node)
            order = order_prizes_visited(maze, order_prizes_searched) # print the maze with numbers instead of prizes in the order they were visited
            print(f"Length of path: {len(path)}\n")
            print(f"Number of nodes expanded: {total_visited}\n")
            return path, order
        
        elif goal_test(curr_node.state):
            point = curr_node.state[0]
            closest_prize = find_best_prize(point, prizes)
            new_prize_state = [point, closest_prize]
            prizes.remove(closest_prize)
            order_prizes_searched.append(closest_prize)
            new_start_node = Node(state=new_prize_state, parent=curr_node)
            curr_node = new_start_node
            new_frontier = PriorityQueueFrontier()
            new_frontier.add(new_start_node)
            frontier = new_frontier
            total_visited += len(visited)
            visited = set()
            
        moves = transition_model(maze, curr_node.state)
        for move in moves:
            if move not in visited and not priority_frontier_check(frontier, move):
                new_state = [move] + [curr_node.state[1]]
                cost = curr_node.cost + 1
                heuristic_value = manhattan_distance(new_state)
                new_node = Node(state=new_state, parent=curr_node, cost=cost, heuristic_value=heuristic_value)
                frontier.add(new_node)
    return None

def order_prizes_visited(maze, order_prize_search):
    prize = order_prize_search
    for i in range(len(order_prize_search)):
        if i < 10:
            maze[prize[i][0]][prize[i][1]] = str(i)
        else:
            maze[prize[i][0]][prize[i][1]] = chr(i+87)
    
    lines = [''.join(line) for line in maze]
    text = '\n'.join(lines)
    return text



def find_best_prize(point, prizes):
    best_prize_val = 999
    best_prize = None
    for prize in prizes:
        val = manhattan_distance([point, prize])
        if val < best_prize_val:
            best_prize_val = val
            best_prize = prize
    return best_prize
    
def priority_frontier_check(frontier, state):
    for node in frontier.frontier:
        if node[0].state[0] == state:
            return True
    return False


# Backtrack from goal node to find path taken
def path_to_goal(node):
    path = []
    while node.parent is not None:
        path.append(node.state[0])
        node = node.parent
    path.reverse()
    return path

# Display all the maze squares visited
def draw_path(maze, path):
    for coord in path:
        maze[coord[0]][coord[1]] = "#"
    lines = [''.join(line) for line in maze]
    text = '\n'.join(lines)
    print(text)

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search a maze for a path')
    parser.add_argument('-a','--algorithm', help='algorithm', required=True)
    parser.add_argument('-f','--filename', help='filename', required=True)
    args = parser.parse_args()

    filename = args.filename
    algorithm = args.algorithm

    # Read text file into 2D array
    with open(filename, "r") as f:
        maze = [list(line.strip()) for line in f]

    # initial_state = find_symbol_coordinates(START_POINT, maze) + find_symbol_coordinates(PRIZE, maze)
    # start_node = Node(state=initial_state)

    if algorithm == "single_dfs":
        path = single_dfs(maze)
    elif algorithm == "single_bfs":
        path = single_bfs(maze)
    elif algorithm == "single_gbfs":
        path = single_gbfs(maze)
    elif algorithm == "single_astar":
        path = single_astar(maze)
    elif algorithm == "multi_astar":
        path, draw_prize_order = multi_astar(maze)
    else:
        raise(ValueError("Invalid algorithm"))
    
    if path == None:
        print("No path found.")
    elif algorithm == "multi_astar":
        print(draw_prize_order)
    else:
        draw_path(maze, path)
    