# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = ""
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = "2"
# 输出：["a","b","c"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] 是范围 ['2', '9'] 的一个数字。 
#  
#  Related Topics 哈希表 字符串 回溯 👍 1487 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        回溯遍历所有的值
        :param digits:
        :return:
        """
        if digits == '': return []
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        res = []
        def backtrack(idx):
            if idx == len(digits):
                res.append("".join(tmp))
            else:
                for i in KEY[digits[idx]]:
                    tmp.append(i)
                    backtrack(idx+1)
                    tmp.pop()

        tmp = []
        backtrack(0)
        return res


# leetcode submit region end(Prohibit modification and deletion)
