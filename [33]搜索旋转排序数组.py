# 整数数组 nums 按升序排列，数组中的值 互不相同 。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1], target = 0
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10^4 <= nums[i] <= 10^4 
#  nums 中的每个值都 独一无二 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -10^4 <= target <= 10^4 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？ 
#  Related Topics 数组 二分查找 👍 1564 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1



# leetcode submit region end(Prohibit modification and deletion)


    def search2(self, nums: List[int], target: int) -> int:
        i = nums.index(min(nums))
        print(i)
        l, r = 0, len(nums) - 1
        if i > 0 and nums[0] <= target and target <= nums[i - 1]:
            r = i - 1
        else:
            l = i

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid;

            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1
if __name__ == '__main__':
    print(Solution().search([3,1],1))
    print(Solution().search1([3,1],1))