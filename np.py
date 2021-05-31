# takes the list of steps from dfs.py, and writes out
# the the steps and the state into file 'out.txt' after each step

"""
TODO: Get data and algorithm
"""
# From solver.py imports the function dfs, and the variables state, goal_state, and n
from dfs import dfs, state, goal_state, n
 
steps = dfs(state,goal_state)           # a list with all the steps

file = open('out.txt','w')              # begin to write
if not steps and state!= goal_state:    # if there are no steps, then the algorithm did not find a solution
    file.write('\n No Solution Could Be Found')
    
elif not steps and state == goal_state: # in case initial and final states are the same
    file.write('\n There is Nothing to Solve')

else:
    file.write('\n' + '---Init State---' + '\n')
    file.write(str(state))
    file.write('\n' + '\n' + '---Goal State---' + '\n')
    file.write(str(goal_state))
    file.write('\n' + '\n' + '----------------')
    file.write('\n' + 'Solution')
    file.write('\n' + '----------------')

    for a in steps:
        t = list(state).index(0)        # finds zero in the list

        file.write('\n' + a + '\n')     # prints the step
                
        if a == 'Up':
            state[t], state[t-n] = state[t-n], state[t]
        elif a == 'Down':
            state[t], state[t+n] = state[t+n], state[t]
        elif a == 'Left':
            state[t], state[t-1] = state[t-1], state[t]
        elif a == 'Right':
            state[t], state[t+1] = state[t+1], state[t]
            
        file.write(str(state))

file.close()
