# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 栈 递归 链表 双指针 
#  👍 1050 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return False
        p1,p2=head,head
        stack = list()
        while p2:
            stack.append(p1.val)
            p1=p1.next
            if p2.next:
                p2=p2.next.next
            else:
                # p2.next为空代表是基数个链表，弹出中间位
                stack.pop()
                break
        while p1:
            tmp = stack.pop()
            if p1.val != tmp:
                return False
            p1 = p1.next
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    head = ListNode(1)
    node = head
    for i in range(2,5):
        node.next=ListNode(i)
        node = node.next
    for i in range(5,0,-1):
        node.next = ListNode(i)
        node = node.next
    print(Solution().isPalindrome(head))
    while head:
        print(head.val,end="->")
        head=head.next