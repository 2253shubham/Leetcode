# Problem description here https://leetcode.com/problems/add-binary/description/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lg = max(len(a), len(b))
        while lg - len(a) > 0:
            a = "0" + a
        while lg - len(b) > 0:
            b = "0" + b
        sumn = ""
        carry = 0
        for i in range(lg - 1, -1, -1):
            s = int(a[i]) ^ int(b[i]) ^ carry
            carry = (int(a[i]) & int(b[i])) | (int(a[i]) & carry) | (int(b[i]) & carry)
            sumn = str(s) + sumn

        if carry:
            sumn = str(carry) + sumn

        return sumn


# Time Complexity = O(N), Space Complexity = O(N)
# where N is the length of the longest binary string
