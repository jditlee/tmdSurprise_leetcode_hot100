# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  有效括号组合需满足：左括号必须以正确的顺序闭合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 动态规划 回溯 👍 2029 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(S, left, right):
            if len(S) == 2 * n:
                print("left:", left, "===right:", right, "===appS:", S)
                res.append("".join(S))
                return
            if left < n:
                S.append("(")
                print("left:",left,"===right:",right,"===S:",S)
                dfs(S, left + 1, right)
                print("left:",left,"===right:",right,"===S:",S)
                S.pop()
            if right < left:
                S.append(")")
                print("left:",left,"===right:",right,"===S:",S)
                dfs(S, left, right + 1)
                print("left:",left,"===right:",right,"===S:",S)
                S.pop()

        dfs([], 0, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().generateParenthesis(3))