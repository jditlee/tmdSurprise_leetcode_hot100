# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  示例 4: 
# 
#  
# 输入: s = ""
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 
#  👍 5958 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        计算重复元素之间的距离
        :param s:
        :return:
        """
        if len(s) <= 1: return len(s)
        i,res=-1,0
        sidx = {}
        for m in range(len(s)):
            if s[m] in sidx:
                i = max(i,sidx[s[m]])
            res = max(res,m-i)
            sidx[s[m]] = m
        return res

    # leetcode submit region end(Prohibit modification and deletion)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        暴力解法，计算i->j之间是否有重复元素，有的话i++,没有计算长度并且j++
        用了collections.Counter(s).most_common(1)来计算wordcount
        :param s:
        :return:
        """
        if len(s) == 0: return 0
        i, j, n = 0, 1, len(s)
        res = 0
        while j < n + 1:
            a = list(collections.Counter(s[i:j]).most_common(1))[0][1]
            if a > 1:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        遍历每一个元素，如果当前元素之前有重复的，位置就更新到之前重复元素的下一个位置

        :param s:
        :return:
        """

        if len(s) <= 1: return len(s)
        i,j,res=0,1,0
        for m in range(1,len(s)):
            if s[m] in (s[i:j]):
                # s.index(x,i,j)找到s[i:j]中x的下标
                i = s.index(s[m],i,j)+1
            j+=1
            res = max(res,j-i)
        return res

if __name__ == '__main__':
    # print(Solution().lengthOfLongestSubstring("abcabcbb"))
    # s = "abcccddefg"
    # print(s[0:1])
    # print(s[0:2])
    # print(s[0:-1])
    # i,j=0,5
    # a = list(collections.Counter(s[i:j]).most_common(1))[0][1]
    # print(list(a)[0][1])
    s = "abcabcbb"
    print(s.index('a',1,4))