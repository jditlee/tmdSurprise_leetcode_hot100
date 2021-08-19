# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  
#  
#  Related Topics 树 二叉搜索树 动态规划 回溯 二叉树 
#  👍 958 👎 0

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        二叉搜索树：左子树所有节点的值 < 根节点 < 右子树所有节点的值
        当根节点为i,那么左子树节点的值为[1,i),右子树节点的值为(i,n],
        递归求解

        :param n:
        :return:
        """
        def getTrees(start,end):
            if start>end:
                return [None]
            allTree = []
            for i in range(start,end+1):
                l=getTrees(start,i-1)
                r=getTrees(i+1,end)
                for a in l:
                    for b in r:
                        node = TreeNode(i)
                        node.left = a
                        node.right = b
                        allTree.append(node)
            return allTree

        return getTrees(1,n)

# leetcode submit region end(Prohibit modification and deletion)
