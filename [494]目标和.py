# 给你一个整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
#  Related Topics 数组 动态规划 回溯 
#  👍 851 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (target + s) & 1: return 0

        V = (target + s) >> 1
        f = [1] + [0] * V
        for n in nums:
            for i in range(V, n - 1, -1):
                f[i] += f[i - n]
        return f[-1]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (s - target) < 0 or (s - target) & 1: return 0
        v = (s - target) >> 1
        dp = [[0] * (v + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(v + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]

        return dp[-1][-1]

    # leetcode submit region end(Prohibit modification and deletion)

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.count = 0

        @lru_cache(None)
        def dfs(sumnums: int, idx: int):
            if idx == n:
                self.count += 1 if sumnums == target else 0
            else:
                dfs(sumnums + nums[idx], idx + 1)
                dfs(sumnums - nums[idx], idx + 1)

        dfs(0, 0)
        return self.count


if __name__ == '__main__':
    print(Solution().findTargetSumWays1([2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 47, 53],
                                       1000))
    print(Solution().findTargetSumWays1([1, 1, 1, 1, 1], 3))
    # print(
    #     Solution().findTargetSumWays([42, 16, 31, 11, 36, 19, 9, 3, 25, 0, 27, 29, 35, 29, 45, 15, 35, 42, 35, 23], 39))
    # print(2 ** 20)
