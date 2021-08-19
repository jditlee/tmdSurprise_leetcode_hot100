# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0
        def plusres(l,r):
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
                self.res += 1
        for i in range(n):
            plusres(i,i)
            plusres(i,i+1)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(2 * n - 1):
            l, r = i // 2, i // 2 + i % 2
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
                res += 1

        return res

    def countSubstrings1(self, s: str) -> int:
        """
        超时
        :param s:
        :return:
        """
        def ispol(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        n = len(s)
        res = n
        for i in range(n):
            for j in range(i+1,n):
                res += 1 if ispol(i,j) else 0
        return res
if __name__ == '__main__':
    # print(2&1)
    # print(3&1)
    # print(4>>1)
    print(Solution().countSubstrings("abaaa"))
    # print(0//2)
    # print(1//2)
    # print(2//2)
    # print(3//2)
