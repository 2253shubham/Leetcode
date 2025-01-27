# problem link here https://neetcode.io/problems/duplicate-integer

import collections


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        k = collections.Counter(nums)
        if max(k.values()) > 1:
            return True
        else:
            return False


"""
## with set() method

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
"""
