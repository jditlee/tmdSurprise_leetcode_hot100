# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 104 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
# 
#  进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？ 
#  Related Topics 数组 哈希表 
#  👍 11845 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hash字典存num对应的index，
        遍历一次，查看target-当前num的值是否存在字典中
        :param nums:
        :param target:
        :return:
        """
        hashtable = dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[num] = i
        return []



# leetcode submit region end(Prohibit modification and deletion)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        暴力遍历两两数之和
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

if __name__ == '__main__':
    print(Solution().twoSum([1,2,3],5))