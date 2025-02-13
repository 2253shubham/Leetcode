# Problem description here https://leetcode.com/problems/reverse-bits/description/


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n & 0xFFFFFFFF)[2:].zfill(32)[::-1], base=2)


# Time Complexity = O(1), Space Complexity = O(1)
