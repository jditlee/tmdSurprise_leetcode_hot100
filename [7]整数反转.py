# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−231, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -231 <= x <= 231 - 1 
#  
#  Related Topics 数学 
#  👍 2910 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        MIN,MAX=-2**31,2**31-1

        res = 0
        while x!=0:
            if res<MIN//10+1 or res > MAX//10:
                return 0
            dig = x%10
            # python3小于的数取余特殊，结果为 x-n*(x//n) n是除数，x是被除数，而python中x//n向下取整，所以需要特殊处理
            if x<0:
                dig=x%-10
            # 整除也要特殊处理
            x = (x-dig)//10

            res = res*10+dig

        return res

    def reverse1(self, x: int) -> int:
        flag = 0
        if x < 0:
            x=-x
            flag=1
        res = 0
        while x != 0:
            res = res*10 + x%10
            x//=10
        if flag==1:
            res = -res
        if res > 2**31-1 or res < -2**31:
            return 0
        return res




if __name__ == '__main__':
    # print(Solution().reverse(-123))
    print(-123//10)
    # print(0==-0)
# leetcode submit region end(Prohibit modification and deletion)
