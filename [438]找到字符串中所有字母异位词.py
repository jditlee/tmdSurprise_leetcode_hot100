# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  异位词 指字母相同，但排列不同的字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, p.length <= 3 * 104 
#  s 和 p 仅包含小写字母 
#  
#  Related Topics 哈希表 字符串 滑动窗口 
#  👍 577 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        滑动窗口+数组
        :param s:
        :param p:
        :return:
        """
        m, n, res = len(p), len(s), []
        if m > n:
            return res
        parr, sarr = [0] * 26, [0] * 26
        for i in range(m):
            parr[ord(p[i]) - ord('a')] += 1
            sarr[ord(s[i]) - ord('a')] += 1
        if parr==sarr:
            res.append(0)
        for j in range(m,n):
            sarr[ord(s[j-m]) - ord('a')] -= 1
            sarr[ord(s[j]) - ord('a')] += 1
            if sarr==parr:
                res.append(j-m+1)
        return res


    # leetcode submit region end(Prohibit modification and deletion)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        超时
        :param s:
        :param p:
        :return:
        """
        plen = len(p)
        res = []
        for i in range(len(s) - (plen - 1)):
            count = collections.Counter(p)
            for j in range(plen):
                ch = s[i + j]
                if ch not in count or count[ch] <= 0:
                    break
                count[ch] -= 1
            if j == plen - 1 and [count[item] for item in count] == [0] * len(count.items()):
                res.append(i)
        return res


if __name__ == '__main__':
    # print(Solution().findAnagrams("abab", "ab"))
    # print(Solution().findAnagrams("cbaebabacd", "abc"))
    print(Solution().findAnagrams("baa", "aa"))
    # p = "abc"
    # count = collections.Counter(p)
    # a = [count[item] for item in count]
    # print(type(a))
    # print(a)
    # print(count.values())
    # print(type(count.values()))
    # print(count.values() == [0] * len(p))
    # print(count.values() == [1] * len(p))
    # print(a == [1] * len(p))
    # print(count['a'])
    # print(count)
    # print(type(count))
    # print('a' in count)
    # for j in range(3):
    #     print(j)
    # print("循环外", j)
