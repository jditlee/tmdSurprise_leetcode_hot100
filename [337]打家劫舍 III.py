# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“
# 房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。 
# 
#  计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。 
# 
#  示例 1: 
# 
#  输入: [3,2,3,null,3,null,1]
# 
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7. 
# 
#  示例 2: 
# 
#  输入: [3,4,5,1,3,null,1]
# 
#   3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#  
#  Related Topics 树 深度优先搜索 动态规划 二叉树 
#  👍 919 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        f = dict()
        g = dict()

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val + g.get(node.left, 0) + g.get(node.right, 0)
            g[node] = max(f.get(node.left, 0), g.get(node.left, 0)) + max(f.get(node.right, 0),
                                                                          g.get(node.right, 0))
        dfs(root)
        return max(f[root], g[root])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    h = dict()
    h["1"] = 3
    print(h.get("1", 0))
