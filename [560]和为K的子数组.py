# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表 前缀和 
#  👍 1036 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s,c=0,0
        m = collections.defaultdict(int)
        m[0] = 1
        for i in range(len(nums)):
            s+=nums[i]
            c+=m[s-k]
            m[s]+=1
        return c

# leetcode submit region end(Prohibit modification and deletion)
    def subarraySum1(self, nums: List[int], k: int) -> int:
        """
        超时
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        c = 0
        for i in range(n):
            s = 0
            for j in range(i,-1,-1):
                s += nums[j]
                if s==k:
                    c+=1
        return c