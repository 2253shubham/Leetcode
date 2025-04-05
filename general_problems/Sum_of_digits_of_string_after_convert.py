# Problem description here https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ns = ""
        for i in s:
            ns += str(ord(i) - ord("a") + 1)

        def rec(ns, k):
            if k == 0:
                return int(ns)
            st = 0
            k -= 1
            for i in ns:
                st += int(i)
            return rec(str(st), k)

        return rec(ns, k)


# Time Complexity = O(N*K), Space Complexity = O(N)
# where N is the length of input string and K is number of interations
