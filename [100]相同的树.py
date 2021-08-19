# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  两棵树上的节点数目都在范围 [0, 100] 内 
#  -104 <= Node.val <= 104 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 667 👎 0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and  q: return False
        if  p and not q: return False
        if not p and not q: return True
        if p.val != q.val: return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
# leetcode submit region end(Prohibit modification and deletion)
