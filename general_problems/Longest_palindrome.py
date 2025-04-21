# Problem description here https://leetcode.com/problems/longest-palindrome/description/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        flag = 0
        for i in counter.values():
            if i % 2 == 0:
                length += i
            else:
                flag = 1
                length += i - 1
        return length + flag


# Time Complexity = O(N), Space Complexity = O(N)
