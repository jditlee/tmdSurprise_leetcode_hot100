# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性： 
# 
#  
#  每行的元素从左到右升序排列。 
#  每列的元素从上到下升序排列。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 5
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 20
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -109 <= matix[i][j] <= 109 
#  每行的所有元素从左到右升序排列 
#  每列的所有元素从上到下升序排列 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 二分查找 分治 矩阵 
#  👍 672 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        b1, b2 = m - 1, 0
        while b1 >= 0 and b2 < n:
            if matrix[b1][b2] < target:
                b2 += 1
            elif matrix[b1][b2] > target:
                b1 -= 1
            else:
                return True
        return False

        # def search(ml,mr,nl,nr):
        #     midm, midn = (ml + mr) // 2, (nl + nr) // 2
        #     if midn==0 and midm==0 and matrix[midm][midn] != target:
        #         return False
        #     if matrix[midm][midn] < target:
        #         return search(midm,mr,midn,nr)
        #     elif matrix[midm][midn] > target:
        #         return search(ml,midm,nl,midn)
        #     else:
        #         return True
        #
        # mr, nr = len(matrix), len(matrix[0])
        # ml, nl = 0, 0
        # return search(ml,mr,nl,nr)

    # leetcode submit region end(Prohibit modification and deletion)
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    res = Solution().searchMatrix(matrix, target)
    print(res)
