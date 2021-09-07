# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "()[]{}"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(]"
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "([)]"
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "{[]}"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由括号 '()[]{}' 组成 
#  
#  Related Topics 栈 字符串 
#  👍 2585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        """
        funny
        :param s:
        :return:
        """
        if len(s) & 1: return False
        while "()" in s or "[]" in s or "{}" in s:
            s=s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""

    # leetcode submit region end(Prohibit modification and deletion)
    def isValid1(self, s: str) -> bool:
        """
        用栈存左边括号，遇到右边括号的时候弹栈判断两种括号是否成对
        :param s:
        :return:
            执行耗时:20 ms,击败了99.79% 的Python3用户
            内存消耗:14.7 MB,击败了99.11% 的Python3用户
        """
        # 判断长度为奇数直接false
        if len(s) & 1: return False
        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                # 栈空就是先遇到右括号的情况，
                # 弹栈判断是否成对
                if not stack or dic[stack.pop()] != i:
                    return False
                # 这三句话浓缩成一句dic[stack.pop()] != i
                # m = stack.pop()
                # if dic[m] != i:
                #     return False
        # return True if not stack else False 这句话真蠢
        return not stack


if __name__ == '__main__':
    print(Solution().isValid("]()"))
