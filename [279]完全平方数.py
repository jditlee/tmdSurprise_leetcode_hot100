# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
#  例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 104 
#  
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 1022 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math
import random
from functools import lru_cache


class Solution:
    def numSquares2(self, n: int) -> int:
        return random.randint(1, 4)

    def numSquares(self, n: int) -> int:
        if self.isSquare(n):
            return 1
        if self.isAnswer4(n):
            return 4
        for i in range(int(n ** 0.5) + 1):
            j = n - i * i
            if self.isSquare(j):
                return 2
        return 3

    def isSquare(self, x: int) -> bool:
        return int(x ** 0.5) ** 2 == x

    # if n=4^k*(8m+7) return 4
    # n/=(4^k)
    # n=(8m+7)
    # x%8==7
    def isAnswer4(self, x: int) -> bool:
        while x % 4 == 0:
            x /= 4
        return x % 8 == 7

    # leetcode submit region end(Prohibit modification and deletion)
    def numSquares1(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while i - j ** 2 >= 0:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[n]


if __name__ == '__main__':
    # print(Solution().numSquares(6922))
    # print(math.sqrt(6922))
    # print(83*83)
    # print(83**2)
    # print(6992-6889)
    for i in range(10):
        print(random.randint(1, 4))
