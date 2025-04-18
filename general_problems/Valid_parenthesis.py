# Problem description here https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        openb = []

        lookup = {"{": "}", "[": "]", "(": ")"}

        if len(s) % 2 == 1:
            return False

        for i in s:
            if i in lookup:
                openb.append(i)
            else:
                if len(openb) != 0 and lookup[openb[-1]] == i:
                    openb.pop()
                else:
                    return False

        return len(openb) == 0


# Time Complexity = O(N), Space Complexity = O(N)
