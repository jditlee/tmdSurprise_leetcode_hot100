# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
#  Related Topics 位运算 数组 回溯 👍 1345 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def dfs(nums,a):
            if not nums:
                return
            for i in range(len(nums)):
                a.append(nums[i])
                res.append(a.copy())
                dfs(nums[i+1:len(nums)],a)
                a.pop()
        dfs(nums,[])
        return res

    # dfs_list = [[]]
    #
    # def dfs(nums: List[int], res):
    #
    #     if not nums:
    #         return
    #     for i in range(len(nums)):
    #         res.append(nums[i])
    #         dfs_list.append(res.copy())
    #         # print("进入递归",dfs_list)
    #         dfs(nums[i + 1:len(nums)], res)
    #         # print("出递归",dfs_list)
    #         res.pop()
    #
    # dfs(nums, [])
    # return dfs_list
# leetcode submit region end(Prohibit modification and deletion)
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums: res += [[i]+ n for n in res]
        return res