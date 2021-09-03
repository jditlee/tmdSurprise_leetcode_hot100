# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 3704 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        排序+双指针：
        先排序，然后遍历第一个数：后两数之和等于0-first
        求两数之和为-first:因为是排序的，所以用最小的+最大的来枚举，用到双指针来计算剩下的两数之和
        :param nums:
        :return:
        """
        n = len(nums)
        res = list()
        nums.sort()

        for first in range(n):
            if first>0 and nums[first]==nums[first-1]:
                continue
            third = n-1
            target = -nums[first]
            for second in range(first+1,n):
                if second>first+1 and nums[second]==nums[second-1]:
                    continue
                while second<third and nums[second]+nums[third]>target:
                    third-=1
                if second==third:
                    break
                if nums[second]+nums[third]==target:
                    res.append([nums[first],nums[second],nums[third]])
        return res

# leetcode submit region end(Prohibit modification and deletion)
