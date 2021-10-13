# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1574 👎 0
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(t1,t2):
            if not t1 and not t2:
                return  True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and dfs(t1.left,t2.right) and dfs(t1.right,t2.left)
        return dfs(root.left,root.right)


# leetcode submit region end(Prohibit modification and deletion)

    def isSymmetric1(self, root: TreeNode) -> bool:
        from collections import deque
        dq = deque()
        dq.append(root)
        while dq:
            dqsize = len(dq)
            # print("dqsize",dqsize)
            res = []
            for i in range(dqsize):
                node = dq.popleft()
                if not node:
                    res.append(None)
                    continue
                res.append(node.val)
                # print(i,":",res)
                dq.append(node.left)
                dq.append(node.right)
            # print("总res",res)
            if res != res[::-1]:
                return False
        return True
if __name__ == '__main__':
    print(Solution().isSymmetric())