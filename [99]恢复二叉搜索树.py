# 给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。 
# 
#  进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。 
# 
#  
# 
#  提示： 
# 
#  
#  树上节点的数目在范围 [2, 1000] 内 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 
#  👍 528 👎 0
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        在递归过程中找到错误的位置
        """
        self.x, self.y, self.pre = None, None, None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            # 这里直接存节点，方便后面修改值
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root
            dfs(root.right)

        dfs(root)

        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val

    # leetcode submit region end(Prohibit modification and deletion)
    def recoverTree1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        用一个数组存中序遍历结果，找出顺序错误的位置
        """
        sortarr = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            # 这里直接存节点，方便后面修改值
            sortarr.append(root)
            dfs(root.right)

        dfs(root)
        x, y, pre = None, None, sortarr[0]

        for i in range(1, len(sortarr)):
            if pre.val > sortarr[i].val:
                y = sortarr[i]
                if not x:
                    x = pre
            pre = sortarr[i]
        if x and y:
            x.val, y.val = y.val, x.val
