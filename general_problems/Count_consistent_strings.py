# Problem description here https://leetcode.com/problems/count-the-number-of-consistent-strings/description/


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        sa = set(allowed)
        for i in words:
            for l in i:
                if l not in sa:
                    counter += 1
                    break
        return len(words) - counter


# Time Complexity = O(N*M), Space Complexity = O(1)
# Where N is the number of words in string list and M is the average length of each word
