# Problem description here https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    
# Time Complexity = O(N), Space Complexity = O(1)

"""

# Alternate solution (using bitwise &, little better time and space complexity)
# Known as Brian Kernighan’s Algorithm

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # Removes the rightmost 1-bit
            count += 1
        return count

# Time Complexity = O(k), Space Complexity = O(1)        
# where k is the number of 1s in the binary of n

"""