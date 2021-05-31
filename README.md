# A1 - AI INTRO
    - In this assignment, we must complete three problem (N-Puzzle, Sudoku, Finding path) relate to 
    search algorithm and informed algorithm (Depth First Search, Genetic Algorithm, A* Algorithm).
    - Environment : python 3.8
    - Implemented problem at least three file (include README.md).
    - Comment , explain clearly each function in each file.
    -  Problems can be formulated as a problem as follows:
        - 'State'
        - 'Initial State'
        - 'Goal State'
        - 'Legal moves'
        - 'Heuristic Function'
## N - Puzzle
    N - Puzzle is played on a n-by-n (from which : n = square root of N) grid with (N - 1) square blocks labeled 1 through N and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide blocks horizontally or vertically into the blank square.
### Implementation
    - Implement N-Puzzle based on Depth First Search (DFS).
### Compile and run
    - python np.py
### Result
    - make a file 'out.txt' contains {initial state, how to move(Up, Down, Left, Right) and state of N-Puzzle at that moment, goal state}. 
    - Example of file 'out.txt':
    
       '---Init State---
        [2, 3, 1, 0]

        ---Goal State---
        [0, 3, 2, 1]

        ----------------
        Solution
        ----------------
        Up
        [2, 0, 1, 3]
        Left
        [0, 2, 1, 3]
        Down
        [1, 2, 0, 3]
        Right
        [1, 2, 3, 0]
        Up
        [1, 0, 3, 2]
        Left
        [0, 1, 3, 2]
        Down
        [3, 1, 0, 2]
        Right
        [3, 1, 2, 0]
        Up
        [3, 0, 2, 1]
        Left
        [0, 3, 2, 1]'