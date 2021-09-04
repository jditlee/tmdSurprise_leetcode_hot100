# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针 排序 👍 873 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k1 = k - 1
                    while j < k1 and nums[k1] == nums[k]:
                        k1 -= 1
                    k = k1
                else:
                    j1 = j + 1
                    while k > j1 and nums[j1] == nums[j]:
                        j1 += 1
                    j = j1
        return best



# leetcode submit region end(Prohibit modification and deletion)

    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        # 枚举 a
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best
if __name__ == '__main__':
    print(Solution().threeSumClosest1([-1,2,1,-4],1))