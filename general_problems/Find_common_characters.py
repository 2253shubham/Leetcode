# Problem description here https://leetcode.com/problems/find-common-characters/description/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cc = Counter(words[0])
        common = []
        for i in words[1:]:
            cc &= Counter(i)
        for key, value in cc.items():
            common.extend(key * value)
        
        return common
    
# Time Complexity = O(N*M), Space Complexity = O(1) 
# where N is the number of words and M is the average length of words