# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  
# 
#  进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics 并查集 数组 哈希表 
#  👍 824 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # nums_set = set(nums)
        dic = dict()
        res = 0
        for num in nums:
            if num not in dic:
                left = dic.get(num - 1, 0)
                right = dic.get(num + 1, 0)
                curlen = left + right + 1
                res = max(res, curlen)
                dic[num] = dic[num - left] = dic[num + right] = curlen
        return res

    def longestConsecutive1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        x = sorted(nums_set)
        maxlong = 1
        curlong = 1
        for i in range(1, len(x)):
            if x[i] == x[i - 1] + 1:
                curlong += 1
                maxlong = max(maxlong, curlong)
            else:
                curlong = 1
        return maxlong


if __name__ == '__main__':
    test = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # test = [100, 4, 200, 1, 3, 2,2]
    print(Solution().longestConsecutive(test))
# leetcode submit region end(Prohibit modification and deletion)
