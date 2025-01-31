# Problem description here https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left, right = dummy, head

        for i in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
    
# Time Complexity = O(N), Space Complexity = O(1)
