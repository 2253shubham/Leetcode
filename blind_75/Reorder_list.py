# Problem description here https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Quick response for empty linked list
        if not head:
            return None

        # Locate the mid point of linked list
        # First half is the linked list before mid point
        # Second half is the linked list after mid point
        # Also known as Floyd’s Tortoise and Hare (slow and fast pointer approach)

        fast, slow = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow

        # ------------------------------------------
        # Reverse second half

        prev, curr = None, mid

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second_head = prev

        # ------------------------------------------
        # Update link between first half and reversed second half

        first, second = head, second_head

        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp


# Time Complexity = O(N), Space Complexity = O(1)