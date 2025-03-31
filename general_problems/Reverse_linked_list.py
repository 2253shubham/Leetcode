# Problem description here https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        return node


# Time Complexity = O(N), Space Complexity = O(1)
