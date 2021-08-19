# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 
# 
#  路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,1000] 
#  -109 <= Node.val <= 109 
#  -1000 <= targetSum <= 1000 
#  
#  Related Topics 树 深度优先搜索 二叉树 
#  👍 935 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root: TreeNode, s: List[int]) -> int:
            if not root:
                return 0
            s = [i + root.val for i in s] + [root.val]
            return s.count(targetSum)+dfs(root.left,s)+dfs(root.right,s)
        return dfs(root, [])

    # leetcode submit region end(Prohibit modification and deletion)
    def pathSumError(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root: TreeNode, s: int) -> int:
            if not root:
                return 0
            if s + root.val == targetSum:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            elif s + root.val < targetSum:
                return dfs(root.left, s + root.val) + dfs(root.right, s + root.val) + dfs(root.left, root.val) + dfs(
                    root.right, root.val)
            else:
                return dfs(root.left, root.val) + dfs(root.right, root.val)

        return dfs(root, 0)
