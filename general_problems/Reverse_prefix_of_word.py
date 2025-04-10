# Problem description here https://leetcode.com/problems/reverse-prefix-of-word/description/


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[: i + 1][::-1] + word[i + 1 :]
        return word


# Time Complexity = O(N), Space Complexity = O(1)
