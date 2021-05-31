
"""
TODO: How to solve N-Puzzle Problem by using Depth First Search.
"""
#   contains all required functions that writes
#   the solution into a file (contains result). 
#
#   legal_moves function: creates a list with all the moves 0 is allowed to do given its
#   coordinates in the form (row,column).
#
#   generate_child function: it generates children for every node, where node is a state and
#   ech child is a possible next state.
#
#   find_path function: backtraces the path to a given node, in this case the final state.
#
#   dfs function: depthh-first search algorithm, based on the algorithm given in the book.
#

import numpy as np

"""
TODO: Initilize state (begin) and goal state (final state).
"""
# Creat random n (n x n: size of N-puzzle with n x n = N).
# In this task, we random size puzzle between (2,5). We can random (number > 5) and solve, but it spends a lot of time.
n = np.random.randint(2,5)

# make random state and goal state.
state = []
s = np.random.permutation(n*n)
for k in s:
        state.append(k)         # adds every number in the list

goal_state = []
gs = np.random.permutation(n*n)
for k in gs:
        goal_state.append(k)    # adds every number in the list
print(state)
print(goal_state)

"""
TODO: make legal moves
"""
# Returns a list with legal moves of 0 for a given state.
def legal_moves(row,col):
    global n                # n is the nuber of rown and columns
        
    legal_action = ['Down', 'Left', 'Up','Right']
    if row == 0:            # up is not not allowed at the top row
        legal_action.remove('Up')
    elif row == n-1:        # down is not allowed at the bottom row
        legal_action.remove('Down')
    if col == 0:            # Left is not allowed at the leftost column
        legal_action.remove('Left')
    elif col == n-1:        # Right is not allowed at the rightmost column
        legal_action.remove('Right')
    return legal_action

"""
TODO: generate child nodes
"""
# Retuns the children, i.e. next states, for a given node/state, based on the legal moves.
def generate_child(node):
    
    children = []           # list of children    
        
    x = node.index(0)       # index of zero in the list,  i.e. where is the zero. 
                            # Note that the NxN matrix has been converted to 1D matix, i.e. a list

    parent = node           # stores the curent state as the oaret state
    
    i = int(x / n)          # row
    j = int(x % n)          # column
    
    legal_actions=legal_moves(i,j)  # calls the function legal_moves

    for action in legal_actions:

        new_state = node.copy()     # loop always starts with the curent state, and then find the child
            
        if action == 'Down':
            new_state[x], new_state[x+n] = new_state[x+n], new_state[x]
            
        elif action == 'Left':
            new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
                                    # for each move in the list, it changes the index of 0 accordingly
        elif action == 'Up':
            new_state[x], new_state[x-n] = new_state[x-n], new_state[x]
            
        elif action == 'Right':
            new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            
            
        children.append([new_state,action,parent]) 
                                    # puts in the chidren list the child, the action that resulted to that state, and the parent state
    return children


"""
TODO: Debpth First Search Algorithm
"""   
def dfs(initialState,goalState):

    snode = initialState                        # start node

    
    frontier = []                               # a LIFO list
    frontier.append(snode)

    family = [[initialState,None,None]]         # keeps track of all nodes. It is a big list that has smaller lists of children. Necesary to backtrace the path.
    explored = []                               # keeps track of the explored node to avoid recheckig the same node and falling into a loop

    if snode == goal_state:
        return find_path(family)
    
    while frontier:
        node = frontier.pop()                   # chooses the swallowest node in frontier, but we are using LIFO, so it is not actually the swaloest
        explored.append(node)                   # puts node in the explore list

        ch = generate_child(node)               # calls the generate_child function to return a list of children of the node
           
        
        for child in ch:                        # child has the form [[child node],'action',[parent node]]. 
            
            if child[0] not in explored and child[0] not in frontier: 
                                                # traces the child nodes from the list ch that contains all child nodes for a given node

                family.append(child)            # adds the child in the family list

                if child[0] == goalState:       # tests if the child node is the goal state
                    
                    frontier.append(child[0])   # puts child node in the frontier 
                    return find_path(family)    # calls the find_path function
       
                frontier.append(child[0])       # puts child node in the frontier
                               
    return

"""
TODO: Finding path
"""
# Returns a list with the moves 0 needs to make fpr the puzzle to be solved.      
def find_path(node):                # node is the big list family

    #it has the form [[[child node],'action',[parent node]],[[child node],'action',[parent node]],...,[[final node],'action',[parent node]]]
    #the last list has the final node, so we start form there.
    
    steps = [(node[-1])[1]]         # list of steps

    parent = (node[-1])[2]          # list of parents
    
    while parent != None:           # traces thourgh family list
        for p in node:              # only the first state has None as parent
            if p[0] == parent:      # if the state of a node is the parent of the node we are curently in..
               steps.append(p[1])   #... add the step in the list
               parent = p[2]        # add the parent of that node in the list

    steps.pop(-1)   # removes the last step at the end of the list, which is None
    steps.reverse() # since we BACKtraced the path, we need to reverse the list    
                    
    return steps    # return a list with the steps

