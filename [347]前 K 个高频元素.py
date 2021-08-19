# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 
#  👍 811 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        桶排序
        :param nums:
        :param k:
        :return:
        """
        newdic = collections.Counter(nums)
        b = [[] for _ in range(len(nums)+1)]
        for i, j in newdic.items():
            b[j].append(i)
        res = list()
        for i in range(len(b) - 1, -1, -1):
            if len(b[i]) != 0:
                res+=b[i]
                if len(res) == k:
                    return res

    # leetcode submit region end(Prohibit modification and deletion)
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        堆排序
        :param nums:
        :param k:
        :return:
        """
        newdic = collections.Counter(nums)
        h = []
        for i, j in newdic.items():
            heapq.heappush(h, (j, i))
            if len(h) > k:
                heapq.heappop(h)
        return [r[1] for r in h]

    def topKFrequent2_2(self, nums: List[int], k: int) -> List[int]:
        """
        堆排序,调用方法heapq.nlargest(n,heap)
        :param nums:
        :param k:
        :return:
        """
        newdic = collections.Counter(nums)
        h = [(val, key) for (key, val) in newdic.items()]
        return [item[1] for item in heapq.nlargest(k, h)]
    def topKFrequent2_3(self, nums: List[int], k: int) -> List[int]:
        """
        堆排序,调用方法heapq.nlargest(n,heap)
        :param nums:
        :param k:
        :return:
        """
        return [item[1] for item in heapq.nlargest(k, [(val, key) for (key, val) in collections.Counter(nums).items()])]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        """
        暴力排序
        :param nums:
        :param k:
        :return:
        """
        numdict = collections.defaultdict(int)
        for i in nums:
            numdict[i] += 1
        newdict = sorted(numdict.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in newdict[:k]]
        # res = list()
        # for i in range(k):
        #     res.append(newdict[i][0])
        # return res

    def topKFrequent1_2(self, nums: List[int], k: int) -> List[int]:
        """
        暴力排序,调用方法newdic.most_common
        :param nums:
        :param k:
        :return:
        """
        newdic = collections.Counter(nums)
        return [item[0] for item in newdic.most_common(k)]

    def topKFrequent1_3(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]


if __name__ == '__main__':
    print(Solution().topKFrequent1([1,1,1,1,1,1,1,1,1,3,3,3,2,2,5,5,5,5,2], 2))
