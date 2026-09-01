class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 存入queue
        rows, cols = len(grid), len(grid[0])
        queue = deque ()
        count = 0
        for row in range (rows):
            for col in range (cols):
                if grid[row][col] == 2: 
                    queue.append((row, col,0)) 
                elif grid[row][col] == 1:
                    count += 1

        # 单源BFS    
        max_val = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        while queue:
            row, col,time = queue.popleft()
            for d_row, d_col in directions:
                new_row , new_col = row+ d_row , col + d_col
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    count -=1 
                    queue.append((new_row, new_col,time + 1))
                    max_val = max(max_val , time + 1)
                    continue

        if count == 0: 
            return max_val
        else:
            return -1
                
            