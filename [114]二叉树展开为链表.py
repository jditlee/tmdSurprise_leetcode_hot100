# 给你二叉树的根结点 root ，请你将它展开为一个单链表： 
# 
#  
#  展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。 
#  展开后的单链表应该与二叉树 先序遍历 顺序相同。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 2000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？ 
#  Related Topics 栈 树 深度优先搜索 链表 二叉树 👍 952 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
# leetcode submit region end(Prohibit modification and deletion)
