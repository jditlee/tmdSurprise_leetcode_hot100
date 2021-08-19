# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 单调栈 
#  👍 1424 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调栈+哨兵
        :param heights:
        :return:
        """
        size = len(heights)
        heights = [0]+ heights + [0]
        size +=1
        res = 0
        stack = [0]
        for i in range(size):
            while heights[stack[-1]]>heights[i]:
                curh = heights[stack.pop()]
                curw = i-stack[-1]-1
                res = max(res,curh*curw)
            stack.append(i)
        return res
# leetcode submit region end(Prohibit modification and deletion)
















