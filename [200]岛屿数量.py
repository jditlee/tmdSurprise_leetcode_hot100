# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 1233 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            grid[r][c] = 0
            for x, y in ((r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)):
                if 0 <= x < row and 0 <= y < col and grid[x][y]=="1":
                    dfs(x,y)

        row = len(grid)
        col = len(grid[0])
        numisland = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    numisland += 1
                    dfs(r, c)
        return numisland

# leetcode submit region end(Prohibit modification and deletion)
