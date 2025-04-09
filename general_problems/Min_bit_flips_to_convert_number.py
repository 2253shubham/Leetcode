# Problem description here https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the start and goal, then count the number of 1s in the result
        return bin(start ^ goal).count('1')

# Time Complexity = O(N) , Space Complexity = O(N)

"""
# Alternate solution (same time and space complexity)

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def biny(num):
            s = ""
            while num != 0:
                s += str(num % 2)
                num = num // 2
            return s

        sstr = biny(start)
        estr = biny(goal)
        if len(sstr) > len(estr):
            for i in range(len(sstr) - len(estr)):
                estr += "0"
        else:
            for i in range(len(estr) - len(sstr)):
                sstr += "0"
        sstr = sstr[::-1]
        estr = estr[::-1]
        counter = 0
        for i in range(len(sstr) - 1, -1, -1):
            if sstr[i] == estr[i]:
                continue
            else:
                counter += 1
        return counter
"""