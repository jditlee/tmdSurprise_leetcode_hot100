# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。 
# 
#  现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
#  1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。 
# 
#  求所能获得硬币的最大数量。 
# 
#  
# 示例 1：
# 
#  
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,5]
# 输出：10
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 500 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 762 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
from typing import List


class Solution:
    # 动规
    def maxCoins(self, nums: List[int]) -> int:
        newnum = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    total = newnum[i]*newnum[k]*newnum[j]
                    total+= dp[i][k]+dp[k][j]
                    dp[i][j] = max(total,dp[i][j])
        return dp[0][n+1]
    # leetcode submit region end(Prohibit modification and deletion)
    # 记忆化搜索
    def maxCoins1(self, nums: List[int]) -> int:
        newnum = [1] + nums + [1]
        @lru_cache(None)
        def res(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            resol = 0
            for i in range(left + 1, right):
                total = newnum[left] * newnum[i] * newnum[right]
                total += res(left, i) + res(i, right)
                resol = max(resol, total)
            return resol
        return res(0, len(nums) + 1)

    @lru_cache(None)
    def res1(self, left: int, right: int) -> int:
        print("cal", left, right)
        return left * right


if __name__ == '__main__':
    @lru_cache(None)
    def res12(left: int, right: int) -> int:
        print("cal", left, right)
        return left * right


    print(res12(1, 2))
    print(res12(1, 2))
    print(res12(1, 2))
