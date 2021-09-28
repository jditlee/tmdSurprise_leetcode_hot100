# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 1903 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        动态规划：优化内存
        :param n:
        :return:
        """
        a = b = 1
        # ab都为1循环n-1次，就不用判断n<2的情况了
        for i in range(n - 1):
            a, b = b, a + b
        return b
# leetcode submit region end(Prohibit modification and deletion)
    def climbStairs1(self, n: int) -> int:
        """
        动态规划
        :param n:
        :return:
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs3(self, n: int) -> int:
        """
        超时递归
        :param n:
        :return:
        """
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    dp={}
    def climbStairs4(self, n: int) -> int:
        """
        递归优化
        :param n:
        :return:
        """
        if n<=3:
            return n
        if n in self.dp:return self.dp[n]

        self.dp[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dp[n]