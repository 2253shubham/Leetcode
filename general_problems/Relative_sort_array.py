# Problem description here https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count = Counter(arr1)
        output = []
        for i in arr2:
            output += [i]*count[i]
            del count[i]

        st = sorted(count)
        for i in st:
            output += [i]*count[i]

        return output       

# TIme Complexity = O(NlogN) , Space Complexity = O(N)