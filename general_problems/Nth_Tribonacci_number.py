# Problem description here https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1     
        i = 0
        j = 1
        k = 1
        for count in range(n-2):
            sumn = i + j + k
            i = j
            j = k
            k = sumn

        return k
        
# Time Complexity = O(N), Space Complexity = O(1)