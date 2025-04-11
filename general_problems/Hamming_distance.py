# Problem description here

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the start and goal, then count the number of 1s in the result
        return bin(x ^ y).count('1')

# Time Complexity = O(N), Space Complexity = O(1)

"""
# Alternate solution (same time and space complexity)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def biny(num):
            s = ""
            while num != 0:
                s += str(num % 2)
                num = num // 2
            return s

        sstr = biny(x)
        estr = biny(y)
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