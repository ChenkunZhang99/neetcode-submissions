class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = 0
        col = 0
        count = 0
        for row in range (len(grid)):
            for col in range (len(grid[0])):
                if grid [row][col]  == "1":
                    self.dfs(grid, row, col)
                    count += 1
        return count
            
    

    def dfs(self, grid, row, col):
                # 终止条件（什么情况下，应该直接return，不再继续扩散）：

        # 1. row或col是否超出了网格的边界？
        # 2. 当前这个格子，是不是水（'0'）？或者已经被访问过（比如已经被标记过了）？
        
        # 如果都不满足终止条件，说明这是一个"未访问的陆地"：
        # 第一步：先标记为已访问（防止死循环、重复计数）
        # 第二步：对上下左右四个方向，递归调用dfs 
        rows = len(grid)
        cols = len(grid[0])

        # 终止条件
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if grid[row][col] == "0":
            return
        # 如果你用的是"直接修改原数组"的标记方式，这里可以省略"已访问"这个判断
        # 因为一旦访问过，就已经被改成"0"了，上面这条"是水"的判断，会顺便把它也拦下来

        # 标记为已访问
        grid[row][col] = "0"

        # 对四个方向，递归调用
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d_row, d_col in directions:
            self.dfs(grid, row + d_row, col + d_col)