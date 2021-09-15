# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 回溯 👍 1551 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(S, tmp):
            if not S:
                res.append(tmp[:])
                return
            for i in range(len(S)):
                # tmp.append(S[i])
                # dfs(S[:i] + S[i + 1:], tmp)
                # tmp.pop()
                # 三句浓缩成一句，有意思
                dfs(S[:i] + S[i + 1:], tmp + [S[i]])
        res = []
        dfs(nums, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    S = [1, 2, 3]
    print(S[:-1])
    print(S[:0])
    print(S[1:])
    print(S[3:])
    print(Solution().permute(S))
