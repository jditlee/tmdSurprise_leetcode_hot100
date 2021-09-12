# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 二分查找 👍 1203 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        def getleft(tar):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= tar:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        a = getleft(target)
        b = getleft(target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        return [a, b - 1]

# leetcode submit region end(Prohibit modification and deletion)
