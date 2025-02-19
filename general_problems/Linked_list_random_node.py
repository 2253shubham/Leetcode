# Problem description here https://leetcode.com/problems/linked-list-random-node/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        k = []
        head = self.head
        while head:
            k.append(head.val)
            head = head.next
        rnd = random.randint(0, len(k)-1)
        return k[rnd]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Time Complexity = O(N), Space Complexity = O(N)