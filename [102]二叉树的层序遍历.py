# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 966 👎 0
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        from collections import deque
        dq = deque()
        dq.append(root)
        res = []
        while dq:
            dqsize = len(dq)
            tmp = []
            for i in range(dqsize):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)

            res.append(tmp)

        return res


# leetcode submit region end(Prohibit modification and deletion)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        from collections import deque
        dq = deque()
        dq.append(root)
        res = []
        while dq:
            n = len(dq)
            t = []
            for i in range(n):
                node = dq.popleft()
                t.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res.append(t)
        return res


if __name__ == '__main__':
    t = []
    # t.append(1)
    # t.append(2)
    # print(t)
    # t.insert(0,5)
    # print(t)
    # t.insert(-1,6)
    # print(t)
