#encoding=utf-8
from collections import deque

# 定义华容道游戏的初始状态和目标状态
initial_state = [[4, 4, 0], [1, 2, 3], [7, 5, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

# 定义状态转移函数，根据当前状态和移动方向生成新的状态
def get_next_states(state):
    next_states = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上、下、左、右四个方向
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if 0 <= new_i < 3 and 0 <= new_j < 3:
                        new_state = [row[:] for row in state]  # 复制当前状态
                        new_state[i][j] = new_state[new_i][new_j]
                        new_state[new_i][new_j] = 0
                        next_states.append(new_state)
    return next_states

# 使用广度优先搜索找到曹操的出口路径
def solve_game(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal_state:
            return path
        
        visited.add(tuple(tuple(row) for row in state))
        
        next_states = get_next_states(state)
        for next_state in next_states:
            if tuple(tuple(row) for row in next_state) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# 解决华容道游戏并输出结果
solution = solve_game(initial_state, goal_state)
if solution:
    print("solution:")
    for step in solution:
        print(step)
else:
    print("no solution")