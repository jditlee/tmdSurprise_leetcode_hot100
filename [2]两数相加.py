# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。 
# 
#  请你将两个数相加，并以相同形式返回一个表示和的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个链表中的节点数在范围 [1, 100] 内 
#  0 <= Node.val <= 9 
#  题目数据保证列表表示的数字不含前导零 
#  
#  Related Topics 递归 链表 数学 
#  👍 6611 👎 0
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

class Solution:
    """
    思路：两个链表从头加到尾，需要注意进位情况，
    添加一个标志位记录进位的值，两个节点相加时还要加上前一位进位的值
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        优化，循环里面的代码都一样，写在一个循环里面，l1和l2都为空才停止循环
        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)
        p = head
        c = 0
        while l1 or l2:
            a = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            p.next = ListNode(a % 10)
            c = a // 10
            p = p.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if c > 0:
            p.next = ListNode(1)
        return head.next

    # leetcode submit region end(Prohibit modification and deletion)

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        暴力解法
        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)
        p = head
        c = 0
        while l1 and l2:
            a = l1.val + l2.val + c
            b = a % 10
            p.next = ListNode(b)
            c = a // 10
            p = p.next
            l1, l2 = l1.next, l2.next
        while l1:
            a = l1.val + c
            b = a % 10
            p.next = ListNode(b)
            c = a // 10
            p = p.next
            l1 = l1.next
        while l2:
            a = l2.val + c
            b = a % 10
            p.next = ListNode(b)
            c = a // 10
            p = p.next
            l2 = l2.next
        if c > 0:
            p.next = ListNode(1)
        return head.next


if __name__ == '__main__':
    print(Solution().addTwoNumbers())
