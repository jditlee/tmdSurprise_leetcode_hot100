# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。 
# 
#  返回所有可能的结果。答案可以按 任意顺序 返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ")("
# 输出：[""]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 25 
#  s 由小写英文字母以及括号 '(' 和 ')' 组成 
#  s 中至多含 20 个括号 
#  
#  Related Topics 广度优先搜索 字符串 回溯 
#  👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 使用set去重
        res = set()
        left, right = 0, 0
        for i in s:
            if i == "(":
                left += 1
            if i == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        def dfs(index, leftcount, rightcount, leftremove, rightremove, st):
            """
            :param index: 字符串id
            :param leftcount: 保留的左括号数量
            :param rightcount: 保留的右括号数量
            :param leftremove: 需要移除的左括号数量
            :param rightremove: 需要移除的右括号数量
            :param st: 保留下来的字符串
            :return:
            """
            if index == len(s):
                if leftremove == 0 and rightremove == 0:
                    res.add(st)
                return
            # 删除操作
            if s[index] == "(" and leftremove > 0:
                dfs(index + 1, leftcount, rightcount, leftremove - 1, rightremove, st)
            if s[index] == ")" and rightremove > 0:
                dfs(index + 1, leftcount, rightcount, leftremove, rightremove - 1, st)

            # 不删除操作
            if s[index] not in "()":
                dfs(index + 1, leftcount, rightcount, leftremove, rightremove, st + s[index])
            elif s[index] == "(":
                dfs(index + 1, leftcount + 1, rightcount, leftremove, rightremove, st + s[index])
            elif rightcount < leftcount:
                dfs(index + 1, leftcount, rightcount + 1, leftremove, rightremove, st + s[index])

        dfs(0, 0, 0, left, right, "")
        return list(res)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "()())()"
    r = Solution().removeInvalidParentheses(s)
    print(r)
    print(type(r))
    for i in r:
        print(type(i))
    print(s[0]=="(")