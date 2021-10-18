# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
#  
# 
#  示例 2: 
# 
#  
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  字符串 s 由 ASCII 字符组成 
#  
#  Related Topics 双指针 字符串 👍 424 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(i.lower() for i in s if i.isalnum())
        return s1 == s1[::-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "a bche f g h"
    s1 = "".join(i.lower() for i in s if i.isalnum())
    s2 = (i.lower() for i in s if i.isalnum())
    print(s1)
    print(s2)
