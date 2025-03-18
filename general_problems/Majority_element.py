# Problem description here https://leetcode.com/problems/majority-element/description/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxm = 0
        idx = 0
        counter = 0
        for i in c.values():
            if i > maxm:
                idx = counter
                maxm = i
            counter += 1
        return list(c.keys())[idx]


# Time Complexity = O(N), Space Complexity = O(N)

"""
# Alternate solution (better space (O(1)) complexity) , Understand!!

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, count = nums[0], 1                   # curr will store the current majority element, count will store the count of the majority
        for i in nums[1:]:
            count += (1 if curr == i else -1)      # if i is equal to current majority, they're in same team, hence added, else one current majority and i both will be dead
            if not count:                          # if count of current majority is zero, then change the majority element, and start its count from 1
                curr = i
                count = 1
        return curr
"""
