# Problem description here https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/


class Solution:
    def minOperations(self, n: int) -> int:
        return (n**2) // 4


# Time Complexity = O(1), Space Complexity = O(1)

"""
# Alternate approach (O(N) time complexity)
        minm = 0
        for i in range(1, n, 2):
            minm += n - i
        
        return minm
"""
