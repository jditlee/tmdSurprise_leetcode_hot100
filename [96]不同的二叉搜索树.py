# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 19 
#  
#  Related Topics 树 二叉搜索树 数学 动态规划 二叉树 👍 1360 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        """
        dp[n] = sum(dp[i-1]*dp[n-i) i=1~n
        :param n:
        :return:
        """
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(n):
            c *= 2 * (2 * i + 1) / (i + 2)
        return int(c)