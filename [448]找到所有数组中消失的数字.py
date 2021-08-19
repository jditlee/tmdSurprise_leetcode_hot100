# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数
# 字，并以数组的形式返回结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,1]
# 输出：[2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 105 
#  1 <= nums[i] <= n 
#  
# 
#  进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。 
#  Related Topics 数组 哈希表 
#  👍 785 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in nums:
            a = (i - 1) % n
            nums[a] += n
        res = [i + 1 for i, j in enumerate(nums) if j <= n]
        return res

    # leetcode submit region end(Prohibit modification and deletion)

    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        d = dict(collections.Counter(nums))
        # for i in range(1, n + 1):
        #     if i not in d:
        #         res.append(i)
        res = [i for i in range(1, n + 1) if i not in d]
        return res


if __name__ == '__main__':
    # a = [4, 3, 2, 7, 8, 2, 3, 1]
    # b = collections.Counter(a)
    # print(b)
    # c = dict(b)
    # print(c)
    # print(1 in c)
    # print(5 in c)
    print(Solution().findDisappearedNumbers1([4,3,2,7,8,2,3,1]))
