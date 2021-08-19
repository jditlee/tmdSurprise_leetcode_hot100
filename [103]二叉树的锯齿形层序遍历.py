# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层序遍历如下： 
# 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 495 👎 0
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        from collections import deque
        dq = deque()
        dq.append(root)
        res = []
        flag = True
        while dq:
            n = len(dq)
            t = []
            for i in range(n):
                node = dq.popleft()
                if flag:
                    t.append(node.val)
                else:
                    t.insert(0,node.val)
                if node.left:dq.append(node.left)
                if node.right:dq.append(node.right)
            res.append(t)
            flag = not flag
        return res


# leetcode submit region end(Prohibit modification and deletion)
