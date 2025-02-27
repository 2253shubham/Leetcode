# Problem description here https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == [] or k > len(s):
            return 0

        freq = collections.Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(
                    self.longestSubstring(s[:i], k),
                    self.longestSubstring(s[i + 1 :], k),
                )

        return len(s)


# Time Complexity = O(NlogN), Space Complexity = O(N^2)


"""

# Sliding window approach (Time Complexity = O(N), Space Complexity = O(1))
# Understand it!!!

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        # get number of chars that have k occurances 
        # so we only look up to that many unique chars
        counts = Counter(s)
        maxchars = 1
        for char, occurances in counts.items():
            if occurances >= k:
                maxchars += 1
        count = 0
        for i in range(1, maxchars):
            count = max(count, self.helper(s, k, i))
        return count
    
    def helper(self, s, k, numUniqueTarget):
        start = end = uniqueCharsCount = charsAtLeastKCount = count = 0
        # count the 
        alphabet = [0] * 26
        
        def getAlphabetIndex(a):
            return ord(a) - 97

        while end < len(s):
            endAlphaIndex = getAlphabetIndex(s[end])
            # count end char
            alphabet[endAlphaIndex] += 1
            
            # count another unique if end char is newly seen
            if alphabet[endAlphaIndex] == 1:
                uniqueCharsCount += 1
            elif alphabet[endAlphaIndex] == k: 
                charsAtLeastKCount += 1

            end += 1
            
            # while we have more unique chars than our current target, move the start ptr
            while uniqueCharsCount > numUniqueTarget:
                startAlphaIdx = getAlphabetIndex(s[start])
                alphabet[startAlphaIdx] -= 1
                
                # decrement counts if this char fell below k or to 0
                if alphabet[startAlphaIdx] == k - 1: 
                    charsAtLeastKCount -= 1
                elif alphabet[startAlphaIdx] == 0: 
                    uniqueCharsCount -= 1
                    
                start += 1

            # if every char in substring has at least k count, we found a valid substring
            if uniqueCharsCount == charsAtLeastKCount: 
                count = max(count, end - start)

        return count

"""
