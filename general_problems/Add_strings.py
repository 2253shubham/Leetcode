# Problem description here https://leetcode.com/problems/add-strings/description/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        results = []

        while i > -1 or j > -1 or carry:
            d1 = ord(num1[i]) - ord("0") if i > -1 else 0
            d2 = ord(num2[j]) - ord("0") if j > -1 else 0

            total = d1 + d2 + carry
            carry = total // 10
            results.append(str(total % 10))

            i -= 1
            j -= 1

        return "".join(results[::-1])


# Time Complexity = O(N) , Space Complexity = O(N)
