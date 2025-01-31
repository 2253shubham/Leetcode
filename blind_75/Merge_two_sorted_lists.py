# Problem description here https://leetcode.com/problems/merge-two-sorted-lists/submissions/1526029203/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        list3 = ListNode(0, None)
        dummy = list3
        while list1 and list2:
            if list1.val <= list2.val:
                temp = ListNode(list1.val)
                list3.next = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val)
                list3.next = temp
                list2 = list2.next
            list3 = list3.next

        list3.next = list1 if list1 else list2

        return dummy.next


# Time Complexity = O(N + M), Space Complexity = O(1)