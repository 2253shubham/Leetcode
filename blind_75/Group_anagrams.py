# Problem description here https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicty = defaultdict(list)

        for i in strs:
            se = "".join(sorted(i))
            dicty[se].append(i)

        out = []
        for i in dicty.values():
            out.append(i)

        return out
    
# Time Complexity = O(N * MlogM), Space Complexity = O(N * M)
# Where N is the length of list, m is the length of each word in list

"""
# Better approach

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Time Complexity = O(N * M), Space Complexity = O(N)
# Where N is the length of list, m is the length of each word in list

"""