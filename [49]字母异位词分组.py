# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。 
# 
#  字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# 
#  示例 2: 
# 
#  
# 输入: strs = [""]
# 输出: [[""]]
#  
# 
#  示例 3: 
# 
#  
# 输入: strs = ["a"]
# 输出: [["a"]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] 仅包含小写字母 
#  
#  Related Topics 哈希表 字符串 排序 👍 856 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        题目说明：数组中每个字符串 字符相同 的划分为一个列表
        :param strs:
        :return:
        """
        d = dict()
        for s in strs:
            t = "".join(sorted(s))
            # 判断d中是否存在key为t的值
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        return list(d.values())


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    S = "abc"
    print("".join(sorted(S)))
    d = {"abd":["dba"],"csa":["acs","cas"]}
    print("abd" in d)
    print("aba" in d)
    print("dba" in d)
    print("csa" in d)
    print("acs" in d)
