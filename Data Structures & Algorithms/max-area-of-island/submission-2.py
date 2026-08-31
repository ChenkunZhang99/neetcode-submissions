class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_val = 0
        for row in range (len(grid)):
            for col in range (len(grid[0])):
                if grid[row][col] == 1:
                    max_val = max (max_val, self.maxArea( grid, row, col,0))
        return max_val


    def maxArea(self, grid, row, col, max_val):
        rows = len(grid)
        cols = len(grid[0])
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return max_val
        if grid[row][col] == 0:
            return max_val
        grid[row][col] = 0
        max_val += 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d_row, d_col in directions:
            max_val = self.maxArea(grid, row + d_row, col + d_col,max_val)
        return max_val