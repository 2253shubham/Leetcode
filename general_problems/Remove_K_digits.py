# Problem description here https://leetcode.com/problems/remove-k-digits/description/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        stack = stack[:-k] if k > 0 else stack

        result = "".join(stack).lstrip("0")

        return result if result else "0"


# Time Complexity = O(N), Space Complexity = O(N)
