# 给定一棵树的前序遍历 preorder 与中序遍历 inorder。请构造二叉树并返回其根节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder 和 inorder 均无重复元素 
#  inorder 均出现在 preorder 
#  preorder 保证为二叉树的前序遍历序列 
#  inorder 保证为二叉树的中序遍历序列 
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1259 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """

        :param preorder:
        :param inorder:
        :return:
        """
        def buildSubTree(pre_left, pre_right, in_left, in_right):
            """

            :param pre_left: 前序遍历起始index
            :param pre_right: 前序遍历结束index
            :param in_left: 中序遍历起始index
            :param in_right: 中序遍历结束index
            :return:
            """
            if pre_left > pre_right:
                return None
            # pre_left是当前根节点,中序遍历根节点位置，用来求左右子树长度
            in_root_idx = idx[preorder[pre_left]]
            root = TreeNode(preorder[pre_left])
            #左子树长度，用来定位左子树前序遍历，中序遍历的下标
            left_len = in_root_idx-in_left
            root.left = buildSubTree(pre_left+1,pre_left+left_len,in_left,in_root_idx-1)
            root.right = buildSubTree(pre_left+left_len+1,pre_right,in_root_idx+1,in_right)
            return root

        idx = {element: i for i, element in enumerate(inorder)}
        n = len(preorder)
        return buildSubTree(0, n - 1, 0, n - 1)

# leetcode submit region end(Prohibit modification and deletion)
