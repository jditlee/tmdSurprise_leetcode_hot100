# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  请你找出符合题意的 最短 子数组，并输出它的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？ 
#  
#  
#  Related Topics 栈 贪心 数组 双指针 排序 单调栈 
#  👍 680 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1
        for i in range(n):
            if maxn <= nums[i]:
                maxn = nums[i]
            else:
                # 不为升序的位置
                right = i
            if minn >= nums[n - 1 - i]:
                minn = nums[n - 1 - i]
            else:
                # 不为降序的位置
                left = n - 1 - i
        return 0 if right == -1 else right - left + 1

    # leetcode submit region end(Prohibit modification and deletion)


    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        """
        排序比较
        :param nums:
        :return:
        """
        n = len(nums)

        def is_sorted() -> bool:

            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        if is_sorted():
            return 0

        nums_sort = sorted(nums)
        left, right = 0, n - 1
        while nums_sort[left] == nums[left]:
            left += 1
        while nums_sort[right] == nums[right]:
            right -= 1
        return right - left + 1
