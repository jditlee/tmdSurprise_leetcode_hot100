# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之
# 外其余各元素的乘积。 
# 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,4]
# 输出: [24,12,8,6] 
# 
#  
# 
#  提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。 
# 
#  说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  进阶： 
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。） 
#  Related Topics 数组 前缀和 
#  👍 869 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        优化空间复杂度
        :param nums:
        :return:
        """
        length = len(nums)
        res=[1]*length
        for i in range(1,length):
            res[i] = res[i-1]*nums[i-1]
        R = 1
        for i in range(length-1,-1,-1):
            res[i] = res[i]*R
            R = R*nums[i]
        return res


# leetcode submit region end(Prohibit modification and deletion)

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, res = [1] * length, [1] * length, [1] * length
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(length):
            res[i] = left[i] * right[i]

        return res


if __name__ == '__main__':
    # nums = [-1,1,0,-3,3]
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))