# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        res = ListNode(0, head)
        del_node = res
        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            del_node = del_node.next

        del_node.next = del_node.next.next
        return res.next