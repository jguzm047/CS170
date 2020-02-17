def main():
    puzzle_mode = input("Welcome to the 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."+ '\n')
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
        "Please only enter valid 8-puzzles. " + '\n')
    puzzle_row_one = input("Enter the first row: ")
    puzzle_row_two = input("Enter the second row: ")
    puzzle_row_three = input("Enter the third row: ")
    puzzle_row_one = puzzle_row_one.split()
    puzzle_row_two = puzzle_row_two.split()
    puzzle_row_three = puzzle_row_three.split()
    for i in range(0, 3):
        puzzle_row_one[i] = int(puzzle_row_one[i])
        puzzle_row_two[i] = int(puzzle_row_two[i])
        puzzle_row_three[i] = int(puzzle_row_three[i])
        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)
        q.Readyqueue()
    return
def init_default_puzzle_mode():
    selected_difficulty = input(
    "Please enter a difficulty on a scale from 1 through 3." + '\n')
    if selected_difficulty == "1":
        print("Difficulty of 'easy' selected.")
        return 1
    if selected_difficulty == "2":
        print("Difficulty of 'Medium' selected.")
        return 2
    if selected_difficulty == "3":
        print("Difficulty of 'hard' selected.")
        return 3
def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
        print('\n')
# Uniform Cost Search Algorithm
def uniform_cost_searchQueingFunction(Node, children):
    from queue import PriorityQueue
    q = PriorityQueue() # this is our PriorityQueue
    childern = [node()] # this is a child object
    for child in childern:
        global current_state # global variables
        global goal_state # global variables
        global count
        current_state = np.array([[8, 3, 2], [4, 5, 6], [7, 1, 0]]) # current state of array/matrix
        goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) # goal state of the array/matrix
        misplaced_tiles = np.sum(current_state != goal_state) - 1
        q.PriorityQueue(child.g + child.h, child)
    child.g = Node.g + 1
    child.h = futureFunction(0)
    print(q.queue)
# A star Misplaced Tile Algorithm
def MisplacedTileQueingFunction(Node, children):
    from queue import PriorityQueue # This is our PriorityQueue
    q = PriorityQueue()
    children = [node()] # This is our child object
    for child in children:
        global current_state # global variables
        global goal_state # global variables
        global count
        current_state = np.array([[8, 3, 2], [4, 5, 6], [7, 1, 0]])
        goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        misplaced_tiles = np.sum(current_state != goal_state) - 1
        q.PriorityQueue(child.g + child.h, child)
    child.g = node.g + 1
    child.h = futureFunction(child)
    print(q.queue)
#def ManhattanDistanceFunction(node):
#    h = 0
#    for r in range(3):
#        for j in range(3):
def select_and_init_algorithm(user_puzzle):
    aNode = node() # Created a node object
    child = [node()] # Created a child object
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
    "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        uniform_cost_searchQueingFunction(aNode, child)
    if algorithm == "2":
        MisplacedTileQueingFunction(aNode, child)
    if algorithm == "3":
        ManhattanDistanceFunction(node)
import numpy as np
class node:
    state_board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) # initial board of the matrix
    h = 0;
    g = 0;
class Problem:
    def __init__(self, initial_state, goal_state, operators):
        initial_state = []
        goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        operators = ["move up", "move down", "move left", "move right"] # list of operators
    def expand(node, operators): # This is to return all the valid children in the puzzle
        for operator in operators:
            if "move up ":
                new_puzzle = node.state_board
                pop()
            else:
                return
            if "move down ":
                new_puzzle = node.state_board
                swap()
            if "move left ":
                new_puzzle = node.state_board
                pop()
            if "move right ":
                new_puzzle = node.state_board
                pop()
            else:
                return
#def SwapTile(node): #This is to Swap Tile and swap returns puzzle happening
#def getCurrentRowCol(node, queryTile):
#    row, col = getCurrentRowCol()
#return[row, col]
main()
select_and_init_default_puzzle_mode()
