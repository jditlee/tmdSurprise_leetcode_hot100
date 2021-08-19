# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  进阶： 
# 
#  
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 104] 内 
#  -105 <= Node.val <= 105 
#  
#  Related Topics 链表 双指针 分治 排序 归并排序 
#  👍 1214 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow, fast = slow.next, fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head,mid),sortFunc(mid,tail))

        def merge(la:ListNode, lb:ListNode)->ListNode:
            if not la:return lb
            if not lb:return la
            l1,l2,l3=la,lb,ListNode(-1)
            newl =l3
            while l1 and l2:
                if l1.val<l2.val:
                    newl.next = l1
                    l1 = l1.next
                else:
                    newl.next = l2
                    l2=l2.next
                newl = newl.next
            if l1:newl.next=l1
            if l2:newl.next=l2
            return l3.next

        return sortFunc(head,None)

# leetcode submit region end(Prohibit modification and deletion)
