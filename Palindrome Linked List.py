# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head

        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None
