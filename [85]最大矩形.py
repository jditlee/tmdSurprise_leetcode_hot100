# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = [["0","0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  0 <= row, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 
#  👍 961 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        # print(m,n)
        # print(matrix)
        left = [[0] * n for _ in range(m)]
        # print(left)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    left[i][j] = (0 if j == 0 else left[i][j-1])+1
        # print(left)
        left = [[0] * n] + left + [[0] * n]
        # print(left)
        res = 0
        m += 2
        for x in range(n):
            stack = [0]
            for y in range(1,m):
                while left[stack[-1]][x]>left[y][x]:
                    curhight = left[stack.pop()][x]
                    curweight = y-stack[-1]-1
                    res = max(curweight*curhight,res)
                stack.append(y)
        return res


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalRectangle(matrix))
# leetcode submit region end(Prohibit modification and deletion)
