# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），
# 并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 1176 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxd = mind = res = nums[0]
        for i in range(1, len(nums)):
            mx, mn = maxd, mind
            maxd = max(mx * nums[i], mn * nums[i], nums[i])
            mind = min(mx * nums[i], mn * nums[i], nums[i])
            res = max(res, maxd)
        return maxd

    def maxProduct1(self, nums: List[int]) -> int:
        maxd = [nums[0]] + [0] * (len(nums) - 1)
        mind = [nums[0]] + [0] * (len(nums) - 1)
        res = nums[0]
        for i in range(1, len(nums)):
            maxd[i] = max(maxd[i - 1] * nums[i], mind[i - 1] * nums[i], nums[i])
            mind[i] = min(maxd[i - 1] * nums[i], mind[i - 1] * nums[i], nums[i])
            res = max(res, maxd[i])
        return res


if __name__ == '__main__':
    print(Solution().maxProduct([-4, -3, -2]))
# leetcode submit region end(Prohibit modification and deletion)
