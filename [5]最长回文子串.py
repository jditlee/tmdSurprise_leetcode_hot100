# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 👍 4036 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        动态规划：dp[i][j]代表从s[i]到s[j]是否是回文串，那么就有
        dp[i][j]=True if i==j
        dp[i][j]= s[i]==s[j] if i==j-1
        dp[i][j]= s[i]==s[j] and dp[i+1][j-1]
        :param s:
        :return:
        """
        n = len(s)
        if n == 1: return s
        dp = [[False] * n for _ in range(n)]
        maxlen,begin=0,1
        # 因为需要提前知道dp[i + 1][j - 1]，所以i是从大到小遍历，j是从小到大遍历，j<i题意不符
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                elif i == j-1:
                    dp[i][j]=s[i]==s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                # 是回文串就判断长度，记录开始位置和长度
                if dp[i][j] and j-i+1>maxlen:
                    maxlen = j-i+1
                    begin = i
        return s[begin:begin+maxlen]
# leetcode submit region end(Prohibit modification and deletion)
