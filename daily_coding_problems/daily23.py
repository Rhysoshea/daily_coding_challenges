"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

from collections import deque

def valid_direction(board, x, y):
    m = len(board)
    n = len(board[0])
    if x >= 0 and x < m and y >= 0 and y < n and not board[x][y]:
        return True
    return False


'''---'''

def maze_solver(input, start, end, path_matrix, current_length):
    x, y = start[0], start[1]

    if (x,y) == end:
        path_matrix[x][y] = current_length
        return True

    directions = [(x, y-1), #left
                  (x-1, y), #up
                  (x, y+1), #right
                  (x+1, y)] #down

    for direction in directions:
        if valid_direction(input, direction[0], direction[1]):
            # print (direction[0], direction[1])
            if not path_matrix[direction[0]][direction[1]] or path_matrix[direction[0]][direction[1]] > current_length:
                path_matrix[direction[0]][direction[1]] = current_length

                maze_solver(input, (direction[0], direction[1]), end, path_matrix, current_length+1)



def solution_recursive(input, start, end):
    path_matrix = [[False for x in y] for y in input]
    # pathways = []
    # current_length = 0
    x, y = start[0], start[1]
    path_matrix[x][y] = 0
    # seen = set()
    current_length = path_matrix[x][y]
    maze_solver(input, start, end, path_matrix, current_length)

    # print solver matrix
    # for i in path_matrix:
    #     print (i)
    return path_matrix[end[0]][end[1]]

'''------'''

def get_walkable_neighbors(board, x, y):
    return [(r,c) for r, c in[
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y)]
            if valid_direction(board, r, c)
    ]

# using breadth first search
def solution(input, start, end):
    seen = set()
    queue = deque([(start,0)])
    while queue:
        coords, count = queue.popleft()
        # print (coords)
        if coords == end:
            return count
        seen.add(coords)
        neighbors = get_walkable_neighbors(input, coords[0], coords[1])
        queue.extend((neighbor, count+1) for neighbor in neighbors if neighbor not in seen)

def test1(input, start, end, ans):
    assert (solution_recursive(input, start, end) == ans)

def test2(input, start, end, ans):
    assert (solution(input, start, end) == ans)


input = [[False, False, False, False],
         [True , True , False, True ],
         [False, False, False, False],
         [False, False, False, False]]
start = (3,0)
end = (0,0)

input2 = [[False, False, False, False],
         [False , True , False, False ],
         [False, True, False, True],
         [False, False, False, True]]
start2 = (3,0)
end2 = (1,2)

input3 = [[False, False, False, False, False],
         [False , True , False, True, False ],
         [False, False, False, False, False],
         [False, True, False, True, False],
         [False, False, False, False, False]]

start3 = (2,2)
end3 = (4,4)

# print(solution_recursive(input3, start3, end3))
print(solution(input3, start3, end3))

test1(input, start, end, 7)
test1(input2, start2, end2, 4)
test1(input3, start3, end3, 4)

test2(input, start, end, 7)
test2(input2, start2, end2, 4)
test2(input3, start3, end3, 4)
