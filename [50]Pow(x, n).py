# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x⁴
# 
#  Related Topics 递归 数学 👍 724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(n):
            if n == 0:
                return 1.0
            res = pow(n // 2)
            return res * res * x if n & 1 else res*res
        return pow(n) if n>=0 else 1/pow(-n)

            # return x**n


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(1 & 1)
    print(2 & 1)
    print(3 & 1)
    print(4 & 1)
