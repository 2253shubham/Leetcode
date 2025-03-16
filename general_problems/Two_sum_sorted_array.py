# Problem description here https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while numbers[right] + numbers[left] != target:
            if numbers[right] + numbers[left] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
    
# Time Complexity = O(N), Space Complexity = O(1)