# Problem description here https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty array

        i = 1  # Position to insert next valid element
        count = 1  # Tracks occurrences of current number

        for c in range(1, len(nums)):
            if nums[c] == nums[c - 1]:  # Duplicate found
                count += 1
            else:
                count = 1  # Reset count for new number
            
            if count <= 2:  # Allow at most two occurrences
                nums[i] = nums[c]
                i += 1

        return i  # New length of modified array
        

# Time Complexity = O(N), Space Complexity = O(1)


"""
# My original solution (Same time and space complexity)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        c = 1
        count = 1
        i = 1
        while c < l:
            curr = nums[c]
            if curr != nums[i - 1]:
                count = 0
                nums[i] = curr
                i += 1
                count += 1
                c += 1
            else:
                if count == 1:
                    nums[i] = curr
                    i += 1
                    count += 1
                    c += 1
                else:
                    count = 0
                    while c < l and curr == nums[c]:
                        c += 1
        return i
            
"""