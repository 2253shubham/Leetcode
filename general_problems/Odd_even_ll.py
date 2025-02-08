# Problem description here https://leetcode.com/problems/odd-even-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head1 = head
        head2 = head.next
        head3 = head2

        while head2 and head2.next:
            head1.next = head1.next.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next
        head1.next = head3

        return head


# Time Complexity = O(N), Space Complexity = O(1)
