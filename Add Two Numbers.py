class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        node = result
        temp = 0
        while l1 and l2:
            node.val = (l1.val + l2.val + temp) % 10
            if l1.next or l2.next:
                node.next = ListNode()
                node = node.next
            temp =  (l1.val + l2.val + temp) // 10
            l1 = l1.next
            l2 = l2.next
        if not l1 and l2:
            l1 = l2
        while l1:
            node.val = (l1.val + temp) % 10
            temp = (l1.val + temp) // 10
            if l1.next:
                node.next = ListNode()
                node = node.next
            l1 = l1.next
        if temp == 1:
            node.next = ListNode()
            node = node.next
            node.val = 1
        return result