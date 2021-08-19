# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。 
# 
#  说明： 
# 
#  
#  拆分时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#  
# 
#  示例 2： 
# 
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  
#  Related Topics 字典树 记忆化搜索 哈希表 字符串 动态规划 
#  👍 1049 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """

        :param s:
        :param wordDict:
        :return:
        """
        import functools

        @functools.lru_cache(None)
        def back_tack(s):
            if not s:
                return True
            res = False
            for i in range(1,len(s)+1):
                # print("1:",s[:i],res)
                if s[:i] in wordDict:
                    # print("2:", s[:i], res)
                    res = res or back_tack(s[i:])
                    # print("3:", s[:i], res)
            return res
        return back_tack(s)

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        """
        动态规划 时间复杂度O(n^2) 空间复杂度O(n)
        :param s:
        :param wordDict:
        :return:
        """
        size = len(s)
        dp = [True]+[False]*size
        for i in range(size):
            for j in range(i+1,size+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]



def fab(n):
    if n<2:
        return n
    return fab(n-1)+fab(n-2)

if __name__ == '__main__':
    s = "hello"
    wordDict = ["he","llo"]
    print(Solution().wordBreak(s,wordDict))
    # print(len(s))
    # print(s[0:1])
    # print(s[0:4])
    # print(fab(6))



# leetcode submit region end(Prohibit modification and deletion)
